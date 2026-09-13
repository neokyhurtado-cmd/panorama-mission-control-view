# SUINI — DECISIONS

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:28:23Z
```

## Decision log

| Date | Decision | Rationale | Reversible? |
|------|----------|-----------|-------------|
| 2026-09-11 | Telegram = normal Hermes session transport (no special agent) | Per Astra directive #5643285255 | YES |
| 2026-09-12 | TRANSPORT_OWNER_SAFETY_V1: 1 owner / many sessions, 2nd poller = PROHIBITED | Per Astra incident #5644048913 | YES |
| 2026-09-12 | Telegram gateway fix: removed --replace from service + code source | Per gateway crash-loop diagnosis | PARTIAL |

## Pending decisions

(none recorded — see OPEN_QUESTIONS.md for open items requiring decisions)
