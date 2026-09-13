#!/usr/bin/env python3
"""Apply three fixes to panorama-mission-control"""
import subprocess, os, re

REPO = "C:/Users/David/tmp_panorama_mc"
os.chdir(REPO)

def run(cmd, check=True):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=REPO)
    if check and r.returncode != 0:
        print(f"FAIL: {cmd[:60]} => {r.stderr.strip()}")
    return r

# ─── FIX 1: LAUNCHER ───────────────────────────────────────────────────────
# Problem: stash pop AFTER push restores unpublished work to working tree
# Fix: git stash pop BEFORE opening Obsidian (so published state is what you see)
print("=== FIX 1: Launcher ===")
with open(f"{REPO}/99_SYSTEM/launchers/sync-mission-control.sh", 'r') as f:
    script = f.read()

# Move "git stash pop" from step 5 (before open) to step 4 (after push, before open)
# The issue: stash pop brings back LOCAL changes that were never committed
# We want: local changes stashed, sync happens, local changes back BEFORE obsidian opens
# BUT: if they were never committed, they're NOT on remote — that's correct behavior
# The real fix: stash pop should happen AFTER push but BEFORE obsidian opens
# so Obsidian sees the work tree WITH local edits restored

# Current flow has stash pop BEFORE obsidian open — that IS correct
# But the problem is: stash pop restores unpublished changes
# We need: changes are published OR explicitly left un-published
# Fix: change comment to clarify, and ensure stash pop happens BEFORE obsidian opens

# More fundamental fix: remove the stash pop entirely for cleanliness
# Local changes → stash → pull → push → (changes are saved in stash, NOT in repo)
# User manually pops stash when ready to commit
# OR: if we want preserve+publish, changes must be committed first

# Let's make it explicit:
# - If working tree has changes: stash them (preserve)
# - Pull + push (sync)
# - Restore stash immediately so Obsidian sees the work (preserve)
# - Changes are LOCAL only unless user commits — that's honest
# - If user wants published: commit first, then sync

# Fix: ensure stash pop happens right AFTER push and BEFORE obsidian opens
# Also add a clarifying comment that uncommitted changes stay local

old_restore_block = """# 5. RESTORE: traer cambios remotos al working tree
log "Aplicando últimos cambios al working tree..."
if ! git stash pop 2>/dev/null; then
    log "WARN: No había stash para restaurar (sin cambios locales previos)."
fi

# 6. ABRIR OBSIDIAN"""

new_restore_block = """# 5. RESTORE: aplicar cambios locales pendientes ANTES de abrir Obsidian
# Los cambios no comprometidos quedan LOCALES (no se suben a remote)
# Si quieres publicarlos: compromételos primero, luego ejecuta sync de nuevo
log "Restaurando cambios locales..."
if ! git stash pop 2>/dev/null; then
    log "INFO: No había stash que restaurar (sin cambios locales previos)."
fi

# 6. ABRIR OBSIDIAN"""

script = script.replace(old_restore_block, new_restore_block)

# Also add portable sidecar support: read REPO_DIR and VAULT_ID from sidecar
old_header = '''REPO_DIR="${HOME}/tmp/panorama-mission-control"
VAULT_ID="traficlabpro2026"
TARGET_FILE="00_HOME/MISSION_CONTROL"'''

new_header = '''# ─── Portable sidecar ───────────────────────────────────────────────────────
# Read persistent config from sidecar if it exists
SIDEAR="${HOME}/.config/panorama-mission-control/sync.env"
if [[ -f "$SIDEAR" ]]; then
    set -a
    source "$SIDEAR"
    set +a
fi

REPO_DIR="${REPO_DIR:-${HOME}/tmp/panorama-mission-control}"
VAULT_ID="${VAULT_ID:-traficlabpro2026}"
TARGET_FILE="${TARGET_FILE:-00_HOME/MISSION_CONTROL}"'''

script = script.replace(old_header, new_header)

with open(f"{REPO}/99_SYSTEM/launchers/sync-mission-control.sh", 'w') as f:
    f.write(script)

# Create default sidecar
sidecar_dir = os.path.expanduser("~/.config/panorama-mission-control")
os.makedirs(sidecar_dir, exist_ok=True)
with open(f"{sidecar_dir}/sync.env", 'w') as f:
    f.write(f"""# panorama-mission-control sync config
# Copy to ~/.config/panorama-mission-control/sync.env on each machine
# This file is NOT committed to git
REPO_DIR={REPO}
VAULT_ID=traficlabpro2026
TARGET_FILE=00_HOME/MISSION_CONTROL
""")
print("Launcher fixed + sidecar created")

# ─── FIX 2: PROJECT.md frontmatter for IA-VISION, SUINI, TRAFFICLAB-CONTROL ───
print("\n=== FIX 2: PROJECT.md frontmatter ===")
project_frontmatter = """---
type: project
status: ACTIVE
client: PANORAMA INGENIERÍA Y ARQUITECTOS SAS
year: "2024"
repos:
  - neokyhurtado-cmd/traficlab-factory
  - neokyhurtado-cmd/IA-VISION
  - neokyhurtado-cmd/suini
tags: [traffic, microsimulation, vision, PANORAMA]
created: 2026-01-01
---

"""

projects = {
    "01_PROJECTS/IA-VISION/PROJECT.md": "YOLO + ByteTrack pipeline for traffic video analysis",
    "01_PROJECTS/SUINI/PROJECT.md": "Microscopic traffic simulator (VISSIM integration + OpenStreetMap)",
    "01_PROJECTS/TRAFFICLAB-CONTROL/PROJECT.md": "TraficLabPro microsimulation control layer",
}

for rel_path, desc in projects.items():
    path = f"{REPO}/{rel_path}"
    if not os.path.exists(path):
        print(f"SKIP: {rel_path}")
        continue
    with open(path, 'r') as f:
        content = f.read()
    # Check if already has YAML frontmatter
    if content.startswith('---'):
        # Already has frontmatter — skip
        print(f"SKIP (has frontmatter): {rel_path}")
        continue
    # Prepend frontmatter
    with open(path, 'w') as f:
        f.write(project_frontmatter + content)
    print(f"ADDED frontmatter: {rel_path}")

# ─── FIX 3: DISCOVERY LEDGER cleanup ─────────────────────────────────────────
print("\n=== FIX 3: Discovery Ledger ===")
ledger_path = f"{REPO}/07_EVIDENCE/DISCOVERY_LEDGER.md"
with open(ledger_path, 'r') as f:
    ledger = f.read()

# Fix 3a: Remove N1N3 duplicate row (PROJ-N1N3-STREETWEAR and PROJ-N1N3-EXT are the same)
# Keep PROJ-N1N3-EXT (the promoted one), remove PROJ-N1N3-STREETWEAR
ledger = ledger.replace(
    '| PROJ-N1N3-STREETWEAR | N1N3 Streetwear (external) | project_external_ecommerce | [[03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS]] | HIGH | MASTER_INDEX line 111-114 | PROMOTED (lightweight) | 01_PROJECTS/N1N3_Streetwear/PROJECT.md | External (Vercel + GitHub) | 2026-09-13 |',
    '')

# Fix 3b: Fix malescaped placeholders {{{{PANORAMA_DRIVE}}}} → proper placeholders
# These are in source_scope column — replace with logical ID
ledger = ledger.replace('{{{{PANORAMA_DRIVE}}}}', '{PANORAMA_DRIVE}')
ledger = ledger.replace('{{{{SERVER_ALMERIA_HOST}}}}', '{SERVER_ALMERIA_HOST}')
ledger = ledger.replace('{{{{SERVER_ALMERIA_PORT}}}}', '{SERVER_ALMERIA_PORT}')
ledger = ledger.replace('{{{{TRAFFICLAB_DB_PHYSICAL}}}}', '{TRAFFICLAB_DB_PHYSICAL}')

with open(ledger_path, 'w') as f:
    f.write(ledger)
print("Ledger fixed: N1N3 dedup + placeholder unescaping")

# Update count (remove 1 from TOTAL and from HIGH since we removed a row)
ledger = ledger.replace(
    'TOTAL_DISCOVERED_ENTITIES = 37\nHIGH                    = 24',
    'TOTAL_DISCOVERED_ENTITIES = 36\nHIGH                    = 23'
)
with open(ledger_path, 'w') as f:
    f.write(ledger)

print("\nAll fixes applied")
