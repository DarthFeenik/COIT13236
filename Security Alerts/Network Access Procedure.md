# Unauthorised Network Access Detection and Response Procedure

# COIT13236  |  Security monitoring and incident response
## SEC-01  |  Version 1.0  | 


Owner: IT Administrator  |  Approval: __________________  |  Effective date: __________


Detect and investigate unauthorised network access, suspicious remote sessions and unexpected administrative activity. The IT Administrator uses this procedure for pfSense, network devices, servers and monitored workstations.
Operating baseline: approve the proposed thresholds and response targets before activation. Review each semester and after a significant incident or system change.


## Monitoring requirements

Forward relevant pfSense firewall and system logs to the central monitoring service. Collect remote-access authentication, DHCP or device inventory records, and server login records where available. Log relevant firewall rules explicitly. Traffic between devices on the same network segment may not pass through pfSense; use endpoint or switch evidence for that activity.


| Detection condition	| Initial severity |
| 10 blocked attempts from one internal device to protected services in 5 minutes	| Medium |
| 5 failed remote or administrative logins for one account in 5 minutes	| High |
| Successful administrative access from an unapproved source, or confirmed unauthorised access	| High |
| Active lateral movement, widespread compromise or destructive activity	| Critical |
| One blocked connection or newly observed device without other indicators	| Low; validate against inventory |


These are proposed starting thresholds. A blocked connection or unfamiliar IP alone does not prove compromise. Correlate source, destination, account, asset ownership and approved changes; use SEC-05 for authentication correlation.
Responsibilities
The monitoring service records and routes detections. The IT Administrator owns triage and containment. The nominated backup administrator takes over missed acknowledgements under SEC-03. The project lead approves wider service disruption and accepts residual risk.
 
Investigation and response
1. Open an incident record, record event and receipt times, rule ID and severity, and acknowledge the alert under SEC-03. Preserve the original event before changing the rule or host.
2. Validate the source using DHCP lease time, inventory, switch port and login evidence. Account for shared IP addresses, NAT and clock differences. Check approved maintenance with the device owner using a known contact.
3. Review related firewall, authentication and endpoint events around the detection. Determine whether traffic was blocked or allowed, whether login succeeded, which systems were reached and whether privileges changed.
4. If activity is ongoing, isolate the affected endpoint or block the narrowest confirmed malicious connection. Record the time, reason, approver and rollback method. Preserve volatile information when feasible without delaying urgent containment.
5. Use SEC-05 for compromised accounts and SEC-02 for affected shares. Avoid disabling shared infrastructure solely because a threshold fired. Escalate broader isolation to the project lead; record emergency action immediately.
6. Export relevant logs and configuration evidence using SEC-04. Remove the cause through credential recovery, access correction or host remediation. Test the change before restoring access.
7. Restore connectivity in stages and observe for at least 24 hours. Confirm normal authorised access and no recurrence. Record impact, root cause, actions, evidence and follow-up owner; the IT Administrator closes, with project lead review for High or Critical incidents.
Notification and fallback
Send High and Critical detections immediately through SEC-03, including source IP, destination, port, firewall action and related user where known. If the monitoring or email service is unavailable, use the backup contact channel and preserve local logs for later reconciliation.
 
Validation and operating record
Acceptance tests
Controlled test	Expected result
From a test endpoint, attempt access to an explicitly blocked test service	Connection denied; matching firewall event reaches the collector
Generate the configured repeat threshold against the test service	One correlated alert with correct count, source, destination and severity
Generate an approved test administrative login from a non-approved test source	High alert; approval context can be recorded without deleting evidence
Simulate a missed administrator acknowledgement	Backup escalation occurs within SEC-03 target
Restore test endpoint access after containment	Authorised traffic works; monitoring remains active
Run only on approved lab assets during a scheduled test window. Record event time, collector time, notification time, acknowledgement, actual result, evidence link and tester. Tests pass only when all expected results are demonstrated; retest failures.
Routine review
Each working day, review unresolved alerts and source health. Weekly, compare unfamiliar devices with inventory and check rule exceptions. After changes, repeat a controlled detection and delivery test. Every exception must have an owner, reason, scope and expiry.
Incident record fields
Incident ID: __________  Owner: __________  Severity: __________
Detected and acknowledged: __________  Source and destination: __________
Evidence location: __________  Containment and rollback: __________
Recovery test: __________  Closure reviewer and date: __________
