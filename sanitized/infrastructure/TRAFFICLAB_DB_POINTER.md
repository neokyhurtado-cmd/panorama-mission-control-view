# TRAFFICLAB_DB POINTER

PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:15:47Z
  RESULT: trafficlab_db_pointer_only
  PC_B: BLOCKED_EXTERNAL_ACCESS

## Pointer (NO copy per protocol — originals must be preserved)

```
X:/TraficLabPro/data/trafficlab.db
SHA256: (TO BE VERIFIED at next step; do not hash without explicit authorization)
SIZE:   (TO BE VERIFIED)
ROLE:   canonical database (READ-ONLY per #79 frozen boundaries)
```

Per protocol rule "no copiar corpus pesados por defecto; usar punteros":
- This file IS a pointer, not a copy
- DB file remains at its canonical path
- Any future reference to trafficlab.db should resolve via this pointer, not duplicate the file

## Pending

- Verify db exists at canonical path (read-only check, no access modification)
- Hash for provenance if authorization granted (NOT done now — wait for explicit authorization)
- Record canonical_db_sha256 in this pointer file (when authorized)

ORIGINALS_MODIFIED = 0
CANONICAL_DB_WRITE = NO
SOURCE_VIDEO_WRITE = NO
