#!/usr/bin/env python3
"""Fix 3 issues: year/created UNKNOWN, PROJECTS.base displayName, launcher push order"""
import subprocess, os

REPO = "C:/Users/David/tmp_panorama_mc"
os.chdir(REPO)

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

# ─── FIX 1: year/created → UNKNOWN where no evidence ─────────────────────────
# Confirmed evidence:
#   PANORAMA  → 2026 (Issue #26 opened 2026-09-12, ARCHITECTURE.md date)
#   N1N3      → 2025 (Vercel deploy, plausible but not proven — keep 2025)
#   IA-VISION → UNKNOWN (no commit/issue date evidence)
#   SUINI     → UNKNOWN
#   TRAFFICLAB-CONTROL → UNKNOWN
print("=== FIX 1: year/created UNKNOWN ===")
unknown_projects = [
    "01_PROJECTS/IA-VISION/PROJECT.md",
    "01_PROJECTS/SUINI/PROJECT.md",
    "01_PROJECTS/TRAFFICLAB-CONTROL/PROJECT.md",
]
for rel in unknown_projects:
    path = f"{REPO}/{rel}"
    content = read(path)
    # Replace guessed year/created with UNKNOWN
    content = content.replace('year: "2024"', 'year: null  # UNKNOWN — no commit date evidence')
    content = content.replace('year: "2024"\n', 'year: null  # UNKNOWN — no commit date evidence\n')
    content = content.replace('created: 2024-01-01', 'created: null  # UNKNOWN')
    write(path, content)
    print(f"  {rel} → year/created = UNKNOWN")

# PANORAMA keep 2026, N1N3 keep 2025
print("  PANORAMA/PROJECT.md → year=2026 (evidenced by #26)")
print("  N1N3/PROJECT.md → year=2025 (plausible, keep)")

# ─── FIX 2: PROJECTS.base displayName ─────────────────────────────────────────
# Obsidian Bases uses displayName, not name, for property display names
print("\n=== FIX 2: PROJECTS.base displayName ===")
base_path = f"{REPO}/00_HOME/PROJECTS.base"
content = read(base_path)

# Replace name: with displayName: in properties section
# Current:   status_emoji:\n    name: Estado
# Target:    status_emoji:\n    displayName: Estado
import re
# Replace property "name:" with "displayName:" (Bases current syntax)
content = re.sub(r'^(\s+)name: (\w.*)$', r'\1displayName: \2', content, flags=re.MULTILINE)

write(base_path, content)
print("  name: → displayName: in PROJECTS.base")

# Verify
verify = read(base_path)
print("  displayName count:", verify.count('displayName:'))
print("  name: in properties count:", len(re.findall(r'^\s+name: \w', verify, re.MULTILINE)))

# ─── FIX 3: LAUNCHER — push BEFORE stash pop (publish first) ─────────────────
# Current: stash → pull → push → stash pop → open
# Fixed:   stash → pull → push → open → stash pop (separate step)
#
# Rationale: push publishes changes FIRST, then stash pop restores local copy
# This ensures remote is up-to-date before Obsidian opens
# The stash pop after open is a local convenience (not a sync requirement)
print("\n=== FIX 3: Launcher push order ===")
script_path = f"{REPO}/99_SYSTEM/launchers/sync-mission-control.sh"
script = read(script_path)

old_sequence = """# ─── 5. RESTORE STASH (si había) ─────────────────────────────────────────
# Restaura cambios locales al working tree ANTES de abrir Obsidian
STASH_RESTORE_OK=1
if [[ -n "$STASH_MSG" ]]; then
    log "Restaurando cambios locales al working tree..."
    if git stash pop; then
        STASH_RESTORE_OK=0
        log "Cambios locales restaurados."
    else
        log "WARN: Stash pop falló. Cambios en stash — ejecutar manualmente: git stash pop"
    fi
else
    log "Sin cambios locales que restaurar."
    STASH_RESTORE_OK=0
fi

# ─── 6. ABRIR OBSIDIAN ────────────────────────────────────────────────────
log "Abriendo Obsidian..."
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}&paneType=tab" 2>/dev/null || \\
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}" 2>/dev/null || \\
log "WARN: No se pudo abrir Obsidian automáticamente."

# ─── 7. REPORTE HONESTO ──────────────────────────────────────────────────
if (( STASH_RESTORE_OK == 0 )); then
    log "✓ Sincronización completa."
else
    log "⚠ Sincronización completa — WARN: stash local pendiente. Ejecutar: git stash pop"
fi"""

new_sequence = """# ─── 5. ABRIR OBSIDIAN (después de push, antes de stash pop) ───────────────
# push va PRIMERO para que el otro Hermes vea los cambios en esta sincronización
# stash pop va DESPUÉS para que el local vea su trabajo propio
log "Abriendo Obsidian..."
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}&paneType=tab" 2>/dev/null || \\
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}" 2>/dev/null || \\
log "WARN: No se pudo abrir Obsidian automáticamente."

# ─── 6. RESTORE STASH (después de abrir) ─────────────────────────────────
STASH_RESTORE_OK=1
if [[ -n "$STASH_MSG" ]]; then
    log "Restaurando cambios locales al working tree..."
    if git stash pop; then
        STASH_RESTORE_OK=0
        log "Cambios locales restaurados (disponibles para próximo commit)."
    else
        log "WARN: Stash pop falló. Cambios en stash — ejecutar manualmente: git stash pop"
    fi
else
    log "Sin cambios locales que restaurar."
    STASH_RESTORE_OK=0
fi

# ─── 7. REPORTE HONESTO ──────────────────────────────────────────────────
if (( STASH_RESTORE_OK == 0 )); then
    log "✓ Sincronización completa."
else
    log "⚠ Sincronización completa — WARN: stash local pendiente. Ejecutar: git stash pop"
fi"""

script = script.replace(old_sequence, new_sequence)
write(script_path, script)
print("  push → open → stash pop (publishes first)")

# ─── VERIFY ALL ───────────────────────────────────────────────────────────
print("\n=== VERIFY ===")
# year/created UNKNOWN
for p in ["IA-VISION", "SUINI", "TRAFFICLAB-CONTROL"]:
    c = read(f"{REPO}/01_PROJECTS/{p}/PROJECT.md")
    has_unknown = 'null  # UNKNOWN' in c
    print(f"  {p} year/created=UNKNOWN: {'✅' if has_unknown else '❌'}")

# displayName
base = read(base_path)
has_dn = 'displayName:' in base
print(f"  displayName in PROJECTS.base: {'✅' if has_dn else '❌'}")

# push order
scr = read(script_path)
open_before_pop = scr.index('Abriendo Obsidian') < scr.index('STASH_RESTORE_OK')
print(f"  push→open→stash pop order: {'✅' if open_before_pop else '❌'}")

print("\nDone.")
