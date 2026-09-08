# Prime Core Minerals LAN Access Point - AP - port allocation table


As all AP's will be configured the same, there is only 1 table to demonstrate the setup. This is table 2.
They will be identified in the network management VLAN by having the last octet of the IP address being different. The hundreds location will start with a 1 then the ten's location will correspond to the office number and the ones location will be the AP number in that office. As we don't expect any more than 10 AP's in the office, this sequence can be maintained in all offices.
First 3 octets of IP address will be from office location. Both Brisbane AP's and SiteB office will be used as examples in the following table.

Table
| Location | AP Name | 1st 3 octets | 100's place | 10's place | 1's place |
|---|---|---|---|---|---|
| Brisbane AP1 | PCM-BNE-AP01 | `192.168.99.` | `1` | `1` | `0` |
| Brisbane AP2 | PCM-BNE-AP02 | `192.168.99.` | `1` | `1` | `1` |
| SiteB | PCM-SITEB-AP01 | `192.168.199.120.` | `1` | `2` | `0` |


Laptops in the domain will connect to the SSID called - PCM-Employee.
Non-domain devices (like laptops, tablets, smart phones, etc.) will connect to SSID PCM-Visitor.
As SSID's can't be replicated in a virtual enviornment, we have allocated VLANs to specific ports on the AP and connected corresponding laptops to them to replicate the network security associated with those vlans.

If additional devices are needed to connect to the AP then any of the spare ports can be updated with the correct vlan tag.



## Table 2 - All Offices (with PCM-BNE-AP01 as an example)
### PCM-BNE-AP01 - IP Address = 192.168.99.110

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|------------|------------------|--------------------|-------------------------|--------------------|
| `1` | E0 | ens3 | tag=11 | WiFi Employee PC |
| `2` | E1 | ens4 | tag=20 | WiFi Visitor PC |
| `3` | E2 | ens5 | | |
| `4` | E3 | ens6 | | |
| `5` | E4 | ens7 | | |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | trunk=11,20,99 | PCM-BNE-AP01 |
