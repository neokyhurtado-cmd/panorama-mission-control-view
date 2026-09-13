# PANORAMA Mission Control

**Owner**: David Hurtado — PANORAMA INGENIERÍA Y ARQUITECTOS SAS
**Owner NIT**: 901384855-2 (legal entity; public registry)

Router central del ecosistema digital de David / PANORAMA.
Solo markdown/índices — archivos pesados quedan como punteros en OneDrive.

## Hosts

| Host | DEVICE_ID | Rol | Estado |
|------|-----------|-----|--------|
| PC-A (este) | `PANO-DEV-[REDACTED]` | Agente activo | OPERATIONAL |
| PC-B | (no enrolado) | — | BLOCKED_EXTERNAL_ACCESS |

Prior enrollment DEVICE_ID (from commit `b17a0c6`) is preserved as `prior_enrollment_unverified_alias` in `ENROLLMENT_LOG.md`. Not promoted to `SUPERSEDED` until local evidence confirms same physical machine.

## Contact

- **Company**: PANORAMA INGENIERÍA Y ARQUITECTOS SAS
- **NIT**: 901384855-2
- (personal email / phone intentionally NOT published per protocol)

## Estructura provisional (será reorganizada en commits siguientes)

- `clients/` — notas de clientes/proyectos (scaffold)
- `quotations/` — índices de cotizaciones por año (scaffold)
- `unknown/` — carpetas sin clasificar + punteros especiales
- `infrastructure/` — servers, DBs, servicios

Estructura canónica objetivo: 00_HOME / 01_PROJECTS / 02_COMPANY / 03_CLIENTS / 04_RESEARCH / 05_DECISIONS / 06_INVENTORIES / 07_EVIDENCE / 08_AGENTS / 09_PROTOCOLS / 90_INBOX / 98_ARCHIVE / 99_SYSTEM

(Generated 2026-09-13T02:22:43Z by Hermes orchestrator)
