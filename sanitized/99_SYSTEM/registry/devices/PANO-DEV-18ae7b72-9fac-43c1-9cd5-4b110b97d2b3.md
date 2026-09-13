# Device Registration

```text
DEVICE_ID: [REDACTED]
AGENT_ID: [REDACTED]
ROLE: HERMES_SERVER
TOPOLOGY_ROLE: one of two hosts (HERMES_PERSONAL <-> GitHub private repo <-> HERMES_SERVER + OneDrive external corpus)
ENROLLED_AT: 2026-09-13T02:22:43Z
METHOD: uuid.uuid4() — Python native UUIDv4 (RFC 4122)
PERSISTENCE: {HERMES_IDENTITY_DIR}/device.json
STATUS: OPERATIONAL
```

## Enrollment history

| Timestamp | Event | Note |
|-----------|-------|------|
| 2026-09-13T02:11Z | First enrollment (PANO-DEV-FFF308922F1D) | NOT UUIDv4 — superseded |
| 2026-09-13T02:11Z | Re-enrollment (PANO-DEV-18ae7b72...) | UUIDv4 RFC 4122 ✓ |
| 2026-09-13T02:11Z | Session rotated (PANO-SES-5c959bac...) | UUIDv4 RFC 4122 ✓ |
| 2026-09-13T~02:48Z | Topology migration | PC-A → HERMES_SERVER (per panorama-mission-control#2 / 5650384358) |
| 2026-09-13T~02:48Z | HERMES_PERSONAL placeholder | Awaiting enrollment from second host |

## Topology (canonical)

```text
HERMES_PERSONAL  <->  GitHub private (panorama-mission-control)  <->  HERMES_SERVER
                              |
                       OneDrive (shared external corpus)
```

PC-A / PC-B terminology is obsolete as of 2026-09-13 (per comment 5650384358).
