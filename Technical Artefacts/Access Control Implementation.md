# Access Control Implementation

## PrimeCore Minerals | Secure Multi Office Network

PC-02 | Version 0.1 | 23 September 2026

Status: Partly evidenced implementation and proposed extension

Owner: IT Administrator | Approver: Project lead | Approval date: Pending

Implement and validate role based access for PrimeCore users, shared files and network administration. This guide combines the demonstrated HQ network block with a proposed identity and file permission implementation.


## Baseline and prerequisites

HQ-EMP-LAPTOP uses 192.168.11.100 on VLAN 11. HQ-MONITOR uses 192.168.90.60 on VLAN 90. R06 blocks the tested IPv4 ICMP path to management gateway 192.168.99.1, tracker 1787829015. T01 correlates four blocked requests with four central records. This does not establish application permissions or all management protocols.
Before identity changes, record the actual Samba AD domain, domain controller, file server, share paths and supported versions. Confirm recoverable identity backups, a working emergency administrator and a change window. The group names below are proposed naming conventions, not discovered directory objects.

| Proposed group	| Access purpose	| Approver |
| --------------- | --------------- | -------- |
| GG_PC_Staff	| Ordinary staff business access	| Line manager| 
| GG_PC_File_Project_RW	| Modify approved project share	| Data owner |
| GG_PC_File_Project_RO	| Read approved project share	| Data owner |
| GG_PC_Network_Admin	| Administer network from approved management endpoint	| IT owner |
| GG_PC_Security_Analyst	| Read monitoring and incident evidence	| Security owner |
| GG_PC_Backup_Operator	| Operate backup jobs and restores	| IT owner |

## Implementation sequence

1. Export current membership, share permissions, filesystem ACLs and firewall configuration. Record the change reference and restore procedure.

2. Create role groups and dedicated test accounts. Use named administrator accounts separate from daily accounts. Avoid direct user grants unless an approved exception requires them.

3. Map approved staff to business groups, then grant resource permissions through groups. On Samba shares, validate the interaction of share restrictions and filesystem ACLs, including inheritance and effective rights.

4. Apply network rules at the actual ingress boundary. Preserve required DNS, authentication and time services. Place the management block ahead of broad employee allow rules after reviewing floating rules and existing states.


## Validation and rollback

1. Test with a fresh login or refreshed session so cached access does not conceal membership changes. Record the user, groups, target path, source address and time.

2. For each role, exercise allowed operations and one prohibited operation. A successful login alone does not prove least privilege.

3. Remove test data and temporary grants, preserve evidence, and obtain the resource owner’s acceptance. Reapply exported permissions or configuration if expected access fails; verify recovery using the same tests.


| Test	| Expected outcome	| Evidence status |
| ----- | ----------------- | --------------- |
| AC-01 employee ICMP to 192.168.99.1	| Blocked and correlated with R06	| T01 passed on 13 Sep |
| AC-02 employee HTTPS/SSH to approved management test host	| Denied and logged	| To execute |
| AC-03 approved administrator to approved management service	| Allowed from approved endpoint only	| To execute |
| AC-04 read only account reads then writes test share	| Read succeeds; write denied	| To execute |
| AC-05 modify account creates, changes and deletes test file	| Allowed only within approved share	| To execute |
| AC-06 remove role and terminate relevant session	| Further protected access denied	| To execute |

Test record: change ID; tester; timestamp and timezone; account and effective groups; source and destination; expected and actual outcomes; raw log and screenshot references; reviewer. Use disposable accounts and files. Do not test denial by locking the operational administrator out.

## Operational handover

Record actual group names, owners, authorised administrator endpoints and exceptions in PC-03. Reconcile membership monthly and remove obsolete access when a person changes role or leaves. Follow SEC-02 for shared-file misuse and SEC-05 for suspicious authentication. Retest after changes to groups, ACL inheritance, routing or firewall rule order.

