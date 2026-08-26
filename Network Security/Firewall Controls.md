# Firewall Controls

## Network Segmentation

pfSense will be used to control communication between the PrimeCore Minerals network segments. Each VLAN will use pfSense as its gateway so any traffic travelling between network segments can be inspected and controlled by firewall rules.

The firewall configuration will follow a least-privilege approach. Traffic will only be permitted where it is required, while unauthorised communication between network segments will be blocked. Important denied traffic will also be recorded to support security monitoring and validation.

## Network Design

| VLAN | Network | Purpose | Gateway |
|---|---|---|---|
| VLAN 10 | `192.168.10.0/24` | Employee LAN | `192.168.10.1` |
| VLAN 11 | `192.168.11.0/24` | Employee Wi-Fi | `192.168.11.1` |
| VLAN 20 | `192.168.20.0/24` | Visitor Network | `192.168.20.1` |
| VLAN 30 | `192.168.30.0/24` | Printer Network | `192.168.30.1` |
| VLAN 40 | `192.168.40.0/24` | Video Conferencing | `192.168.40.1` |
| VLAN 41 | `192.168.41.0/24` | CCTV Network | `192.168.41.1` |
| VLAN 50 | `192.168.50.0/24` | IoT Network | `192.168.50.1` |
| VLAN 90 | `192.168.90.0/24` | Server Network | `192.168.90.1` |
| VLAN 91 | `192.168.91.0/24` | Backup Network | `192.168.91.1` |
| VLAN 99 | `192.168.99.0/24` | Network Management | `192.168.99.1` |

## Implemented pfSense Network Aliases

The following aliases have been created in pfSense in preparation for the VLAN firewall configuration.

| Alias | Network | Status |
|---|---|---|
| `EMPLOYEE_LAN` | `192.168.10.0/24` | Implemented |
| `EMPLOYEE_WIFI` | `192.168.11.0/24` | Implemented |
| `VISITOR_NETWORK` | `192.168.20.0/24` | Implemented |
| `PRINTER_NETWORK` | `192.168.30.0/24` | Implemented |
| `VIDEO_NETWORK` | `192.168.40.0/24` | Implemented |
| `CCTV_NETWORK` | `192.168.41.0/24` | Implemented |
| `IOT_NETWORK` | `192.168.50.0/24` | Implemented |
| `SERVER_NETWORK` | `192.168.90.0/24` | Implemented |
| `BACKUP_NETWORK` | `192.168.91.0/24` | Implemented |
| `MANAGEMENT_NETWORK` | `192.168.99.0/24` | Implemented |

### Internal Networks Alias

The `INTERNAL_NETWORKS` alias has also been created. It groups the trusted and restricted PCM networks together so that firewall rules can reference them using a single alias.

The alias contains:

- `192.168.10.0/24` Employee LAN
- `192.168.11.0/24` Employee Wi-Fi
- `192.168.30.0/24` Printers
- `192.168.40.0/24` Video Conferencing
- `192.168.41.0/24` CCTV
- `192.168.50.0/24` IoT
- `192.168.90.0/24` Servers
- `192.168.91.0/24` Backup
- `192.168.99.0/24` Network Management

The Visitor network is intentionally excluded so that visitor traffic can be blocked from accessing internal PCM networks.

## Implemented Port Aliases

| Alias | Ports | Purpose | Status |
|---|---|---|---|
| `WEB_PORTS` | 80, 443 | HTTP and HTTPS | Implemented |
| `DNS_PORT` | 53 | DNS | Implemented |
| `MANAGEMENT_PORTS` | 22, 443 | SSH and HTTPS management | Implemented |

## Planned Firewall Rule Matrix

| Rule | Source | Destination | Service | Action | Logging |
|---|---|---|---|---|---|
| R01 | Visitor Network | Internet | HTTP/HTTPS/DNS | Allow | No |
| R02 | Employee LAN | Internet | Required Internet Traffic | Allow | No |
| R03 | Employee Wi-Fi | Internet | Required Internet Traffic | Allow | No |
| R04 | Visitor Network | Internal Networks | Any | Block | Enabled |
| R05 | Employee LAN | Management Network | Any | Block | Enabled |
| R06 | Employee Wi-Fi | Management Network | Any | Block | Enabled |
| R07 | Employee LAN | Server Network | Required Services | Allow | TBC |
| R08 | Employee Wi-Fi | Server Network | Required Services | Allow | TBC |
| R09 | Employee LAN / Wi-Fi | Printer Network | Required Printing Services | Allow | TBC |
| R10 | Management Network | Network Infrastructure | SSH/HTTPS | Allow | TBC |
| R11 | IoT Network | Internal Networks | Any not explicitly required | Block | Enabled |
| R12 | CCTV Network | Required Server Services | Required Services | Allow | TBC |
| R13 | Backup Network | Server Network | Backup/Replication Services | Allow | TBC |
| R14 | Video Network | Required Services / Internet | Video Conferencing Traffic | Allow | TBC |

## Planned pfSense Rules

### R01 - Visitor Internet Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R01 |
| Action | Pass |
| Interface | VLAN 20 - Visitor |
| Address Family | IPv4 |
| Protocol / Service | TCP/UDP as required |
| Source | `VISITOR_NETWORK` |
| Destination | Internet |
| Destination Port | `WEB_PORTS`, `DNS_PORT` |
| Logging | No |
| Description | Allow Visitor Internet Access |

Visitor traffic will first be blocked from `INTERNAL_NETWORKS` before permitted Internet services are allowed.

### R02 - Employee LAN Internet Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R02 |
| Action | Pass |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Source | `EMPLOYEE_LAN` |
| Destination | Internet |
| Destination Port | Required Services |
| Logging | TBC |
| Description | Allow Employee LAN Internet Access |

### R03 - Employee Wi-Fi Internet Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R03 |
| Action | Pass |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Source | `EMPLOYEE_WIFI` |
| Destination | Internet |
| Destination Port | Required Services |
| Logging | TBC |
| Description | Allow Employee Wi-Fi Internet Access |

### R04 - Block Visitor Access to Internal Networks

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R04 |
| Action | Block |
| Interface | VLAN 20 - Visitor |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `VISITOR_NETWORK` |
| Destination | `INTERNAL_NETWORKS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Visitor Access to Internal Networks |

`R04 BLOCK VISITOR_NETWORK -> INTERNAL_NETWORKS ANY`

This rule prevents visitors from accessing employee, server, printer, CCTV, IoT, backup and management networks.

### R05 - Block Employee LAN Access to Management

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R05 |
| Action | Block |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `EMPLOYEE_LAN` |
| Destination | `MANAGEMENT_NETWORK` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Employee LAN Access to Management |

### R06 - Block Employee Wi-Fi Access to Management

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R06 |
| Action | Block |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `EMPLOYEE_WIFI` |
| Destination | `MANAGEMENT_NETWORK` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Employee Wi-Fi Access to Management |

### R07 - Employee LAN Access to Servers

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R07 |
| Action | Pass |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `EMPLOYEE_LAN` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC - Required Services |
| Logging | TBC |
| Description | Allow Required Employee LAN Access to Servers |

### R08 - Employee Wi-Fi Access to Servers

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R08 |
| Action | Pass |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `EMPLOYEE_WIFI` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC - Required Services |
| Logging | TBC |
| Description | Allow Required Employee Wi-Fi Access to Servers |

### R09 - Employee Access to Printers

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R09 |
| Action | Pass |
| Interface | Employee LAN / Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `EMPLOYEE_LAN` / `EMPLOYEE_WIFI` |
| Destination | `PRINTER_NETWORK` |
| Destination Port | TBC - Required Printing Services |
| Logging | TBC |
| Description | Allow Employees to Access Network Printers |

### R10 - Management Access to Network Infrastructure

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R10 |
| Action | Pass |
| Interface | VLAN 99 - Network Management |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `MANAGEMENT_NETWORK` |
| Destination | Network Infrastructure |
| Destination Port | `MANAGEMENT_PORTS` |
| Logging | TBC |
| Description | Allow Management Access to Network Infrastructure |

### R11 - Restrict IoT Network

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R11 |
| Action | Block |
| Interface | VLAN 50 - IoT |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `IOT_NETWORK` |
| Destination | `INTERNAL_NETWORKS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Unauthorised IoT Access to Internal Networks |

Required IoT services will be explicitly permitted above this rule when those requirements are confirmed.

### R12 - CCTV Access to Required Server Services

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R12 |
| Action | Pass |
| Interface | VLAN 41 - CCTV |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `CCTV_NETWORK` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC |
| Logging | TBC |
| Description | Allow CCTV Traffic to Required Server Services |

### R13 - Backup Network Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R13 |
| Action | Pass |
| Interface | VLAN 91 - Backup |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `BACKUP_NETWORK` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC |
| Logging | TBC |
| Description | Allow Required Backup and Replication Traffic |

Bandwidth limits and lower QoS may later be applied to backup traffic during working hours.

### R14 - Video Conferencing Access

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R14 |
| Action | Pass |
| Interface | VLAN 40 - Video Conferencing |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `VIDEO_NETWORK` |
| Destination | Required Services / Internet |
| Destination Port | TBC |
| Logging | TBC |
| Description | Allow Video Conferencing Traffic |

Higher QoS may later be applied to video conferencing traffic to prioritise voice and video services.

## Current Implementation Status

