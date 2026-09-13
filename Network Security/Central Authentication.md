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

| Setting | Configuration |
|---|---|
| Domain | `primecore.test` |
| Realm | `PRIMECORE.TEST` |
| FQDN | `hq-dc-01.primecore.test` |

I chose Samba Active Directory because it provided the central authentication features needed for the project while using less virtual resources than a Windows Server setup. 


The HQ-DC server was connected to Server VLAN 90 through Open vSwitch. The server uses the ens13 connection on the Brisbane HQ Open vSwitch.

HQ-DC was configured using these network settings:

| Setting | Value |
|---|---|
| IP Address | `192.168.90.10/24` |
| Default Gateway | `192.168.90.1` |
| VLAN | `90` |

By using a static address, the authentication server keeps the same address making it possible to reference it in firewall rules. 

## pfSense AD_SERVER Alias


| Alias | Address | Purpose |
|---|---|---|
| `AD_SERVER` | `192.168.90.10` | Brisbane HQ authentication server |

This makes the firewall rules easier to manage because I can use AD_SERVER instead of having to enter the IP address each time.

The following commands were used to add the connection to the Open vSwitch bridge and tag it with VLAN 90:
## Samba Setup
```bash
sudo ovs-vsctl add-port br0 ens13 tag=90
sudo ip link set ens13 up
```
Samba Active Directory and the supporting packages were installed on HQ-DC using:
```bash
sudo apt update
sudo apt install samba-ad-dc krb5-user bind9-dnsutils chrony -y
```
This installed the main packages needed for the domain controller which include, Samba Active Directory, Kerberos authentication, DNS tools and time synchronisation.

```bash
sudo systemctl disable --now smbd nmbd winbind
sudo systemctl mask smbd nmbd winbind
sudo systemctl unmask samba-ad-dc
sudo systemctl enable samba-ad-dc
```
The normal Samba services were disabled because the server uses the samba-ad-dc service instead.
```bash
bashsudo mv /etc/samba/smb.conf /etc/samba/smb.conf.orig
```
This commands move the pre-existing samba configurations to allow for a new configuration to be created
## Domain Setup
The PrimeCore Active Directory domain was created using:
```bash
sudo samba-tool domain provision --use-rfc2307 --interactive
```
The domain was configured using:

| Setting | Value |
|---|---|
| Realm | PRIMECORE.TEST |
| Domain | PRIMECORE |
| Server Role | dc |
| DNS Backend | SAMBA_INTERNAL |
| DNS Forwarder | `8.8.8.8` |

HQ-DC was then configured to use its own DNS using samba by disabling the original Ubuntu DNS resolver. 

```text
nameserver 127.0.0.1
search primecore.test
```

This command was used to disable the Ubuntu DNS resolver to allow samba to handle the DNS for the Active Directory domain.
```bash
sudo systemctl disable --now systemd-resolved
```

## Testing the Domain
After the domain controller was running, I used the following commands to check that the domain, DNS and Kerberos services were working as intedend.
```bash
sudo samba-tool domain info 127.0.0.1
host -t A hq-dc-01.primecore.test
host -t SRV _ldap._tcp.primecore.test
host -t SRV _kerberos._udp.primecore.test
```
All of the tests pass without issue 

## Creating Accounts 
Within the HQ-DC machine, I created an employee group to manage employee accounts through the domain instead of being created separately on each device.
```bash
sudo samba-tool group add "PrimeCore Employees"
```
A employee account was create as a test using my name "jared.williams" and was added to the PrimeCore Employees group.
```bash
sudo samba-tool user create jared.williams
sudo samba-tool group addmembers "PrimeCore Employees" jared.williams
```
To verify the account was created and added to the correct group I used the command:
```bash
sudo samba-tool group listmembers "PrimeCore Employees"
```
