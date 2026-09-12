# Security Alert Notification and Escalation Procedure

## COIT13236  |  Security monitoring and incident response

## SEC-03  |  Version 1.0  |  9 September 2026


Owner: IT Administrator  |  Approval: __________________  |  Effective date: __________


Ensure security detections reach an accountable IT Administrator, receive a recorded acknowledgement and escalate when unattended. This procedure supplies the common routing and response targets for SEC-01, SEC-02, SEC-04 and SEC-05.


Operating baseline: approve the proposed thresholds and response targets before activation. Review each semester and after a significant incident or system change.


## Routing and response targets

The following are proposed service targets, not measured service levels. Detection-to-notification time begins when a rule triggers. Acknowledgement time begins at notification dispatch. High and Critical targets require a staffed on-call arrangement; nominate coverage before activation.


| Severity	| Dispatch and acknowledgement	| Escalation |
| --------- | ----------------------------- | ---------- |
| Critical	| Email and backup channel within 1 minute; acknowledge within 10 minutes	| Backup and project lead at 10 minutes if unacknowledged |
| High	Email within 1 minute; acknowledge within 30 minutes	| Backup at 30 minutes; project lead at 60 minutes if still unacknowledged |
| Medium	Email within 5 minutes; acknowledge within 4 business hours	| Backup at 4 business hours; project lead next business day if still unowned |
| Low	Record immediately; daily digest; review next business day	| IT Administrator raises severity if impact or recurrence increases |


Business hours: Monday to Friday, 09:00 to 17:00 Australia/Brisbane, excluding local public holidays. High and Critical clocks run continuously. Promote severity immediately when new evidence increases impact; retain the original timestamps and escalation history.


### Contact register

Primary IT Administrator name / email / phone: __________________


Backup administrator name / email / phone: __________________


Project lead name / email / phone: __________________


Monitoring platform / incident register: __________________


Approved backup notification channel: __________________
 
## Dispatch and escalation process

1. The central monitoring service creates an alert ID, severity and incident link, then dispatches to the contact register. Configure an authenticated mail relay with protected credentials and test delivery to the real administrator mailbox.


2. Include event time and timezone, receipt time, source system, user or unknown, client IP, event type, affected resource, rule and threshold, observed outcome, automatic action and evidence link. Never report containment unless it actually occurred.


3. The recipient explicitly acknowledges in the incident register, accepts ownership and records the next action. Mail delivery, an open tracking signal or a read receipt is not acknowledgement.


4. At the severity deadline, route to the backup or project lead as specified. Continue Critical reminders every 10 minutes and High reminders every 30 minutes until an owner accepts. Record each delivery attempt and escalation.


5. Correlate matching alerts for the same rule, user or host and resource into one open incident over 15 minutes. Preserve each event and count; a new resource, rising severity or continuing damage must still notify.


6. If email delivery fails, retry after 1, 5 and 15 minutes and use the backup channel immediately for High or Critical alerts. Monitor the notification service from an independent check so its own failure can be reported.


7. The incident owner supplies Critical updates every 30 minutes and High updates every 2 hours until contained. Follow the relevant technical procedure, record recovery tests, and notify recipients of closure and follow-up actions.


## Ownership and communications


The IT Administrator coordinates technical response. The project lead coordinates service-impact communications and decides whether specialist or external reporting advice is needed. Keep operational details within approved recipients and use restricted incident links for sensitive evidence.
 
## Alert template and acceptance test


## Reusable alert template

Subject: SECURITY ALERT [Severity] [Alert ID] [Event type]
Event time and timezone: [value]
Detected / received: [value]
Source system / client IP: [value]
User / affected resource: [value or unknown]
Rule / count / window: [value]
Observed result: [blocked, denied, succeeded or unknown]
Automatic action: [action actually completed or none]
Incident and evidence link: [restricted link]
Acknowledge by: [date and time]
Required action: Accept ownership and begin the relevant response procedure.


##  End to end acceptance test
•	Generate one controlled detection of each severity; verify timestamps, content, mailbox receipt and correct incident link.
•	Leave a test alert unacknowledged and verify backup escalation and reminders at the stated deadlines. Mark all messages clearly as TEST.
•	Acknowledge a test incident; verify reminders stop and the accepted owner is recorded.
•	Interrupt the test mail route; verify retry records and the independent backup channel. Restore the route and reconcile queued alerts.
•	Generate duplicate events and then increase severity; verify correlation retains evidence and the severity increase produces a new notification.


Record expected and actual times, recipients, evidence and pass or fail. Repeat after contact, rule, mail relay or monitoring changes and monthly during operation. Review overdue incidents each working day.
