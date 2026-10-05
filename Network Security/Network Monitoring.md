# Network Monitoring and Logging

## Overview

Centralised monitoring and logging was set up so network and security activity from Brisbane HQ and Mine Site A could be reviewed from one location.

HQ-MONITOR is used as the central monitoring server and receives firewall, authentication and mirrored network traffic from across the environment.

The monitoring setup uses:

- rsyslog for receiving and storing logs
- Grafana Alloy for reading and forwarding log data
- Loki for storing the collected logs
- Grafana for viewing and searching the logs
- tcpdump for checking mirrored network traffic

## HQ Monitoring Server

The monitoring server is configured as HQ-MONITOR.

| Interface | Purpose | Address |
|---|---|---|
| ens3 | VLAN 90 network connection / central logging | `192.168.90.60/24` |
| ens4 | SPAN packet capture | No IP address |

Keeping the SPAN interface without an IP address allows it to be used only for passive packet capture, while the normal VLAN 90 interface is used for management and receiving centralised logs.

## Firewall Log Collection

Both pfSense firewalls send their firewall and system logs to HQ-MONITOR using UDP port 514.

### Brisbane HQ

HQ-FW sends its logs directly through the Brisbane HQ Server VLAN to:

`192.168.90.60`

The logs are stored on HQ-MONITOR in:

```bash
/var/log/pfsense.log
```
