# Servers Registry

```text
PROVENANCE:
  DEVICE_ID: [REDACTED]
  AGENT_ID: [REDACTED]
  SESSION_ID: [REDACTED]
  TIMESTAMP_UTC: 2026-09-13T03:30Z
```

## Logical ID Mappings

| Logical ID | Type | Physical Ref | Access |
|-----------|------|--------------|--------|
| `{SERVER_WIN_AXIA_PANORAMA}` | Windows server (UNC share) | `\WIN-01-AXIA-PANORAMA\C$\PANORAMA\` | Requires network auth |
| `{SERVER_ALMERIA}` | Linux work server | `[IP_REDACTED]` | SSH/HTTP on port 8765 |
| `{TRAFFICLAB_DB_PHYSICAL}` | SQLite DB file | `\WIN-01-AXIA-PANORAMA\C$\PANORAMA\0. data\` | Via UNC share |

## Active Servers

### {SERVER_ALMERIA}
- **IP**: [IP_REDACTED]
- **Port**: 8765 (Almeria service)
- **Type**: Linux remote work server
- **Purpose**: CI/CD, scripting, web services
- **Repo served**: traficlab-factory, suini, IA-VISION

### {SERVER_WIN_AXIA_PANORAMA}
- **Type**: Windows server with shared drives
- **UNC base**: `\WIN-01-AXIA-PANORAMA\C$\`
- **Share**: `PANORAMA\` (project files, DBs)
- **Purpose**: Central file storage for TraficLabPro, project files

