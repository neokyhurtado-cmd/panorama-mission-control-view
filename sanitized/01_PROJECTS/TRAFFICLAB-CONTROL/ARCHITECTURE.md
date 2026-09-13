# TRAFFICLAB-CONTROL — ARCHITECTURE

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:28:23Z
```

## Components

(To be populated as project matures.)

## Data flow

(To be populated.)

## Boundaries

- CANONICAL_DB_WRITE = NO (read-only on canonical DB)
- SOURCE_VIDEO_WRITE = NO (read-only on source videos)
- PRODUCTION_MUTATION = NO (no runtime mutations)
- SUINI_WRITE = NO (until SUINI project authorized)

## See also

- `PROJECT.md`
- `STATE_POINTERS.md`
- `DECISIONS.md`
- `PROJECT_PROTOCOL.md`
