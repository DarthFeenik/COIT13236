# Central Authentication

PrimeCore Minerals requires a central authentication solution so employee accounts can be managed from one location so they dont have to be created sepereatly on each device. 

For the Brisbane HQ network, a Samba Active Directory Domain Controller was set up on the `HQ-DC-01` server. The server is connected to Server VLAN 90 and uses the static IP address `192.168.90.10`.

## Authentication Design

| Setting | Configuration |
|---|---|
| Server | HQ-DC-01 |
| VLAN | Server VLAN 90 |
| IP Address | 192.168.90.10 |
| Domain | primecore.test |
| Realm | PRIMECORE.TEST |
| FQDN | hq-dc-01.primecore.test |
| Authentication | Samba Active Directory |
