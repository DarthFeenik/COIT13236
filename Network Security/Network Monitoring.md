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
### Mine Site A

SITE-A-FW also sends its firewall logs to HQ-MONITOR using UDP port 514.

Because Mine Site A is located on a different network, these logs travel through the site-to-site IPsec VPN before reaching the monitoring server.

The Site A firewall logs are stored separately in:

```bash
/var/log/sitea-pfsense.log
```

Keeping the HQ and Site A logs separate makes it easier to tell which location each event has come from.

## Authentication Logging

Authentication events from the PRIMECORE.TEST Samba Active Directory domain are also collected by the monitoring system.

These events come from HQ-DC at `192.168.90.10` and allow successful and failed login activity to be reviewed alongside the firewall events.

---
## Log Processing

The logs collected by `HQ-MONITOR` are handled using rsyslog, Grafana Alloy, Loki and Grafana.

The basic flow is:
```
pfSense/HQ-DC > rsyslog > Grafana Alloy > Loki > Grafana
```
Rsyslog receives the incoming firewall events and stores them in separate log files.

Grafana Alloy reads the firewall and authentication logs and forwards them to Loki for storage.

Grafana is then used as the main dashboard for viewing the collected information, with separate dashboard views for Brisbane HQ and Mine Site A.

## OVS SPAN Configuration

A SPAN mirror was configured on the Brisbane HQ Open vSwitch so traffic passing through the pfSense trunk could also be copied to HQ-MONITOR.

The following command was used to create the SPAN mirror:

```bash
sudo ovs-vsctl \
-- --id=@src get Port ens4 \
-- --id=@dst get Port ens12 \
-- --id=@m create Mirror name=HQ-SPAN \
select-src-port=@src \
select-dst-port=@src \
output-port=@dst \
-- set Bridge br0 mirrors=@m
```

The mirrored interface does not need an IP address because it is only used to observe copied traffic.

## Grafana Dashboard Access

Access to the Grafana dashboard is restricted through the VLAN 99 Management network.

HQ-MGMT-PC is allowed to connect to HQ-MONITOR on TCP port 3000, keeping access to the monitoring dashboard limited to the management network.

## Testing

### HQ Firewall Logs

Firewall events were generated on HQ-FW and then checked on HQ-MONITOR.

The events appeared in:

```bash
/var/log/pfsense.log
```

This confirmed that Brisbane HQ firewall logs were being received by the monitoring server.

### Mine Site A Firewall Logs

Firewall activity was also generated at Mine Site A.

New SITE-A-FW events appeared in:

```bash
/var/log/sitea-pfsense.log
```
This confirmed that Site A firewall logs were successfully travelling through the VPN and reaching HQ-MONITOR.


