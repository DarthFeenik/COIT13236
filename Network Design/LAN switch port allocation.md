
# Prime Core Minerals LAN switch port allocation tables
Below is the LAN switch port allocation. This maps what port is connected to which device and the vlan committed to which port.
In EVE-NG, PCM-BNE-SW01, PCM-BNE-SW02, PCM-SITEA-SW01, PCM-SITEA-SW02 and PCMSITEB-SW01 setup. 
PCMSITEC-SW01 and PCMSITED-SW01 are a replication of PCM-SITEB-SW01 with only their hostname and switch IP address changing.



## Brisbane Office
### PCM-BNE-SW01 - IP Address = 192.168.99.10

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|------------|------------------|--------------------|-------------------------|--------------------|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=90 | CCTV Server |
| `3` | E2 | ens5 | tag=90 | AD Server |
| `4` | E3 | ens6 | tag=90 | IT Monitoring Server |
| `5` | E4 | ens7 | tag=90 | Printer Server |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | | |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-BNE-AP01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-BNE-SW02 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | pfsense |


## PCM-BNE-SW02 - IP Address = 192.168.99.11

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|------------|------------------|--------------------|-------------------------|--------------------|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=41 | Printer |
| `3` | E2 | ens5 | tag=90 | VC Unit |
| `4` | E3 | ens6 | tag=90 | Archive Server |
| `5` | E4 | ens7 | tag=90 | Backup Server |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | | |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-BNE-AP02 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-BNE-SW02 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | pfsense |




## Site Offices
### PCM-SITEA-SW01 - IP Address = 192.168.199.10

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|------------|------------------|--------------------|-------------------------|--------------------|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=41 | CCTV Camera |
| `3` | E2 | ens5 | tag=90 | CCTV Server |
| `4` | E3 | ens6 | tag=90 | AD Server |
| `5` | E4 | ens7 | tag=90 | IT Monitoring Server |
| `6` | E5 | ens8 | tag=90 | Printer Server |
| `7` | E6 | ens9 |  |  |
| `8` | E7 | ens10 |  |  |	
| `9` | E8 | ens11 | trunk=11,20,99 |  PCM-SITEA-AP01  |
| `10` | E9 | ens12 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITED-SW01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEA-SW02 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | pfsense |



### PCM-SITEA-SW02 - IP Address = 192.168.199.11

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|---|---|---|---|---|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=91 | Backup Server |
| `3` | E2 | ens5 | tag=91 | Archive Server |
| `4` | E3 | ens6 | tag=40 | VC Unit |
| `5` | E4 | ens7 | tag=30 | Printer |
| `6` | E5 | ens8 | tag=90 | Web Server |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | trunk=11,20,99 | PCM-SITEA-AP02 |
| `10` | E9 | ens12 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEB-SW01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEA-SW02 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | pfsense |



### PCM-SITEB-SW01 - IP Address = 192.168.199.20

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|---|---|---|---|---|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=40 | VC unit |
| `3` | E2 | ens5 | tag=30 | Printer |
| `4` | E3 | ens6 | tag=50 | IoT device |
| `5` | E4 | ens7 | tag=41 | CCTV camera |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | | |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-SITEB-AP01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEC-SW01 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEA-SW02 |



### PCM-SITEC-SW01 - IP Address = 192.168.199.30

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|---|---|---|---|---|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=40 | VC unit |
| `3` | E2 | ens5 | tag=30 | Printer |
| `4` | E3 | ens6 | tag=50 | IoT device |
| `5` | E4 | ens7 | tag=41 | CCTV camera |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | | |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-SITEC-AP01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITED-SW01 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEB-SW01 |



### PCM-SITED-SW01 - IP Address = 192.168.199.40

|Port Number | EVE-NG Port Name | Switch config name | Port VLAN type & number | Port connected to: |
|---|---|---|---|---|
| `1` | E0 | ens3 | tag=10 | LAN Employee PC |
| `2` | E1 | ens4 | tag=40 | VC unit |
| `3` | E2 | ens5 | tag=30 | Printer |
| `4` | E3 | ens6 | tag=50 | IoT device |
| `5` | E4 | ens7 | tag=41 | CCTV camera |
| `6` | E5 | ens8 | | |
| `7` | E6 | ens9 | | |
| `8` | E7 | ens10 | | |	
| `9` | E8 | ens11 | | |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-SITED-AP01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEC-SW01 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEA-SW01 |
