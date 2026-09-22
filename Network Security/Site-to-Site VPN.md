# PrimeCore Minerals Site-to-Site VPN

A site-to-site VPN was implemented to provide secure communication between the PrimeCore Minerals Brisbane HQ and Mine Site A. The VPN connects the internal networks at both locations while allowing traffic to travel across the ISP network in an encrypted form.
The VPN was configured using pfSense at both locations and uses IKEv2/IPsec. This allows selected internal networks at Brisbane HQ and Mine Site A to communicate without exposing their private network traffic across the ISP infrastructure.


## 3. VPN Architecture

### Brisbane HQ

| Component | Address |
|---|---|
| HQ-FW WAN | `172.16.100.2/30` |
| HQ-ISP gateway | `172.16.100.1` |
| Employee VLAN | `192.168.10.0/24` |
| Server VLAN | `192.168.90.0/24` |

### Mine Site A

| Component | Address |
|---|---|
| SITE-A-FW WAN | `172.16.101.2/30` |
| SITE-A-ISP gateway | `172.16.101.1` |
| Employee VLAN | `192.168.110.0/24` |
| Server VLAN | `192.168.190.0/24` |

## 4. IKEv2 Phase 1 Configuration
|Setting |Brisbane HQ| Mine Site A|
|---|---|---|
|Key Exchange| IKEv2| IKEv2|
|Local WAN Address| 172.16.100.2| 172.16.101.2|
|Remote Peer| 172.16.101.2| 172.16.100.2|
|Authentication| Mutual Pre-Shared Key| Mutual Pre-Shared Key|
|Encryption| AES-256| AES-256|
|Hash / Integrity| SHA-256| SHA-256|

## 5. IPsec Phase 2 Configuration

