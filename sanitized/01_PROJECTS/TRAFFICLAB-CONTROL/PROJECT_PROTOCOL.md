# TRAFFICLAB-CONTROL — PROJECT_PROTOCOL

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:28:23Z
```

## Operating protocol

### Boundaries (NON-NEGOTIABLE)

- CANONICAL_DB_WRITE = NO
- SOURCE_VIDEO_WRITE = NO
- PRODUCTION_MUTATION = NO
- SUINI_WRITE = NO (until SUINI authorized separately)
- HISTORY_REWRITE = NO (no `git rebase` to rewrite history)
- DESTRUCTIVE_CLEANUP = NO (no `rm` on originals)

### Authorization gates

- Modifications to canonical DB: requires David micro-GO
- Modifications to source videos: requires David micro-GO
- Production mutations: requires David micro-GO
- New lanes / new repos: requires David micro-GO
- PR #25 merge: separately unauthorized
- Live bootstrap runs (Scene-Auto, M591, etc.): requires Astra exact-head re-audit PASS

### Evidence rule

Every meaningful change must produce evidence:
- Provenance header (DEVICE_ID, AGENT_ID, SESSION_ID, TIMESTAMP)
- Source/Target scope
- GIT_HEAD_BEFORE / GIT_HEAD_AFTER
- RESULT
- NO original files modified (only sidecars/provenance)

### PC-B handling

PC-B is BLOCKED_EXTERNAL_ACCESS until another physical host enrolls. PC-A work continues independently.

### See also

- `09_PROTOCOLS/` (parent repo) — global protocols
- `00_HOME/MISSION_CONTROL.md` — top-level router
- `99_SYSTEM/registry/devices/` — active device registry
