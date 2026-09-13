# ENROLLMENT LOG

PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T02:18:35Z

## Enrollment history (chronological)

### 1. PRIOR (preserved, not overwritten)
- DEVICE_ID: `97194b01-3619-46d5-ac57-89398605c839`
- Source: existing README.md in this repo (commit `b17a0c6 Bootstrap: índices markdown + DEVICE_ID PC-A`)
- Status: SUPERSEDED (not modified)
- Alias: `prior_enrollment_unverified_alias` (preserved per protocol)

### 2. CURRENT (this device)
- DEVICE_ID: `PANO-DEV-[REDACTED]`  ← active
- AGENT_ID: `PANO-AGENT-hermes-orchestrator-20E6CD0DC220`  (stable across sessions on same profile)
- SESSION_ID: `PANO-SES-[REDACTED]`  (rotates per execution)
- Source: Hermes orchestrator profile on Windows (PC-A)
- Created: 2026-09-13 (~02:11 UTC)
- Method: `uuid.uuid4()` — Python native UUIDv4 (RFC 4122)
- Persistence: `C:/Users/david/AppData/Local/hermes/identity/device.json`

## Conflict resolution

Per protocol DEVICE_IDENTITY_PROTOCOL.md:
- Same DEVICE_ID on two physical machines = conflict, one must re-enroll
- Different DEVICE_IDs both claiming "PC-A" = previous enrollment + this new enrollment

**Resolution:**
- PRIOR_DEVICE_ID_FROM_REPO is preserved (not erased) as `prior_enrollment_unverified_alias`
- CURRENT DEVICE_ID takes the active slot
- README will be updated to reference the supersede trail (next commit)
- All sidecars include `DEVICE_ID_REENROLL` block preserving the previous ID

## Identity persistence

DEVICE_ID survives restart (file at `C:/Users/david/AppData/Local/hermes/identity/device.json`)
AGENT_ID stable (sha256 of profile path truncated 12)
SESSION_ID rotates per execution


## Hardware identifier policy

Per protocol DEVICE_IDENTITY_PROTOCOL.md:
- DO NOT use MAC address, disk serial, Windows ID, host username, or any hardware-derivative
- DEVICE_ID must be cryptographically random (UUIDv4) and persist on disk
- AGENT_ID must be stable across sessions (hash of profile path is OK — that's software, not hardware)
- Any prior enrollment with hardware identifiers in README/history is NON-COMPLIANT

This enrollment log preserves traceability but does NOT include any hardware identifiers in active files.
Prior commit `b17a0c6` contained identifiers in README.md that are now flagged NON-COMPLIANT.
Those identifiers remain in git history only (private history). No rewrite performed.
