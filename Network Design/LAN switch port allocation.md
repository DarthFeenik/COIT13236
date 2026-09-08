
# Prime Core Metals LAN switch port allocation tables


## PCM-SITEA-SW01 - IP Address = 192.168.199.10

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
| `9` | E8 | ens11 |  |  |
| `10` | E9 | ens12 | trunk=11,20,99 | PCM-SITEA-AP01 |
| `11` | E10 | ens13 | trunk=10,11,20,30,40,41,50,90,91,99 | PCM-SITEA-SW02 |
| `12` | E11 | ens14 | trunk=10,11,20,30,40,41,50,90,91,99 | pfsense |
