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

## The alias

- `192.168.10.0/24` Employee LAN
- `192.168.11.0/24` Employee Wi-Fi
- `192.168.30.0/24` Printers
- `192.168.40.0/24` Video Conferencing
- `192.168.41.0/24` CCTV
- `192.168.50.0/24` IoT
- `192.168.90.0/24` Servers
- `192.168.91.0/24` Backup
- `192.168.99.0/24` Network Management

The Visitor network `192.168.20.0` is intentionally excluded so that visitor traffic can be blocked from accessing internal PCM networks.

## Implemented Port Aliases

| Alias | Ports | Purpose | Status |
|---|---|---|---|
| `WEB_PORTS` | 80, 443 | HTTP and HTTPS | Implemented |
| `DNS_PORT` | 53 | DNS | Implemented |
| `MANAGEMENT_PORTS` | 22, 443 | SSH and HTTPS management | Implemented |
| `PRINT_PORTS` | 631, 9100, 515 | IPP, RAW/JetDirect and LPD/LPR printing | Implemented |

## Firewall Rule Matrix

| Rule | Source | Destination | Service | Action | Logging | Status |
|---|---|---|---|---|---|---|
| R01a | Visitor Network | Internet | HTTP/HTTPS (`WEB_PORTS`) | Allow | No | Implemented and Tested |
| R01b | Visitor Network | Internet | DNS (`DNS_PORT`) | Allow | No | Implemented and Tested |
| R02a | Employee LAN | Internet | HTTP/HTTPS (`WEB_PORTS`) | Allow | No | Implemented and Tested |
| R02b | Employee LAN | Internet | DNS (`DNS_PORT`) | Allow | No | Implemented and Tested |
| R03a | Employee Wi-Fi | Internet | HTTP/HTTPS (`WEB_PORTS`) | Allow | No | Implemented, Not Yet Tested |
| R03b | Employee Wi-Fi | Internet | DNS (`DNS_PORT`) | Allow | No | Implemented, Not Yet Tested |
| R04 | Visitor Network | Internal Networks | Any | Block | Enabled | Implemented and Tested |
| R05 | Employee LAN | Management Network | Any | Block | Enabled | Implemented and Tested |
| R06 | Employee Wi-Fi | Management Network | Any | Block | Enabled | Implemented, Not Yet Tested |
| R07 | Employee LAN | Server Network | Required Services | Allow | TBC | Planned |
| R08 | Employee Wi-Fi | Server Network | Required Services | Allow | TBC | Planned |
| R09a | Employee LAN | Printer Network | `PRINT_PORTS` | Allow | No | Implemented, Not Yet Tested |
| R09b | Employee Wi-Fi | Printer Network | `PRINT_PORTS` | Allow | No | Implemented, Not Yet Tested |
| R10 | Management Network | Network Infrastructure | `MANAGEMENT_PORTS` | Allow | TBC | Planned |
| R11 | IoT Network | Internal Networks | Any | Block | Enabled | Implemented, Not Yet Tested |
| R12a | CCTV Network | Server Network | Required Services | Allow | TBC | Planned |
| R12b | CCTV Network | Internal Networks | Any unauthorised traffic | Block | Enabled | Implemented, Not Yet Tested |
| R13a | Backup Network | Server Network | Backup/Replication Services | Allow | TBC | Planned |
| R13b | Backup Network | Any | Any unauthorised traffic | Block | Enabled | Implemented, Not Yet Tested |
| R14 | Video Network | Required Services / Internet | Video Conferencing Traffic | Allow | TBC | Planned |

## pfSense Firewall Rules

### R01a - Visitor Web Access

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R01a |
| Action | Pass |
| Interface | VLAN 20 - Visitor |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `VISITOR_VLAN subnets` |
| Destination | Any |
| Destination Port | `WEB_PORTS` |
| Logging | No |
| Description | Allow Visitor Web Access |

This rule permits HTTP and HTTPS traffic from the Visitor network. HTTP and HTTPS connectivity was successfully tested from VisitorLinux using ports 80 and 443.

---

### R01b - Visitor DNS Access

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R01b |
| Action | Pass |
| Interface | VLAN 20 - Visitor |
| Address Family | IPv4 |
| Protocol | TCP/UDP |
| Source | `VISITOR_VLAN subnets` |
| Destination | Any |
| Destination Port | `DNS_PORT` |
| Logging | No |
| Description | Allow Visitor DNS |

DNS resolution was successfully tested from the Visitor network.

---

### R02a - Employee LAN Web Access

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R02a |
| Action | Pass |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `EMPLOYEE_VLAN subnets` |
| Destination | Any |
| Destination Port | `WEB_PORTS` |
| Logging | No |
| Description | Allow Employee Web Access |

HTTP and HTTPS connectivity was successfully tested from EmployeeLinux using ports 80 and 443.

---

### R02b - Employee LAN DNS Access

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R02b |
| Action | Pass |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | TCP/UDP |
| Source | `EMPLOYEE_VLAN subnets` |
| Destination | Any |
| Destination Port | `DNS_PORT` |
| Logging | No |
| Description | Allow Employee DNS |

DNS resolution was successfully tested from the Employee LAN.

---

### R03a - Employee Wi-Fi Web Access

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R03a |
| Action | Pass |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `EMPLOYEE_WIFI_VLAN subnets` |
| Destination | Any |
| Destination Port | `WEB_PORTS` |
| Logging | No |
| Description | Allow Employee WiFi Web Access |

---

### R03b - Employee Wi-Fi DNS Access

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R03b |
| Action | Pass |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | TCP/UDP |
| Source | `EMPLOYEE_WIFI_VLAN subnets` |
| Destination | Any |
| Destination Port | `DNS_PORT` |
| Logging | No |
| Description | Allow Employee WiFi DNS |

---

### R04 - Block Visitor Access to Internal Networks

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R04 |
| Action | Block |
| Interface | VLAN 20 - Visitor |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `VISITOR_VLAN subnets` |
| Destination | `INTERNAL_NETWORKS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Visitor Access to Internal Networks |

`R04 BLOCK VISITOR_VLAN -> INTERNAL_NETWORKS ANY`

This rule prevents Visitor devices from accessing the Employee, Employee Wi-Fi, Printer, Video Conferencing, CCTV, IoT, Server, Backup and Management networks.

Testing confirmed that Visitor traffic to Employee, Management and Server networks was blocked. The denied connections were also recorded in the pfSense firewall logs.

---

### R05 - Block Employee LAN Access to Management

**Status:** Implemented and Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R05 |
| Action | Block |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `EMPLOYEE_VLAN subnets` |
| Destination | `MANAGEMENT_NETWORK` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Employee Access to Management |

Testing from `192.168.10.71` to the Management gateway `192.168.99.1` timed out as expected. pfSense recorded the denied traffic against the R05 rule.

---

### R06 - Block Employee Wi-Fi Access to Management

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R06 |
| Action | Block |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `EMPLOYEE_WIFI_VLAN subnets` |
| Destination | `MANAGEMENT_NETWORK` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Employee WiFi Access to Management |

---

### R07 - Employee LAN Access to Servers

**Status:** Planned

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

The required server services have not yet been confirmed, so this rule will remain restricted until the necessary ports are identified.

---

### R08 - Employee Wi-Fi Access to Servers

**Status:** Planned

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

The required server services have not yet been confirmed.

---

### R09a - Employee LAN Access to Printers

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R09a |
| Action | Pass |
| Interface | VLAN 10 - Employee LAN |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `EMPLOYEE_VLAN subnets` |
| Destination | `PRINTER_NETWORK` |
| Destination Port | `PRINT_PORTS` |
| Logging | No |
| Description | Allow Employee LAN to Printers |

The `PRINT_PORTS` alias contains the required common network printing services.

---

### R09b - Employee Wi-Fi Access to Printers

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R09b |
| Action | Pass |
| Interface | VLAN 11 - Employee Wi-Fi |
| Address Family | IPv4 |
| Protocol | TCP |
| Source | `EMPLOYEE_WIFI_VLAN subnets` |
| Destination | `PRINTER_NETWORK` |
| Destination Port | `PRINT_PORTS` |
| Logging | No |
| Description | Allow Employee WiFi to Printers |

---

### R10 - Management Access to Network Infrastructure

**Status:** Planned

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

The final infrastructure addresses will be added once the routers, switches and access points used by the project are confirmed.

---

### R11 - Restrict IoT Network

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R11 |
| Action | Block |
| Interface | VLAN 50 - IoT |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `IOT_VLAN subnets` |
| Destination | `INTERNAL_NETWORKS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block IoT Access to Internal Networks |

This rule prevents IoT devices from initiating unauthorised communication with internal PCM networks. Specific required services can later be permitted above this rule if necessary.

---

### R12a - CCTV Access to Required Server Services

**Status:** Planned

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R12a |
| Action | Pass |
| Interface | VLAN 41 - CCTV |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `CCTV_NETWORK` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC - Required CCTV Services |
| Logging | TBC |
| Description | Allow CCTV Traffic to Required Server Services |

The required CCTV services and ports have not yet been confirmed.

---

### R12b - Block Unauthorised CCTV Internal Access

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R12b |
| Action | Block |
| Interface | VLAN 41 - CCTV |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `CCTV_VLAN subnets` |
| Destination | `INTERNAL_NETWORKS` |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Unauthorised CCTV Internal Access |

Specific CCTV server traffic can later be permitted above this restriction when the required services are confirmed.

---

### R13a - Backup Network Access

**Status:** Planned

| pfSense Setting | Planned Configuration |
|---|---|
| Rule ID | R13a |
| Action | Pass |
| Interface | VLAN 91 - Backup |
| Address Family | IPv4 |
| Protocol | TBC |
| Source | `BACKUP_NETWORK` |
| Destination | `SERVER_NETWORK` |
| Destination Port | TBC - Backup/Replication Services |
| Logging | TBC |
| Description | Allow Required Backup and Replication Traffic |

The backup and replication services have not yet been confirmed.

---

### R13b - Block Unauthorised Backup Traffic

**Status:** Implemented, Not Yet Tested

| pfSense Setting | Configuration |
|---|---|
| Rule ID | R13b |
| Action | Block |
| Interface | VLAN 91 - Backup |
| Address Family | IPv4 |
| Protocol | Any |
| Source | `BACKUP_VLAN subnets` |
| Destination | Any |
| Destination Port | Any |
| Logging | Enabled |
| Description | Block Unauthorised Backup Traffic |

Required backup and replication services can later be permitted above this rule.

---

### R14 - Video Conferencing Access

**Status:** Planned

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

The final conferencing services and required ports have not yet been confirmed. Higher QoS may later be applied to video conferencing traffic to prioritise voice and video traffic.

Higher QoS may later be applied to video conferencing traffic to prioritise voice and video services.

## Firewall Validation

Firewall controls were tested using Employee and Visitor clients connected through Open vSwitch to the pfSense firewall. Testing included permitted Internet services and blocked communication between restricted VLANs.

| Test | Source | Destination | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| Employee DNS | `192.168.10.72` | External DNS | Allowed | DNS query successfully resolved `example.com` | Pass |
| Employee HTTP | `192.168.10.72` | Internet | Allowed | HTTP request returned `HTTP/1.1 200 OK` | Pass |
| Employee HTTPS | `192.168.10.72` | Internet | Allowed | HTTPS request returned `HTTP/2 200` | Pass |
| Visitor DNS | `192.168.20.72` | External DNS | Allowed | DNS query successfully resolved `example.com` | Pass |
| Visitor HTTP | `192.168.20.72` | Internet | Allowed | HTTP request returned `HTTP/1.1 200 OK` | Pass |
| Visitor HTTPS | `192.168.20.72` | Internet | Allowed | HTTPS request returned `HTTP/2 200` | Pass |
| Visitor to Employee | `192.168.20.72` | `192.168.10.72` | Blocked | Connection timed out and was logged by R04 | Pass |
| Visitor to Management | `192.168.20.71` | `192.168.99.1` | Blocked | Connection timed out and was logged | Pass |
| Visitor to Server VLAN Gateway | `192.168.20.71` | `192.168.90.1` | Blocked | Connection timed out and was logged | Pass |
| Employee to Management | `192.168.10.71` | `192.168.99.1` | Blocked | Connection timed out and was logged by R05 | Pass |

## Current Implementation Evidence  

<img width="800" alt="Screenshot 2026-08-26 145350" src="https://github.com/user-attachments/assets/fe6103d4-5c10-4ed5-acf9-b7da0aa379b8" />

- pfSense web page showing the firewall aliases ports configured for services such as, web traffic, DNS, SSH and HTTPS.

<img width="800" alt="Screenshot 2026-08-26 145414" src="https://github.com/user-attachments/assets/c6b3c16c-33a8-469f-92bd-ba5900533922" />

- pfSense web page showing the firewall aliases IPs configured for the VLAN networks. The INTERNAL_NETWORK alias groups together the PCM networks.

<img width="800" alt="Visitor R04 blocked in system logs" src="https://github.com/user-attachments/assets/3f191500-7e64-4064-94c4-98acf31e9774" />

- Visitor R04 blocked in system logs

<img width="451" height="158" alt="Visitor VLAN 20 not able to reach Employee VLAN 10" src="https://github.com/user-attachments/assets/12e3e2dc-1210-4c35-a3ff-66461eceb66c" />

- Visitor VLAN 20 not able to reach Employee VLAN 10
