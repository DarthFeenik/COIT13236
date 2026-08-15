# Firewall Controls

## Network Segmentation

The firewall rule configuration will manage all communications between the Employee, Visitor and Management networks by controlling which traffic is allowed and which traffic is blocked. This prevents unauthorised users accessing restricted areas while allowing users that are approved. 

## Planned Network Aliases

| Alias | Network |
|---|---|
| EMPLOYEE_VLAN | 192.168.1.0/24 |
| VISITOR_VLAN | 192.168.2.0/24 |
| MANAGEMENT_VLAN | 192.168.99.0/24 |

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

