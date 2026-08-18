# Firewall Controls

## Network Segmentation

The firewall rule configuration will manage all communications between the Employee, Visitor and Management networks by controlling which traffic is allowed and which traffic is blocked. This prevents unauthorised users accessing restricted areas while allowing users that are approved. 

## Planned Network Aliases

| Alias | Planned Network |
|---|---|
| `EMPLOYEE_VLAN` | `192.168.1.0/24` |
| `VISITOR_VLAN` | `192.168.2.0/24` |
| `MANAGEMENT_VLAN` | `192.168.99.0/24` |
| `INTERNAL_SYSTEMS` | TBC |
| `NETWORK_INFRASTRUCTURE` | TBC |
| `SYSTEM_LOGS` | TBC |

## Firewall Rule Matrix

| Rule | Source | Destination | Service | Action |
|---|---|---|---|---|
| R01 | Visitor | Internet | HTTP/HTTPS/DNS | Allow |
| R02 | Employee | Internet | HTTP/HTTPS/DNS | Allow |
| R03 | Visitor | Employee | Any | Block |
| R04 | Visitor | Management | Any | Block |
| R05 | Visitor | Internal Systems | Any | Block |
| R06 | Employee | Management | Any | Block |
| R07 | Employee | Internal Systems | Required Services | Allow |
| R08 | Management | Network Infrastructure | SSH/HTTPS | Allow |
| R09 | Network Infrastructure | System Logs | Syslog | Allow |

## Planned pfSense Rules

### R01 - Visitor Internet Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R01 |
| Action | Pass |
| Interface | Visitor VLAN |
| Address Family | IPv4 |
| Protocol / Service | HTTP / HTTPS / DNS |
| Source | `VISITOR_VLAN` |
| Destination | Internet |
| Destination Port | HTTP / HTTPS / DNS |
| Logging | TBC |
| Description | Allow Visitor Internet Access |

`R01 PASS VISITOR_VLAN -> INTERNET HTTP/HTTPS/DNS`

### R02 - Employee Internet Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R02 |
| Action | Pass |
| Interface | Employee VLAN |
| Address Family | IPv4 |
| Protocol / Service | HTTP / HTTPS / DNS |
| Source | `EMPLOYEE_VLAN` |
| Destination | Internet |
| Destination Port | HTTP / HTTPS / DNS |
| Logging | TBC |
| Description | Allow Employee Internet Access |

`R02 PASS EMPLOYEE_VLAN -> INTERNET HTTP/HTTPS/DNS`

### R03 - Block Visitor to Employee

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R03 |
| Action | Block |
| Interface | Visitor VLAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `VISITOR_VLAN` |
| Destination | `EMPLOYEE_VLAN` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Visitor to Employee |

`R03 BLOCK VISITOR_VLAN -> EMPLOYEE_VLAN ANY`

### R04 - Block Visitor to Management

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R04 |
| Action | Block |
| Interface | Visitor VLAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `VISITOR_VLAN` |
| Destination | `MANAGEMENT_VLAN` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Visitor to Management |

`R04 BLOCK VISITOR_VLAN -> MANAGEMENT_VLAN ANY`

### R05 - Block Visitor to Internal Systems

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R05 |
| Action | Block |
| Interface | Visitor VLAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `VISITOR_VLAN` |
| Destination | `INTERNAL_SYSTEMS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Visitor to Internal Systems |

`R05 BLOCK VISITOR_VLAN -> INTERNAL_SYSTEMS ANY`

### R06 - Block Employee to Management

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R06 |
| Action | Block |
| Interface | Employee VLAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `EMPLOYEE_VLAN` |
| Destination | `MANAGEMENT_VLAN` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Employee to Management |

`R06 BLOCK EMPLOYEE_VLAN -> MANAGEMENT_VLAN ANY`

### R07 - Employee Access to Internal Systems

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R07 |
| Action | Pass |
| Interface | Employee VLAN |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `EMPLOYEE_VLAN` |
| Destination | `INTERNAL_SYSTEMS` |
| Destination Port | TBC |
| Logging | TBC |
| Description | Allow Employee to Internal Systems |

`R07 PASS EMPLOYEE_VLAN -> INTERNAL_SYSTEMS TBC`

### R08 - Management Access to Network Infrastructure

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R08 |
| Action | Pass |
| Interface | Management VLAN |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `MANAGEMENT_VLAN` |
| Destination | `NETWORK_INFRASTRUCTURE` |
| Destination Port | SSH / HTTPS |
| Logging | TBC |
| Description | Allow Management to Network Infrastructure |

`R08 PASS MANAGEMENT_VLAN -> NETWORK_INFRASTRUCTURE SSH/HTTPS`

### R09 - Network Infrastructure to System Logs

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R09 |
| Action | Pass |
| Interface | TBC |
| Address Family | IPv4 |
| Protocol | TBC - Syslog |
| Source | `NETWORK_INFRASTRUCTURE` |
| Destination | `SYSTEM_LOGS` |
| Destination Port | TBC - Syslog |
| Logging | TBC |
| Description | Allow Network Infrastructure to System Logs |

`R09 PASS NETWORK_INFRASTRUCTURE -> SYSTEM_LOGS SYSLOG`
