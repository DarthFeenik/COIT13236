# Backup Policy

## PrimeCore Minerals | Secure Multi Office Network

PC-06 | Version 0.1 | 23 September 2026

Status: Proposed policy for approval

Owner: IT Administrator | Approver: Project lead | Approval date: Pending


## Backup operating baseline

Maintain three copies of important data across two failure domains, including one offline or immutable copy with separate administrative credentials. A snapshot on the same EVE host is useful for rollback but does not protect against loss of that host. VLAN 91 exists in the addressing register; no working backup repository or restore result is evidenced. 

Data or system	Proposed schedule and retention	Recovery objective
Firewall and network configuration	After approved changes and daily; 30 daily and 12 monthly copies	RPO 24 hours or last approved change; RTO 4 hours
Directory service	Daily supported, consistent backup; 30 daily and 12 monthly copies	RPO 24 hours; RTO 8 hours
Protected shared files	Every 4 hours; retain 7 days of these points, 30 daily and 12 monthly copies	RPO 4 hours; RTO 8 hours
Monitoring configuration	After changes and daily; 30 daily and 12 monthly copies	RPO 24 hours; RTO 8 hours
Security logs and evidence	Daily protected copy; retention and holds under SEC-04	RPO 24 hours for protected copy; RTO 24 hours
