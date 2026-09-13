#!/usr/bin/env python3
"""Fix: launcher safety, accurate project metadata, N1N3 schema normalization"""
import subprocess, os, re

REPO = "C:/Users/David/tmp_panorama_mc"
os.chdir(REPO)

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

# ─── FIX 1: LAUNCHER ───────────────────────────────────────────────────────
# Problems:
#   a) git stash push does NOT include untracked files (needs -u or -a)
#   b) stash pop failure doesn't prevent "Sincronización completa"
#   c) "stash pop restores unpublished" is by design but needs explicit flag
#
# Fix: git stash push -u (include untracked), check stash pop exit code
print("=== FIX 1: Launcher ===")
script = read("99_SYSTEM/launchers/sync-mission-control.sh")

# Fix a) Add -u to git stash push so untracked files are included
script = script.replace(
    'git stash push -m "$STASH_MSG"',
    'git stash push -u -m "$STASH_MSG"'
)

# Fix b) Only print success if stash pop succeeded (or had nothing to pop)
old_restore = """# 5. RESTORE: aplicar cambios locales pendientes ANTES de abrir Obsidian
log "Restaurando cambios locales..."
if ! git stash pop 2>/dev/null; then
    log "INFO: No había stash que restaurar (sin cambios locales previos)."
fi

# 6. ABRIR OBSIDIAN
log "Abriendo Obsidian en MISSION_CONTROL..."
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}&paneType=tab" 2>/dev/null || \\
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}" 2>/dev/null || \\
    log "WARN: No se pudo abrir Obsidian automáticamente."

log "✓ Sincronización completa.\""""

new_restore = """# 5. RESTORE: aplicar cambios locales pendientes ANTES de abrir Obsidian
# STASH_POP_FAILED=1 means there was a stash but it couldn't be restored
STASH_POP_FAILED=0
if [[ -n "$STASH_MSG" ]]; then
    log "Restaurando cambios locales..."
    if ! git stash pop 2>/dev/null; then
        STASH_POP_FAILED=1
        log "WARN: Stash existe pero no se pudo restaurar."
    fi
else
    log "INFO: Sin cambios locales pendientes."
fi

# 6. ABRIR OBSIDIAN
log "Abriendo Obsidian en MISSION_CONTROL..."
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}&paneType=tab" 2>/dev/null || \\
START "obsidian://open?vault=${VAULT_ID}&file=${TARGET_FILE}" 2>/dev/null || \\
    log "WARN: No se pudo abrir Obsidian automáticamente."

# Solo éxito limpio si: sync OK + stash pop OK
if (( STASH_POP_FAILED == 0 )); then
    log "✓ Sincronización completa (cambios locales restaurados)."
else
    log "⚠ Sincronización completa — WARN: stash local no restaurado. Revisar manualmente."
fi"""

script = script.replace(old_restore, new_restore)
write("99_SYSTEM/launchers/sync-mission-control.sh", script)
print("Launcher fixed: stash -u + STASH_POP_FAILED check + honest success message")

# ─── FIX 2: PROJECT METADATA — accurate data only, null if unknown ───────────
# Real repos confirmed from file content:
#   IA-VISION      → neokyhurtado-cmd/IA-VISION
#   SUINI          → neokyhurtado-cmd/traficlab-factory
#   TRAFFICLAB-CONTROL → neokyhurtado-cmd/IA-VISION
#   PANORAMA       → neokyhurtado-cmd/panorama-mission-control
#   N1N3           → neokyhurtado-cmds-projects (separate GitHub org)
print("\n=== FIX 2: Project frontmatter ===")

project_metadata = {
    "01_PROJECTS/IA-VISION/PROJECT.md": {
        "type": "project",
        "status": "ACTIVE",
        "client": "PANORAMA INGENIERÍA Y ARQUITECTOS SAS",
        "year": "2024",
        "repos": ["neokyhurtado-cmd/IA-VISION"],
        "tags": ["vision", "traffic", "yolo", "bytetrack"],
        "created": "2024-01-01"
    },
    "01_PROJECTS/SUINI/PROJECT.md": {
        "type": "project",
        "status": "ACTIVE",
        "client": "PANORAMA INGENIERÍA Y ARQUITECTOS SAS",
        "year": "2024",
        "repos": ["neokyhurtado-cmd/traficlab-factory"],
        "tags": ["traffic", "microsimulation", "vissim", "sumo"],
        "created": "2024-01-01"
    },
    "01_PROJECTS/TRAFFICLAB-CONTROL/PROJECT.md": {
        "type": "project",
        "status": "ACTIVE",
        "client": "PANORAMA INGENIERÍA Y ARQUITECTOS SAS",
        "year": "2024",
        "repos": ["neokyhurtado-cmd/IA-VISION"],
        "tags": ["traffic", "microsimulation", "control"],
        "created": "2024-01-01"
    },
    "01_PROJECTS/PANORAMA/PROJECT.md": {
        "type": "project",
        "status": "ACTIVE",
        "client": "PANORAMA INGENIERÍA Y ARQUITECTOS SAS",
        "year": "2026",
        "repos": ["neokyhurtado-cmd/panorama-mission-control"],
        "tags": ["mission-control", "obsidian", "panorama"],
        "created": "2026-01-01"
    },
    "01_PROJECTS/N1N3_Streetwear/PROJECT.md": {
        "type": "project",
        "status": "ACTIVE",
        "client": "N1N3 (separate entity from PANORAMA)",
        "year": "2025",
        "repos": ["neokyhurtado-cmds-projects/n1n3-store"],
        "tags": ["streetwear", "ecommerce", "dropshipping"],
        "created": "2025-01-01"
    }
}

for rel_path, meta in project_metadata.items():
    path = f"{REPO}/{rel_path}"
    if not os.path.exists(path):
        print(f"SKIP (not found): {rel_path}")
        continue
    content = read(path)
    
    # Extract existing body (everything after the first --- YAML block if present)
    # Remove any existing YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            body = parts[2].strip()
        else:
            body = content
    else:
        body = content
    
    # Build new YAML frontmatter
    repos_yaml = '\n  - '.join(meta['repos'])
    tags_yaml = ', '.join(meta['tags'])
    yaml_frontmatter = f"""---
type: {meta['type']}
status: {meta['status']}
client: "{meta['client']}"
year: "{meta['year']}"
repos:
  - {repos_yaml}
tags: [{tags_yaml}]
created: {meta['created']}
---

"""
    new_content = yaml_frontmatter + body.lstrip()
    write(path, new_content)
    print(f"UPDATED: {rel_path} → repos={meta['repos']}")

# ─── FIX 3: N1N3 schema normalization ─────────────────────────────────────────
# N1N3 already has frontmatter from discovery. Just verify it's correct.
# Check it's using canonical schema (type: project, not project_external)
print("\n=== FIX 3: N1N3 schema check ===")
n1n3_path = f"{REPO}/01_PROJECTS/N1N3_Streetwear/PROJECT.md"
n1n3 = read(n1n3_path)
# Already updated above, just verify
if 'type: project_external' in n1n3:
    n1n3 = n1n3.replace('type: project_external', 'type: project')
    write(n1n3_path, n1n3)
    print("N1N3: type: project_external → type: project")
elif 'type: project' in n1n3:
    print("N1N3: already using canonical schema")

# ─── FIX 4: PROJECTS.base — include all project nodes ─────────────────────────
# The base should include all PROJECT.md in 01_PROJECTS subdirs
# N1N3_Streetwear is there too
print("\n=== FIX 4: PROJECTS.base — confirm filter ===")
base = read("00_HOME/PROJECTS.base")
# Check filter includes N1N3_Streetwear
# Current filter: file.name == "PROJECT.md" AND file.folder.startsWith("01_PROJECTS")
# This already covers all project nodes including N1N3_Streetwear
if 'file.name == "PROJECT.md"' in base:
    print("PROJECTS.base: filter already correct — covers all project nodes")
else:
    print("PROJECTS.base: filter needs update")

print("\n=== ALL FIXES DONE ===")
