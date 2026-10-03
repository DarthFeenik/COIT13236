# HQ network interface and addressing register

Transcribed from Adam's HQ firewall console screenshot supplied 13 September 2026. This records configured firewall interfaces; switch port configuration, physical/virtual connections and security rules require separate verification.

| Interface | Device | VLAN | Firewall IPv4 address |
| --- | --- | --- | --- |
| WAN | vtnet0 | Not shown | 192.168.1.159/24, DHCP |
| LAN | vtnet1 | Not shown | 10.10.10.1/24 |
| EMPLOYEE_VLAN (opt1) | vtnet2.10 | 10 | 192.168.10.1/24 |
| VISITOR_VLAN (opt2) | vtnet2.20 | 20 | 192.168.20.1/24 |
| EMPLOYEE_WIFI_VLAN (opt3) | vtnet2.11 | 11 | 192.168.11.1/24 |
| PRINTER_VLAN (opt4) | vtnet2.30 | 30 | 192.168.30.1/24 |
| VIDEO_VLAN (opt5) | vtnet2.40 | 40 | 192.168.40.1/24 |
| CCTV_VLAN (opt6) | vtnet2.41 | 41 | 192.168.41.1/24 |
| IOT_VLAN (opt7) | vtnet2.50 | 50 | 192.168.50.1/24 |
| SERVER_VLAN (opt8) | vtnet2.90 | 90 | 192.168.90.1/24 |
| BACKUP_VLAN (opt9) | vtnet2.91 | 91 | 192.168.91.1/24 |
| MANAGEMENT_VLAN (opt10) | vtnet2.99 | 99 | 192.168.99.1/24 |

## Confirmed endpoints

- HQ-EMP-LAPTOP: 192.168.11.100/24 on ens3, default gateway 192.168.11.1. This belongs to employee Wi-Fi VLAN 11.
- HQ-MONITOR: 192.168.90.60/24 on ens3, default gateway 192.168.90.1. This belongs to server VLAN 90, not management VLAN 99.

## Test planning

Inspect employee Wi-Fi ingress rules before choosing a blocked destination. Prior Grafana records on vtnet0 include upstream-network broadcast traffic and do not demonstrate employee segmentation. Match a controlled event by test source, destination, service, firewall rule and time.

## Evidence

- ../Evidence/HQ%20FW%20Interface%20Map.png
- ../Evidence/HQ%20EMP%20LAPTOP%20Address%20Route.png

This register contributes to the technical artefacts for Report 2. It is not a complete network design: an annotated topology, rule rationale, site configuration and validation results remain necessary.


## Screenshot evidence appendix

### Figure E1 HQ firewall interfaces

![HQ firewall interfaces](../Evidence/HQ%20FW%20Interface%20Map.png)

The interface register shows the recorded VLAN gateways. Interface presence alone does not demonstrate that every switch port or access rule has been tested.

### Figure E2 Employee test endpoint addressing

![Employee test endpoint addressing](../Evidence/HQ%20EMP%20LAPTOP%20Address%20Route.png)

HQ-EMP-LAPTOP has 192.168.11.100/24 and default gateway 192.168.11.1, placing the test endpoint on the employee WiFi subnet.
