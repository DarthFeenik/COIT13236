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
