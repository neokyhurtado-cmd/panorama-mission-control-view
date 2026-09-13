# HERMES_PERSONAL — Awaiting Enrollment

```text
PROVENANCE:
  DEVICE_ID: (not yet enrolled)
  AGENT_ID: (not yet enrolled)
  STATUS: PLACEHOLDER — awaiting second host enrollment
  TIMESTAMP_UTC: 2026-09-13T02:51:25Z
```

## Status

This is a placeholder entry for HERMES_PERSONAL (the second host in the new topology per comment 5650384358).

## Topology context

```text
HERMES_PERSONAL  <->  GitHub private (panorama-mission-control)  <->  HERMES_SERVER
                              |
                       OneDrive (shared external corpus)
```

## Enrollment requirements

When HERMES_PERSONAL host is accessible:
1. Run `hermes gateway start` (or equivalent) on that host
2. Generate DEVICE_ID via `uuid.uuid4()` — do NOT use hardware identifiers
3. Persist identity at `{HERMES_IDENTITY_DIR}/device.json`
4. Register here as `PANO-DEV-<UUIDv4>.md` file with same schema as HERMES_SERVER

## See also

- `99_SYSTEM/registry/SERVERS.md` — physical→logical mapping
- `99_SYSTEM/registry/agents/PANO-AGENT-hermes-orchestrator-20E6CD0DC220.md` — current active agent (on HERMES_SERVER)
