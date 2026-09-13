# UNKNOWN CLASSIFICATION (PC-A evidence)

PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:15:47Z
  RESULT: unknown_classification_scaffold
  PC_B: BLOCKED_EXTERNAL_ACCESS

## Categories (from inventory)

### UNKNOWN_TYPE_1: Not-a-vault paths (V5, V6)
- V5 = C:/Users/david/vault/ — artefacto NVSSDK mal nombrado (3 archivos)
- V6 = X:/ — drive raíz, marcador residual .obsidian/ vacío (1.1 TB)
- ACTION: ignore (not Obsidian vaults); documented in inventory_report.md

### UNKNOWN_TYPE_2: Subcarpetas recursivas (00_VAULT_OBSIDIAN dentro de sí mismo)
- V2 contains `00_VAULT_OBSIDIAN/` as subfolder
- V3 contains `00_VAULT_OBSIDIAN/` as subfolder
- V4 contains `00_VAULT_OBSIDIAN/` + `vault/` as subfolders
- ACTION: flag for triage in step 6 (project nodes creation)

### UNKNOWN_TYPE_3: Files >1 MB binaries
- V2: 39 archivos >1 MB (modelos .pt ~10-50 MB, tracks JSON, CSV consolidados, vendor_deckgl.min.js)
- V3: 5 archivos >1 MB
- V4: 5 archivos >1 MB
- ACTION: classify each as model / tracks / attachment / vendor; per protocol use punteros not copies

### UNKNOWN_TYPE_4: Filename collisions (1881 duplicates across 2+ vaults)
- V3 ↔ V4: 1881 filenames shared (97% clone)
- V2 unique to itself except `MEMORY.md` + `README.md` (in 3 vaults)
- ACTION: dedup analysis (see duplicates.md in inventory/)

### UNKNOWN_TYPE_5: 00_Indice.md carpeta/archivo
- V4 has `00_Indice.md` as both a file and a subfolder
- OneDrive sync symptom, not data loss
- ACTION: ignore; document as OneDrive artifact

### UNKNOWN_TYPE_6: Permission denied (V3 app.json)
- OneDrive held lock on V3 .obsidian/app.json
- 2-byte file, unreadable during inventory
- ACTION: retry next session; if still blocked, document as caveat

### UNKNOWN_TYPE_7: PC-B contents (BLOCKED)
- All content from second physical PC is UNKNOWN
- Cannot be classified without host access
- ACTION: depends on PC-B host access

ORIGINALS_MODIFIED = 0
PC_B: BLOCKED_EXTERNAL_ACCESS
