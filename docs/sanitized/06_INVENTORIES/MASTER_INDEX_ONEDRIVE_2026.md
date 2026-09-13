
# PROVENANCE
```
DEVICE_ID: [REDACTED]
AGENT_ID: [REDACTED]
SESSION_ID: [REDACTED]
TIMESTAMP_UTC: 2026-09-13T03:00Z
SOURCE: Obsidian CLI scan (PC-A local filesystem)
TARGET: panorama-mission-control (private repo)
```

# LOCAL-PATH HYGIENE PASS — see 99_SYSTEM/registry/SERVERS.md for logical IDs

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:39:29Z
  RESULT: local-path hygiene pass — physical paths replaced with logical IDs (see 99_SYSTEM/registry/SERVERS.md)
```

---


# MASTER INDEX — PANORAMA + ONEDRIVE 2026
**Generado**: 2026-09-12  
**Por**: Hermes CLI  
**Propósito**: Router central de TODO el ecosistema digital de David / PANORAMA

---

## BÓVEDA PRINCIPAL (Obsidian —fuente de verdad-)
- **Vault**: `traficlabpro2026` → `OneDrive/PANORAMA INGENIERIA 2026/TraficLabPro/00_VAULT_OBSIDIAN`
- **Archivos**: 120,940 | **Tamaño**: 5.7 GB | **Carpetas**: 842
- **CLI**: `/c/Users/[REDACTED] --vault=traficlabpro2026`
- **Entry point local**: `[[00_Indice/MASTER_INDEX]]` (sprint 273 carpetas en `40_Actas/`)

---

## ONEDRIVE — Vista de carpetas raíz

| Carpeta | Contenido |
|---------|-----------|
| `PANORAMA INGENIERIA 2026/` | Proyecto activo — TraficLabPro, cotizaciones, planos récord |
| `PANORAMA INGENIERIA 2025/` | Proyectos 2025 — CTIC, FERREIRA, MUTIS, COLPATRIA, etc |
| `PANORAMA INGENIERIA 2024/` | Proyectos 2024 — PESV, PMT varios, OCTAVIO MILLÁN |
| `PANORAMA INGENIERIA 2022/` | Proyectos 2022 — Grupos 5 y 8, USME, CTIC |
| `01_PANORAMA_INGENIERIA/` | otra copia? |
| `ADMINISTRACION_PANORAMA_INGENIERIA/` | Admin, contabilidad |
| `Documentos/` | Notas sueltas, scripts Python, CSV ropa N1N3, `Obsidian_Vault_Unificado/` |
| `Vaults/` | Visores HTML (aforos, mapas) — NO es bóveda Obsidian |
| `COTIZACIONES/` | Plantillas, cotizaciones activas |
| `cotizacion/` | otra carpeta de cotizaciones |
| `CONTRATOS IDU/` | Contratos IDU |
| `ASYDU/` | Contratos ASYDU |
| `Buga/`, `Neiva 006 Ash/`, `Piendamo/` | Proyectos por ciudad |
| `TPD - DISEÑOS/` | Planos TPD |
| `TRAFING 2022/` | Datos de tráfico 2022 |
| `PMT CYD KR 52 A bahia/` | Un PMT específico |
| `PROYECTO DE GRADO/` | Tesis/proyecto de grado |

---

## OTROS DISCOS — {SERVER_WIN_AXIA_PANORAMA} (UNC share — see 99_SYSTEM/registry/servers.md)

> ⚠️ Estos paths son UNC de red, no locales. El servidor {SERVER_WIN_AXIA_PANORAMA} debe estar activo para acceder.

| Path | Contenido |
|------|-----------|
| `{PANORAMA_DRIVE}/TraficLabPro/` | Proyecto TraficLabPro canónico (~121 items) |
| `{PANORAMA_DRIVE}/TraficLabPro_visor_componente_Copy/` | La copia más grande (~641 items, con cvat_repo, modelos) |
| `{PANORAMA_DRIVE}/data/` | `trafficlab.db` ✅ + `refiner_pro/` |
| `{PANORAMA_DRIVE}/Pagina_Panorama_Ingenieria/` | Web app Next.js empresa |
| `{PANORAMA_DRIVE}/Pagina_Cerebra/` | Web app Cerebra |
| `{PANORAMA_DRIVE}/PAGINA_VENTAS/` | Web app ventas |
| `{PANORAMA_DRIVE}/Visualizador_aforos/` | Proyecto paralelo (~889 MB) |
| `{PANORAMA_DRIVE}/everything-claude-code/` | 70 items, repos skills+rules |
| `{PANORAMA_DRIVE}/backup-opencode-config/` | 13 SKILL.md backup |

---

## BÓVEDAS OBSIDIAN (inventario)

| Nombre | Path | Estado |
|--------|------|--------|
| `traficlabpro2026` | `OneDrive/.../00_VAULT_OBSIDIAN` | ✅ ACTIVA |
| `Obsidian_Vault_Unificado/00_TraficLabPro_Vault` | `Documentos/Obsidian_Vault_Unificado/00_TraficLabPro_Vault` | 📦 Backup/sincronización |
| `Obsidian_Vault_Unificado/00_Personal_Vault` | `Documentos/Obsidian_Vault_Unificado/00_Personal_Vault` | 📦 Vacío |

---

## SERVIDORES VIVOS (verificados en MASTER_INDEX)

| Puerto | Servicio | Estado |
|--------|----------|--------|
| `:8001` | Visor 2D/3D | OK |
| `:8080` | Backend FastAPI | OK |
| `:2000` | ? | DOWN |

---

## PROYECTOS ACTIVOS CONOCIDOS

### TraficLabPro (IA-VISION)
- `traficlab-factory` repo público
- `suini` repo — microsimulación Vissim
- Servidor Almería: `{SERVER_ALMERIA_HOST}:{SERVER_ALMERIA_PORT}`
- WO activo: IA-VISION #94 (NVDEC real + C2 pipeline)

### N1N3 Streetwear
- **Live**: https://n1n3-store.vercel.app
- **Repo**: `n1n3-store/`
- **GH**: neokyhurtado-cmds-projects

### PANORAMA INGENIERÍA
- **NIT**: 901384855-2
- **Docs**: cotizaciones, PMT, Planos Récord, Señalización, Semáforos, PESV
- **Clientes frecuentes**: Ing Wilson Bravo, COLPATRIA, FERREIRA, CONCOCRETO, CTIC/IDU, ALIADA, MUTIS, OCTAVIO MILLÁN

---

## ACCIONES PENDIENTES

- [ ] Integrar `C:\PANORAMA	rafficlab.db` al pipeline actual
- [ ] Unificar `Obsidian_Vault_Unificado` con bóveda principal (si hay delta)
- [ ] Indexar carpetas 2022-2024 en Obsidian (hay proyectos sin linking)
- [ ] Consolidar cotizaciones en plantilla única

---
*Actualizado: 2026-09-12 por Hermes CLI*
