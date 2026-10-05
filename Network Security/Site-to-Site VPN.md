# PrimeCore Minerals Site-to-Site VPN

A site-to-site VPN was implemented to provide secure communication between the PrimeCore Minerals Brisbane HQ and Mine Site A. The VPN connects the internal networks at both locations while allowing traffic to travel across the ISP network in an encrypted form.
The VPN was configured using pfSense at both locations and uses IKEv2/IPsec. This allows selected internal networks at Brisbane HQ and Mine Site A to communicate without exposing their private network traffic across the ISP infrastructure.


## VPN Architecture

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

## IKEv2 Phase 1 Configuration
|Setting |Brisbane HQ| Mine Site A|
|---|---|---|
|Key Exchange| IKEv2| IKEv2|
|Local WAN Address| 172.16.100.2| 172.16.101.2|
|Remote Peer| 172.16.101.2| 172.16.100.2|
|Authentication| Mutual Pre-Shared Key| Mutual Pre-Shared Key|
|Encryption| AES-256| AES-256|
|Hash / Integrity| SHA-256| SHA-256|

## IPsec Phase 2 Configuration

Phase 2 is used to control which internal networks are included in the VPN. Separate Phase 2 connections were created for the Employee and Server networks.

| Connection | Brisbane HQ Network | Mine Site A Network |
|---|---|---|
| Employee | `192.168.10.0/24` | `192.168.110.0/24` |
| Server | `192.168.90.0/24` | `192.168.190.0/24` |

The Phase 2 connections use ESP with AES-256 encryption and SHA-256 for integrity. PFS Group 14 is also used on both sides.

Only the networks that need to communicate between Brisbane HQ and Mine Site A were added to the VPN. The firewall rules provide another level of control over what traffic is actually allowed between the sites.

## VPN Firewall Rules

Firewall rules were configured on both pfSense firewalls to control how the VPN is established and what traffic is allowed through it.

### WAN Rules

The WAN interfaces allow the traffic required to create and maintain the VPN connection.

The following traffic is allowed between the VPN endpoints:

- UDP port 500 for IKE
- UDP port 4500 for NAT-T
- ESP for IPsec traffic

The WAN rules are limited to the remote VPN peer so the interfaces are not opened more than required.

### IPsec Rules

Once traffic reaches the other side of the VPN, the IPsec firewall rules control where it is allowed to go.

| Firewall | Source | Destination | Service | Purpose |
|---|---|---|---|---|
| HQ-FW | `192.168.110.0/24` | `192.168.10.0/24` | ICMP | Site A Employee to HQ Employee testing |
| HQ-FW | `192.168.190.0/24` | `192.168.90.60` | UDP 514 | Site A firewall logs to HQ-MONITOR |
| HQ-FW | `192.168.190.0/24` | `192.168.90.60` | ICMP | Site A Server to HQ-MONITOR testing |
| SITE-A-FW | `192.168.10.0/24` | `192.168.110.0/24` | ICMP | HQ Employee to Site A Employee testing |
| SITE-A-FW | `192.168.90.0/24` | `192.168.190.0/24` | ICMP | HQ Server to Site A Server testing |

This means that being included in the VPN does not automatically give a network access to everything at the other location.

## Testing and Validation

Several tests were completed to make sure the VPN was working correctly and that traffic was travelling between Brisbane HQ and Mine Site A as intended.

### WAN Packet Capture

A packet capture was completed on the HQ-ISP connection using Wireshark.

The capture showed IKE and ESP traffic travelling between:

- HQ-FW: `172.16.100.2`
- SITE-A-FW: `172.16.101.2`

This confirmed that the IKEv2/IPsec tunnel was active and encrypted VPN traffic was travelling between both locations.\

## Troubleshooting and Changes

A few issues were found while setting up and testing the VPN.

### Employee VPN Rule

One Employee-to-Site-A firewall rule was originally placed on the WAN interface. The rule was moved to the Employee VLAN interface, which allowed the traffic to pass through the VPN correctly.

### Missing HQ IPsec Rule

Traffic from the Mine Site A Server network to HQ-MONITOR was initially being blocked. An additional IPsec rule was added on HQ-FW, which allowed the required traffic and Site A firewall logs to reach HQ-MONITOR.
