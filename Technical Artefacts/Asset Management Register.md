# Asset Management Register

## PrimeCore Minerals | Secure Multi Office Network

PC-04 | Version 0.1 | 23 September 2026

Status: Initial inventory with verification actions

Owner: IT Administrator | Approver: Project lead | Approval date: Pending


## Register conventions

Asset IDs remain stable if a hostname changes. Proposed names use SITE-ROLE-NN, for example HQ-MON-01; preserve existing HQ-MONITOR and HQ-EMP-LAPTOP names until a controlled rename is approved. Record logical and physical location separately. Evidence observed on 13 September 2026 is not a current live inventory scan.

| ID and asset	| Location and addressing	| Specification and status |
| ------------- | ----------------------- | ------------------------ |
|PC-A001 HQ-FW	 |EVE HQ firewall, WAN 192.168.1.159/24 DHCP; LAN , 10.10.10.1/24; VLAN gateways in PC-13	 | pfSense; installed version to verify Observed interfaces |
PC-A002 HQ-MONITOR	| EVE HQ monitoring guest 192.168.90.60/24; GW 192.168.90.1; ens3	| Ubuntu 26.04; root filesystem about 24 GiB Observed services and address |
PC-A003 HQ-EMP-LAPTOP	| EVE HQ test endpoint 192.168.11.100/24; GW 192.168.11.1; ens3	| OS and allocated capacity to record Observed test endpoint |
PC-A004 EVE host	| Lab virtualisation platform Management address to record	| Host CPU, RAM, disk, version and location to record Inventory required |

## Software and discovery register

| Component	| Host and purpose	| Recorded state |
| --------- | ----------------- | -------------- |
| rsyslog	| HQ-MONITOR; receives firewall UDP 514	| Observed; version and retention to record |
| Alloy	| HQ-MONITOR; forwards /var/log/pfsense.log to Loki	| Observed; version to record |
| Loki	| HQ-MONITOR; central log storage	| Observed TCP 3100 and 9096 listeners; version to record |
| Grafana	| HQ-MONITOR; query, dashboard and alerts	| Observed TCP 3000; version and access controls to record |
| Gmail SMTP route	| Monitoring mail submission	| Test receipt evidenced; final firewall rule needs capture |


| ID and role	| Owner role	| Discovery required |
| ----------- | ----------- | ------------------ |
| PC-A005 Directory service	| Identity administrator	| Domain, hostname, version and backup to verify; Discovery required |
| PC-A006 File service	| Data owner	| Host, shares, ACL model and capacity to verify; Discovery required |
| PC-A007 Backup repository	| Backup operator	| Capacity, software and immutability to select; Planned |
| PC-A008 Azure prototype	| Cloud administrator	| Gateway, test VM and logging in PC-05; Planned |

## Lifecycle and record fields

For each asset record ID, name, owner, custodian, type, serial or VM ID, location, IP and MAC, OS and software versions, support or licence status, classification, criticality, dependencies, backup policy, last patch, evidence reference, last verification and disposal date. Use “not recorded” rather than inventing serial numbers or quantities.

On acquisition, approve an owner and baseline before connecting. On change, reconcile the register and configuration backup. Monthly, compare EVE nodes, directory devices, firewall leases and software inventory. On retirement, revoke identities and keys, remove DNS and rules, securely dispose of data and record the authoriser and method.

## Verification actions

Confirm the EVE host and physical equipment inventory; reconcile branch-site assets with the network designer; confirm directory and file roles; capture software versions; record actual cloud resources only after deployment. The companion CSV is an editable initial asset register, not a scan result.


