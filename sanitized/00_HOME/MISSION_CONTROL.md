---
type: dashboard
title: PANORAMA - MISSION CONTROL
icon: gauge
status: LIVE
---

> [!abstract]+ PANORAMA — COMMAND VIEW
>
> **Active Projects** · ![[PROJECTS.base#KPI]]
>
> **Client Notes** · ![[CLIENTS.base#KPI]]
>
> **Items Need Attention** · ![[INBOX.base#KPI]]
>
> **Decisions Logged** · ![[DECISIONS.base#KPI]]
>
> **Quotations** · N/D
>
> ---
>
> **Mission Control** · **LIVE**&nbsp;&nbsp;|&nbsp;&nbsp;**Sync** · **PASS**&nbsp;&nbsp;|&nbsp;&nbsp;**Bases** · **CORE**&nbsp;&nbsp;|&nbsp;&nbsp;**Dataview** · **0**&nbsp;&nbsp;|&nbsp;&nbsp;**Canary** · [[09_PROTOCOLS/CANARY_IDENTITY_TEST|PASS ✅]]
>
> [!note] KPI Note
> Counts are calculated dynamically from the vault via Obsidian Bases `Filled` summary embedded as standalone blocks (not inside tables). Quotations = N/D until inventory is certified.

---

# PANORAMA - MISSION CONTROL

> [!success] LIVE
> **MISSION_CONTROL_LIVE = PASS**
> Certified sync path: **HERMES_PERSONAL <-> GitHub <-> HERMES_SERVER**.

> [!info] Durable truth
> The private Git vault is the durable authority. OneDrive is external/heavy corpus and is not the Mission Control vault authority.

## Executive summary

| Area | State | Open |
|---|---|---|
| Mission Control | LIVE | [[09_PROTOCOLS/CANARY_IDENTITY_TEST|Certified canary]] |
| Projects | READY | [[PROJECTS_INDEX|Projects]] |
| Clients | READY | [[CLIENTS_INDEX|Clients]] |
| Quotations | N/D | [[COTIZACIONES_INDEX|Quotations]] |
| Inbox / reconciliation | ATTENTION | [[90_INBOX/README|Inbox]] |
| Knowledge graph | READY | [[GRAPH_VIEW|Graph]] |
| Discovery | READY | [[07_EVIDENCE/DISCOVERY_LEDGER|Discovery Ledger]] |

## Quick access

| I want to see... | Open |
|---|---|
| Projects | [[PROJECTS_INDEX]] |
| Clients | [[CLIENTS_INDEX]] |
| Quotations | [[COTIZACIONES_INDEX]] |
| Pending / Inbox | [[90_INBOX/README]] |
| Evidence | [[07_EVIDENCE/README]] |
| Decisions | [[05_DECISIONS/README]] |
| Research | [[04_RESEARCH/README]] |
| Knowledge graph | [[GRAPH_VIEW]] |
| System | [[99_SYSTEM/README]] |

---

## Requires attention

> [!warning] Operational inbox
> These items require classification, reconciliation or promotion. Original source files are not moved or deleted.

![[INBOX.base#Pendientes]]

---

## Strategic projects

![[PROJECTS.base#Tarjetas]]

> [[PROJECTS_INDEX|Open project center]] - [[PROJECTS.base#Tabla|Open table]]

---

## Clients

![[CLIENTS.base#Tarjetas]]

> [[CLIENTS_INDEX|Open technical CRM]] - [[CLIENTS.base#Tabla|Open table]]

---

## Quotations

> [!warning] Data status
> The current quotation inventory is a scaffold/pointer, not a certified exhaustive count. Totals should only appear after normalization by client, project and year.

![[QUOTATIONS.base#Indice]]

> [[COTIZACIONES_INDEX|Open quotation center]]

---

## Recent decisions

![[DECISIONS.base]]

> [[05_DECISIONS/README|Open decisions register]]

---

## Recent activity

![[ACTIVITY.base#Ultimos 14 dias]]

---

## Knowledge network

Mission Control connects **Project <-> Client <-> Year <-> Document <-> Decision <-> Evidence <-> Repo <-> Agent/Source** through properties, wikilinks and backlinks.

> [!tip] Open the network
> Use [[GRAPH_VIEW|Knowledge Graph]] or Obsidian **Graph View** to navigate real relationships.

---

## System health

| Gate | State |
|---|---|
| Mission Control Live | PASS |
| Two distinct host identities | PASS |
| GitHub roundtrip | PASS |
| Pre-open launcher | CANONICAL |
| Sync false-success | FAIL-CLOSED |
| Dataview runtime | 0 |
| Bases | Obsidian Core |
| OneDrive as vault authority | NO |
| External originals modified by discovery | NO |

Evidence: [[09_PROTOCOLS/CANARY_IDENTITY_TEST|identity canary]] - [[09_PROTOCOLS/CANARY_PURPOSE_TEST|transport canary]] - [[07_EVIDENCE/DISCOVERY_LEDGER|discovery ledger]].

---

## Work queue for Hermes

1. Classify/reconcile everything that appears in Inbox.
2. Enrich client <-> project relationships using durable evidence.
3. Complete the quotation inventory without inventing counts.
4. Register new decisions and evidence in canonical folders.
5. Keep this page as a **view**, never as a second source of truth.

---

> [!abstract] Operating rule
> **David decides. Mission Control preserves state. Hermes executes and updates evidence. GitHub synchronizes both hosts.**
