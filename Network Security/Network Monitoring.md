# Network Monitoring and Logging

## Overview


## HQ Monitoring Server

The monitoring server is configured as `HQ-MONITOR`.

| Interface | Purpose | Address |
|---|---|---|
| ens3 | VLAN 90 network connection / central logging | 192.168.90.60/24 |
| ens4 | SPAN packet capture | No IP address |

Keeping the SPAN interface without an IP address allows it to be used only for passive packet capture, while the normal VLAN 90 interface is used for management and receiving centralised logs.




### OVS SPAN Configuration

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
