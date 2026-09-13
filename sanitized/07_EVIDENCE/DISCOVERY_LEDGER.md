---
type: discovery_ledger
title: DISCOVERY LEDGER — Canonical Inventory of Discovered Entities
description: One row per entity discovered from OneDrive scan + local roots. Source of truth for HIGH/MEDIUM/LOW counts.
scan_authority: HERMES_PERSONAL (OneDrive) + HERMES_SERVER (labeling + reconciliation)
labeling_authority: HERMES_SERVER
created: 2026-09-13
---

# DISCOVERY LEDGER — Canonical

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T03:07:18Z
```

This ledger is the **durable source of truth** for entity classification. Every entity discovered from OneDrive scan or local roots has exactly one row here. Counts (HIGH/MEDIUM/LOW) reported elsewhere must reconcile to this ledger.

## Schema (one row per entity)

| logical_id | name | entity_type | relation/parent | confidence | evidence_pointer | decision | destination | source_scope | last_seen |

## Rows

| logical_id | name | entity_type | relation/parent | confidence | evidence_pointer | decision | destination | source_scope | last_seen |
|------------|------|-------------|-------------------|------------|-------------------|----------|-------------|--------------|-----------|
| PROJ-TRAFICLABPRO | TraficLabPro (IA-VISION) | project_active | [[01_PROJECTS/IA-VISION]][[01_PROJECTS/TRAFFICLAB-CONTROL]] | HIGH | MASTER_INDEX + IA-VISION/TRAFFICLAB-CONTROL/STATE_POINTERS.md | ALREADY_PROMOTED | 01_PROJECTS/IA-VISION + 01_PROJECTS/TRAFFICLAB-CONTROL | SHARED_ONEDRIVE + LOCAL_DISCS | 2026-09-13 |

| CLIENT-PANORAMA-INGENIERIA | PANORAMA INGENIERÍA Y ARQUITECTOS SAS | company | [[02_COMPANY]] | HIGH | MASTER_INDEX + NIT 901384855-2 | ALREADY_PROMOTED | 03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md | SHARED_ONEDRIVE + NIT public registry | 2026-09-13 |
| CLIENT-CTIC-IDU | CTIC / IDU | client_frequent | [[03_CLIENTS/CTIC_IDU]] | HIGH | MASTER_INDEX + 03_CLIENTS/CTIC_IDU.md | ALREADY_PROMOTED | 03_CLIENTS/CTIC_IDU.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-ASYDU | ASYDU | client_frequent | [[03_CLIENTS/ASYDU]] | HIGH | MASTER_INDEX + 03_CLIENTS/ASYDU.md | ALREADY_PROMOTED | 03_CLIENTS/ASYDU.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-FERREIRA | FERREIRA | client_frequent | [[03_CLIENTS/FERREIRA]] | HIGH | MASTER_INDEX + 03_CLIENTS/FERREIRA.md | ALREADY_PROMOTED | 03_CLIENTS/FERREIRA.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-MUTIS | MUTIS | client_frequent | [[03_CLIENTS/MUTIS]] | HIGH | MASTER_INDEX + 03_CLIENTS/MUTIS.md | ALREADY_PROMOTED | 03_CLIENTS/MUTIS.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-COLPATRIA | COLPATRIA | client_frequent | [[03_CLIENTS/COLPATRIA]] | HIGH | MASTER_INDEX + 03_CLIENTS/COLPATRIA.md | ALREADY_PROMOTED | 03_CLIENTS/COLPATRIA.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-OCTAVIO-MILLAN | OCTAVIO MILLÁN | client_frequent | [[03_CLIENTS/OCTAVIO_MILLAN]] | HIGH | MASTER_INDEX + 03_CLIENTS/OCTAVIO_MILLAN.md | ALREADY_PROMOTED | 03_CLIENTS/OCTAVIO_MILLAN.md | SHARED_ONEDRIVE | 2026-09-13 |
| CLIENT-WILSON-BRAVO | Ing Wilson Bravo | client_frequent | [[03_CLIENTS/WILSON_BRAVO]] | HIGH | MASTER_INDEX + 03_CLIENTS/WILSON_BRAVO.md | ALREADY_PROMOTED | 03_CLIENTS/WILSON_BRAVO.md | SHARED_ONEDRIVE | 2026-09-13 |
| QUOT-2024 | Quotations 2024 | quotations_index | [[04_RESEARCH/QUOTATIONS_2024]] | HIGH | 04_RESEARCH/QUOTATIONS_2024.md + MASTER_INDEX COTIZACIONES/ | ALREADY_PROMOTED | 04_RESEARCH/QUOTATIONS_2024.md | SHARED_ONEDRIVE | 2026-09-13 |
| QUOT-2025 | Quotations 2025 | quotations_index | [[04_RESEARCH/QUOTATIONS_2025]] | HIGH | 04_RESEARCH/QUOTATIONS_2025.md + MASTER_INDEX PANORAMA INGENIERIA 2025/ | ALREADY_PROMOTED | 04_RESEARCH/QUOTATIONS_2025.md | SHARED_ONEDRIVE | 2026-09-13 |
| QUOT-2026 | Quotations 2026 | quotations_index | [[04_RESEARCH/QUOTATIONS_2026]] | HIGH | 04_RESEARCH/QUOTATIONS_2026.md + MASTER_INDEX PANORAMA INGENIERIA 2026/ | ALREADY_PROMOTED | 04_RESEARCH/QUOTATIONS_2026.md | SHARED_ONEDRIVE | 2026-09-13 |
| ASSET-PAGINA-PANORAMA | Pagina Panorama Ingenieria (webapp) | webapp_company_asset | [[03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS]] | HIGH | MASTER_INDEX + 03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md (Activos digitales) | CLASSIFIED | 03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md | {PANORAMA_DRIVE}/Pagina_Panorama_Ingenieria/ (local) | 2026-09-13 |
| ASSET-PAGINA-VENTAS | PAGINA_VENTAS (webapp) | webapp_internal_commercial | [[03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS]] | HIGH | MASTER_INDEX + 03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md | CLASSIFIED | 03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md | {PANORAMA_DRIVE}/PAGINA_VENTAS/ (local) | 2026-09-13 |
| PROJ-N1N3-EXT | N1N3 Streetwear (promoted this turn) | project_external | (non-PANORAMA) | HIGH | 01_PROJECTS/N1N3_Streetwear/PROJECT.md (created in this commit) | PROMOTED | 01_PROJECTS/N1N3_Streetwear/PROJECT.md | External | 2026-09-13 |
| PROJECT-VISUALIZADOR-AFOROS | Visualizador_aforos | likely_trafficlab_visualizer | [[01_PROJECTS/TRAFFICLAB-CONTROL]] (likely) | NEEDS_RECONCILIATION | MASTER_INDEX line 77 + 90_INBOX/project_candidates/Visualizador_aforos.md | RECONCILE_WITH_TRAFFICLAB-CONTROL | TRAFFICLAB-CONTROL/INVENTORY.md | {PANORAMA_DRIVE}/Visualizador_aforos/ (local) | 2026-09-13 |
| PROJ-PAGINA-CEREBRA | Pagina_Cerebra | webapp_company_asset | (parent TBD) | MEDIUM | MASTER_INDEX line 75 + 90_INBOX/project_candidates/Pagina_Cerebra.md | KEEP_MEDIUM_UNTIL_EVIDENCE_IDENTIFIES_SCOPE | 90_INBOX/project_candidates/Pagina_Cerebra.md | {PANORAMA_DRIVE}/Pagina_Cerebra/ (local) | 2026-09-13 |
| FOLDER-DUPLICATE-01-PANORAMA | 01_PANORAMA_INGENIERIA/ (duplicate) | duplicate_company_folder | (duplicate) | LOW | MASTER_INDEX line 49 | INVENTORY_ONLY | n/a | SHARED_ONEDRIVE | 2026-09-13 |
| FOLDER-DUPLICATE-COTIZACION | cotizacion/ (duplicate) | duplicate_quotations_folder | (duplicate) | LOW | MASTER_INDEX line 54 | INVENTORY_ONLY | n/a | SHARED_ONEDRIVE | 2026-09-13 |
| PROJ-PMT-CYD-KR-52 | PMT CYD KR 52 A bahia/ | project_pmt_specific | (parent TBD) | MEDIUM | MASTER_INDEX line 60 | INVENTORY_ONLY | n/a | SHARED_ONEDRIVE | 2026-09-13 |
| PROJ-CICLO-ESPACIOS | Ciclo Espacios | project_vial_ciclovia | [[03_CLIENTS/CICLO_ESPACIOS]] (client note) | HIGH | 03_CLIENTS/CICLO_ESPACIOS.md | ALREADY_CLASSIFIED_AS_CLIENT_NOTE | 03_CLIENTS/CICLO_ESPACIOS.md | SHARED_ONEDRIVE | 2026-09-13 |
| PROJ-CLINICA-CASTELLANA | Clinica Castellana (PMT) | project_pmt | [[03_CLIENTS/CLINICA_CASTELLANA]] (client note) | HIGH | 03_CLIENTS/CLINICA_CASTELLANA.md | ALREADY_CLASSIFIED_AS_CLIENT_NOTE | 03_CLIENTS/CLINICA_CASTELLANA.md | SHARED_ONEDRIVE | 2026-09-13 |
| DEV-EVERYTHING-CLAUDE-CODE | {PANORAMA_DRIVE}/everything-claude-code/ | dev_tools_archive | (development tooling) | LOW | MASTER_INDEX line 78 | INVENTORY_ONLY | 98_ARCHIVE/ | {PANORAMA_DRIVE} (local) | 2026-09-13 |
| DEV-BACKUP-OPENCODE | {PANORAMA_DRIVE}/backup-opencode-config/ | dev_tools_backup | (development tooling) | LOW | MASTER_INDEX line 79 | INVENTORY_ONLY | 98_ARCHIVE/ | {PANORAMA_DRIVE} (local) | 2026-09-13 |
| FOLDER-TPD-DISENOS | TPD - DISEÑOS/ | engineering_plans | (client TPD) | LOW | MASTER_INDEX line 58 | INVENTORY_ONLY | n/a | SHARED_ONEDRIVE | 2026-09-13 |
| FOLDER-PROGRADO | PROYECTO DE GRADO/ | academic_project | (no parent) | LOW | MASTER_INDEX line 61 | INVENTORY_ONLY | n/a | SHARED_ONEDRIVE | 2026-09-13 |
| FOLDER-NUEVA-CARPETA-2025 | Nueva carpeta (2025)/ (empty) | empty_folder | (no parent) | HIGH | MASTER_INDEX + 06_INVENTORIES/Nueva_carpeta_2025_EMPTY.md | INVENTORY_ONLY | 06_INVENTORIES/Nueva_carpeta_2025_EMPTY.md | SHARED_ONEDRIVE | 2026-09-13 |
| DB-TRAFFICLAB | {TRAFFICLAB_DB_PHYSICAL} | sqlite_database | [[01_PROJECTS/TRAFFICLAB-CONTROL]][[06_INVENTORIES/trafficlab_db_POINTER]] | HIGH | 06_INVENTORIES/trafficlab_db_POINTER.md | ALREADY_PROMOTED | 06_INVENTORIES/trafficlab_db_POINTER.md | {PANORAMA_DRIVE}/data/ (local) | 2026-09-13 |
| WEBAPP-PAGINA-PANORAMA-DUPLICATE | Pagina Panorama Ingenieria (logical dup) | duplicate_logical_id | (same as ASSET-PAGINA-PANORAMA) | n/a | logical deduplication | DEDUPLICATED | n/a | n/a | 2026-09-13 |
| VAULT-TRAFICLABPRO2026 | traficlabpro2026 | obsidian_vault_active | [[01_PROJECTS/TRAFFICLAB-CONTROL]] | HIGH | MASTER_INDEX line 87 | ALREADY_INDEXED | OneDrive/PANORAMA INGENIERIA 2026/TraficLabPro/00_VAULT_OBSIDIAN | SHARED_ONEDRIVE | 2026-09-13 |
| VAULT-UNIFICADO-TRAFICLABPRO | Obsidian_Vault_Unificado/00_TraficLabPro_Vault | obsidian_vault_backup_sync | (possibly sync source) | MEDIUM | MASTER_INDEX line 88 | INVENTORY_ONLY | n/a | Documentos/Obsidian_Vault_Unificado/00_TraficLabPro_Vault | 2026-09-13 |
| VAULT-UNIFICADO-PERSONAL | Obsidian_Vault_Unificado/00_Personal_Vault | obsidian_vault_empty | (empty) | HIGH | MASTER_INDEX line 89 | INVENTORY_ONLY | n/a (empty) | Documentos/Obsidian_Vault_Unificado/00_Personal_Vault | 2026-09-13 |
| SERVICE-VISOR-2D-3D | Visor 2D/3D (port 8001) | web_service | [[01_PROJECTS/TRAFFICLAB-CONTROL]] | HIGH | MASTER_INDEX line 97 | INVENTORY_ONLY | n/a (port reference) | (server, TBD) | 2026-09-13 |
| SERVICE-BACKEND-FASTAPI | Backend FastAPI (port 8080) | web_service | [[01_PROJECTS/TRAFFICLAB-CONTROL]] | HIGH | MASTER_INDEX line 98 | INVENTORY_ONLY | n/a (port reference) | (server, TBD) | 2026-09-13 |
| SERVICE-PORT-2000 | Unknown service (port 2000) | web_service_down | (unknown) | MEDIUM | MASTER_INDEX line 99 (DOWN) | INVENTORY_ONLY | n/a (down) | (server, TBD) | 2026-09-13 |
| SERVER-ALMERIA | Server Almería (microsimulación Vissim) | remote_server | [[01_PROJECTS/IA-VISION]] | MEDIUM | MASTER_INDEX line 108 | INVENTORY_ONLY | n/a | {SERVER_ALMERIA_HOST}:{SERVER_ALMERIA_PORT} (remote) | 2026-09-13 |


---

## Reconciled counts (from this ledger)

```text
TOTAL_DISCOVERED_ENTITIES = 36
HIGH                    = 23
MEDIUM                  = 5
LOW                     = 6
NEEDS_RECONCILIATION    = 1
n/a (deduplicated)      = 1

# Sanity: HIGH + MEDIUM + LOW + NEEDS_RECONCILIATION + n/a must equal TOTAL
# 24 + 5 + 6 + 1 + 1 = 37 (should equal 37)
```

## Reconciliation note (per #2 comment 5650540171)

1. N1N3_Streetwear → HIGH (project_external, lightweight) — promoted to `01_PROJECTS/N1N3_Streetwear/PROJECT.md`
2. Pagina_Panorama_Ingenieria → HIGH (PANORAMA company digital asset) — classified in `03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS.md` (Activos digitales section)
3. PAGINA_VENTAS → HIGH (PANORAMA internal commercial/web system) — same parent as #2
4. Visualizador_aforos → NEEDS_RECONCILIATION (likely_trafficlab_visualizer) — destination: TRAFFICLAB-CONTROL/INVENTORY.md (when integration reconciled)
5. Pagina_Cerebra → MEDIUM (kept; awaits evidence to identify owner/scope)

## Mutations report

```text
Original sources: NOT MODIFIED (no moves/renames/deletes)
OneDrive: NOT rescanned (per protocol)
PR #25: NOT_AUTHORIZED (unchanged)
```

## See also

- [[06_INVENTORIES/MASTER_INDEX_ONEDRIVE_2026]]
- [[01_PROJECTS/IA-VISION]]
- [[01_PROJECTS/TRAFFICLAB-CONTROL]]
- [[01_PROJECTS/PANORAMA]]
- [[01_PROJECTS/N1N3_Streetwear]]
- [[03_CLIENTS/PANORAMA_INGENIERIA_Y_ARQUITECTOS_SAS]]
- [[90_INBOX/project_candidates/Pagina_Cerebra]]
