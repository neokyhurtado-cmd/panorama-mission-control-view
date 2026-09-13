#!/usr/bin/env bash
# sync-mission-control.sh — PORTABLE 2-HOST SYNC
# Per panorama-mission-control#2 / 5650586361 (audit on HEAD 54471f8).
#
# Real flow (audit-verified):
#   1. Sidecar resolve (host-specific values)
#   2. CHECKPOINT: stash push -u (tracked + untracked)
#   3. FETCH origin main
#   4. PULL --no-rebase (on conflict: restore + exit 1)
#   5. RESTORE local edits BEFORE commit/push (per #5650586361: same open, not held back)
#   6. COMMIT local edits + PUSH origin main
#   7. OPEN Obsidian
#
# Failure modes:
#   exit 0 = sync complete
#   exit 1 = pull conflict (local restored, conflict documented in 90_INBOX/CONFLICTS/)
#   exit 4 = restore FAILED (local edits preserved in stash, NO success lie)

set -euo pipefail

# ─── Sidecar resolution (host-specific values) ────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SIDE_CANDIDATES=(
    "$SCRIPT_DIR/.env.local"
    "$SCRIPT_DIR/../.env.local"
    "$HOME/.config/panorama-mission-control/sync.env"
    "$HOME/.config/hermes/mission-control.env"
)
SIDE_FILE=""
for f in "${SIDE_CANDIDATES[@]}"; do
    if [ -f "$f" ]; then
        SIDE_FILE="$f"
        break
    fi
done
if [ -n "$SIDE_FILE" ]; then
    # shellcheck disable=SC1090
    set -a
    source "$SIDE_FILE"
    set +a
fi

REPO_DIR="${REPO_DIR:-${HOME}/tmp/panorama-mission-control}"
VAULT_ID="${VAULT_ID:-traficlabpro2026}"
TARGET_FILE="${TARGET_FILE:-00_HOME/MISSION_CONTROL}"

# ─── Identity (best-effort) ────────────────────────────────────────────────
HOST_ROLE="${HOST_ROLE:-UNKNOWN}"
DEVICE_ID_LOCAL="${DEVICE_ID:-UNKNOWN}"
AGENT_ID_LOCAL="${AGENT_ID:-UNKNOWN}"

log() { echo "[sync-mission-control $(date +%H:%M:%S)] host=$HOST_ROLE device=$DEVICE_ID_LOCAL $1"; }
die() { log "ERROR: $1"; exit 1; }

log "sidecar=${SIDE_FILE:-NONE}"
cd "$REPO_DIR" || die "REPO_DIR=$REPO_DIR no accesible."

# ─── 1. CHECKPOINT (tracked + untracked) ───────────────────────────────────
HAS_CHANGES=0
if [ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
    HAS_CHANGES=1
fi
if ! git diff --quiet 2>/dev/null; then
    HAS_CHANGES=1
fi
if ! git diff --cached --quiet 2>/dev/null; then
    HAS_CHANGES=1
fi

STASH_REF=""
STASH_MSG=""
if (( HAS_CHANGES )); then
    STASH_MSG="checkpoint-$(date +%Y%m%d_%H%M%S)-by-$HOST_ROLE"
    log "1/7 stash push -u (tracked + untracked)..."
    if ! git stash push -u -m "$STASH_MSG" 2>&1 | head -1; then
        die "stash push falló. Abortando para no perder cambios."
    fi
    # Verify stash happened
    if ! git stash list 2>/dev/null | grep -q "$STASH_MSG"; then
        die "stash verification falló. Abortando."
    fi
    STASH_REF="$STASH_MSG"
    log "   stash ref: $STASH_REF"
else
    log "1/7 sin cambios locales."
fi

# ─── 2. FETCH ──────────────────────────────────────────────────────────────
log "2/7 fetch origin main..."
if ! git fetch origin main; then
    [ -n "$STASH_REF" ] && git stash pop || true
    die "fetch falló."
fi

# ─── 3. PULL --no-rebase ───────────────────────────────────────────────────
log "3/7 pull origin main --no-rebase..."
PULL_OK=0
if git pull origin main --no-rebase 2>/dev/null; then
    PULL_OK=1
fi

if (( ! PULL_OK )); then
    log "3/7 pull conflicto. Documentando en 90_INBOX/CONFLICTS/..."
    CONFLICT_FILE="90_INBOX/CONFLICTS/$(date +%Y%m%d_%H%M%S)_conflict.md"
    mkdir -p "$(dirname "$CONFLICT_FILE")"
    {
        echo "# Conflicto de sincronizacion $(date -Iseconds)"
        echo "REMOTE_HEAD: $(git rev-parse origin/main 2>/dev/null || echo UNKNOWN)"
        echo "LOCAL_REF:   $(git rev-parse HEAD 2>/dev/null || echo UNKNOWN)"
        echo "HOST_ROLE:   $HOST_ROLE"
        echo "DEVICE_ID:   $DEVICE_ID_LOCAL"
        echo "AGENT_ID:    $AGENT_ID_LOCAL"
        echo ""
        echo "## Estado git"
        git status || true
        echo ""
        echo "## Archivos en conflicto"
        git diff --name-only --diff-filter=U || true
    } > "$CONFLICT_FILE"
    log "   conflicto en $CONFLICT_FILE"
    if [ -n "$STASH_REF" ]; then
        if ! git stash pop 2>/dev/null; then
            log "3/7 FAIL CLOSED: stash no restaurable en conflicto. Cambios en stash."
            exit 4
        fi
        log "   stash restaurado."
    fi
    log "3/7 sincronizacion incompleta. Resolver manualmente."
    exit 1
fi

# ─── 4. RESTORE LOCAL EDITS BEFORE COMMIT/PUSH ────────────────────────────
# Per #5650586361: local edits must be PUBLISHED on same open, not held back.
if [ -n "$STASH_REF" ]; then
    log "4/7 stash pop (publicar cambios locales antes de push)..."
    if ! git stash pop 2>/dev/null; then
        log "4/7 FAIL CLOSED: no se pudo restaurar stash despues de pull."
        log "   Cambios preservados en: $(git stash list 2>/dev/null | head -3)"
        log "   Para resolver: cd $REPO_DIR && git stash pop"
        exit 4
    fi
    log "   stash restaurado."
fi

# ─── 5. COMMIT local edits + PUSH ──────────────────────────────────────────
log "5/7 verificar cambios locales para commitear..."
if ! git diff --quiet 2>/dev/null || [ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
    log "   hay cambios para commitear."
    git add -A
    # Excluir secretos/env
    if git diff --cached --name-only 2>/dev/null | grep -qE "(\.env$|\.env\.local$|^secrets/|^\.ssh/|^\.aws/)"; then
        log "5/7 ABORT: cambios staged contienen secretos/env. Revisar manualmente."
        exit 5
    fi
    if ! git diff --cached --quiet 2>/dev/null; then
        # Pre-check: is there anything actually staged?
        STAGED_COUNT=$(git diff --cached --name-only 2>/dev/null | wc -l)
        if (( STAGED_COUNT == 0 )); then
            log "   nothing to commit."
        else
            log "   staged: $STAGED_COUNT files."
            COMMIT_MSG="chore(sync): $HOST_ROLE local edits $(date -Iseconds)"
            # Use git status to capture real failures (identity, hooks, perms)
            COMMIT_OUT=$(git commit -m "$COMMIT_MSG" 2>&1)
            COMMIT_RC=$?
            echo "$COMMIT_OUT" | head -3
            if (( COMMIT_RC != 0 )); then
                # Distinguish 'nothing to commit' (pre-checked, should not happen)
                # from REAL failures (identity, hook, perms)
                if echo "$COMMIT_OUT" | grep -qE "nothing to commit|no changes added"; then
                    log "   nothing to commit (race with pre-check)."
                else
                    # REAL FAILURE: identity, hook, perms, etc. FAIL CLOSED.
                    log "5/7 FAIL CLOSED: git commit fallo (rc=$COMMIT_RC). NO se hace push."
                    log "   Output: $COMMIT_OUT" | head -5
                    log "   Cambios locales preservados en working tree (NO commit NO push)."
                    log "   Resolver manualmente: cd $REPO_DIR && git status"
                    exit 6
                fi
            fi
            log "   commit OK."
            log "   push to origin/main..."
            if ! git push origin main 2>&1; then
                log "5/7 FAIL CLOSED: git push failed. Changes committed locally but not published."
                exit 7
            fi
            log "   push OK."
        fi
    fi
fi

# ─── 6. OPEN OBSIDIAN ─────────────────────────────────────────────────────────
# Full procedure: kill → set lastOpenVault → launch vault → open file
log "6/7 restarting Obsidian with panorama-mission-control vault..."

# 6a. Kill all Obsidian processes (avoid stale state from wrong vault)
if tasklist //FI "IMAGENAME eq Obsidian.exe" 2>/dev/null | grep -q "Obsidian.exe"; then
    log "   killing existing Obsidian processes..."
    taskkill //F //IM Obsidian.exe 2>/dev/null || true
    sleep 2
fi

# 6b. Set lastOpenVault = panorama-mission-control in obsidian.json
OBSIDIAN_JSON="C:/Users/David/AppData/Roaming/obsidian/obsidian.json"
PYTHON_UPDATE="
import json, os, sys
cfg = os.path.expanduser('$OBSIDIAN_JSON')
with open(cfg) as f:
    d = json.load(f)
vaults = d.get('vaults', {})
# Ensure panorama-mission-control is registered
pm_path = os.path.expandvars(os.path.join(os.environ.get('REPO_DIR', r'C:\\Users\\David\\tmp_panorama_mc')))
if 'panorama-mission-control' not in vaults:
    vaults['panorama-mission-control'] = {'path': pm_path}
    d['vaults'] = vaults
    with open(cfg, 'w') as f:
        json.dump(d, f, indent=2)
    print(f'Registered panorama-mission-control -> {pm_path}')
# Set as lastOpenVault
d['lastOpenVault'] = 'panorama-mission-control'
with open(cfg, 'w') as f:
    json.dump(d, f, indent=2)
print('lastOpenVault = panorama-mission-control')
"
python3 -c "$PYTHON_UPDATE" 2>&1 || log "   WARN: python update failed (vault may already be correct)"

# 6c. Launch Obsidian (no --vault flag — reads lastOpenVault from obsidian.json)
OBSIDIAN_EXE="${OBSIDIAN_EXE:-${LOCALAPPDATA:+$LOCALAPPDATA/Programs/obsidian/Obsidian.exe}}"
OBSIDIAN_EXE="${OBSIDIAN_EXE:-C:/Users/David/AppData/Local/Programs/obsidian/Obsidian.exe}"
log "   launching Obsidian..."
"/c/Users/David/AppData/Local/Programs/obsidian/Obsidian.exe" &
sleep 4

# 6d. Open MISSION_CONTROL.md via URI
log "   opening 00_HOME/MISSION_CONTROL.md..."
START "" "obsidian://open?vault=panorama-mission-control&file=00_HOME/MISSION_CONTROL.md" 2>/dev/null || true

log "6/7 Obsidian launched with panorama-mission-control vault."

# ─── 7. VERIFY CLEAN BEFORE SUCCESS ────────────────────────────────────────
# Before declaring success, verify working tree is clean (no uncommitted edits pending)
log "7/7 verificando estado final..."
PENDING=0
if ! git diff --quiet 2>/dev/null; then PENDING=1; fi
if ! git diff --cached --quiet 2>/dev/null; then PENDING=1; fi
if [ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then PENDING=1; fi

if (( PENDING == 1 )); then
    log "WARN: cambios pendientes no comprometidos. Revisar manualmente."
    log "WARN: sync completed but working tree not clean."
else
    log "7/7 OK. MISSION_CONTROL published en origin/main."
fi
exit 0
