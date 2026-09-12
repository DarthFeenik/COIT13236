# Shared File Access and Modification Alert Procedure


# COIT13236  |  Security monitoring and incident response


# SEC-02  |  Version 1.0  |  


Owner: IT Administrator  |  Approval: __________________  |  Effective date: __________


Detect denied access, inappropriate permissions and suspicious changes to protected shared files. The IT Administrator investigates with the file owner and preserves evidence before recovery.


Operating baseline: approve the proposed thresholds and response targets before activation. Review each semester and after a significant incident or system change.


## Monitoring requirements


Maintain a protected-share register with share path, host, data owner, authorised groups and permitted changes. Configure Samba file auditing for selected successful and failed operations, and forward records centrally. Record user, client IP, share, operation, result and path. Use host auditing for local changes that bypass Samba.


Samba full_audit records selected operations; it does not itself send administrator email or guarantee complete coverage of every access denial. Validate authentication failures and share-level denials separately. Match operation names to the installed Samba version and test share access after configuration changes; unsupported names can prevent access.


| Proposed detection condition	| Initial severity |
| ----------------------------- | ---------------- |
| 5 denied accesses by one user to one protected share in 5 minutes	| Medium |
| Denied access across 3 protected shares by one user in 5 minutes	| High |
| Unapproved permission change or confirmed unauthorised successful access	| High |
| 50 distinct files deleted or renamed by one user in 5 minutes	| High |
| 100 distinct files read by one user in 5 minutes outside its approved baseline	| Medium |
| Active widespread encryption or destructive file changes	| Critical |
 
## Investigation and response

1. Create and acknowledge an incident under SEC-03. Preserve matching raw audit events and identify the share, user, client, operation, result and affected time range.


2. Check group membership, share permissions and filesystem ACLs against the protected-share register. Confirm with the data owner whether the activity matches an approved task. A denied request does not establish that data was read.


3. Correlate the file events with Samba authentication and endpoint evidence. Count distinct files rather than raw read or write operations. Check approved backup, indexing and batch jobs before classifying bulk activity.


4. For confirmed misuse or active damage, restrict the affected account or client and terminate relevant sessions where supported. If damage continues, restrict writes to the affected share. Record approval, impact and rollback; isolate more broadly only when justified.


5. Preserve logs, permission state, file metadata and affected samples under SEC-04. Do not overwrite the only damaged copy with a restore. Record confirmed and potentially affected files separately.


6. Correct access rights or remediate the client. Recover affected files from a verified clean backup into a separate recovery location; the data owner validates content and permissions before replacement.


7. Test authorised read and write access and a denied test-user access. Monitor for at least 24 hours after restoration. Close only after the data owner accepts recovered files and the IT Administrator records root cause and follow-up work.


## Alert content

Use SEC-03 routing and include the share, operation, result, number of distinct files and restricted evidence link. Keep sensitive filenames and file contents out of email where they would expose data; authorised investigators access details in the incident record.
 
# Validation and protected share register


## Acceptance tests

| Controlled test	| Expected result |
| --------------- | --------------- |
| Test user accesses a restricted test folder	| Access denied; relevant denial captured by a validated source |
| Repeat denials to the configured threshold	| Alert reaches IT Administrator with correct user and share |
| Create, edit, rename and delete disposable protected files	| Selected successful operations recorded with usable attribution |
| Change permissions on a disposable folder	| Unapproved-change rule triggers and prior permissions can be restored |
| Run approved bulk test and restore one test file	| Distinct-file count is correct; restored content and ACLs pass checks |


Use disposable test files and accounts. Capture timestamps, expected and actual results, evidence links and tester. Validate both the central event and delivered notification. Record blind spots and add another source before accepting required coverage.


## Protected share register


Host and share: __________


Path and classification: __________


Data owner and authorised groups: __________


Audited operations and log source: __________


Approved bulk jobs and schedule: __________


Backup location and last restore test: __________


## Maintenance


Review protected shares and permissions monthly. Review detection thresholds after the first week of normal use and after workload changes. Any exclusion must be limited to a specific account, resource and schedule, with approval and expiry.
