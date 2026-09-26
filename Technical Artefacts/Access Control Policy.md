# Access Control Policy

## PrimeCore Minerals | Secure Multi Office Network

PC-03 | Version 0.1 | 23 September 2026

Status: Proposed policy for approval

Owner: IT Administrator | Approver: Project lead | Approval date: Pending

Define who may access PrimeCore systems, who approves access and how access is removed. This policy covers staff, contractors, service identities, cloud resources, network devices and shared information.


## Required controls

•	Use a unique named identity for each person. Keep administrative identities separate from ordinary work. Grant only the rights required for the current role and approved resource.
•	Resource owners approve access before the administrator implements it. The requester must not approve their own privileged access. Record the requested role, resource, duration and business purpose.
•	Use MFA for remote access and privileged services where supported. Prefer phishing resistant methods when the selected service supports them. Document service limitations and compensating controls.
•	Store passwords in an approved password manager. Proposed baseline: unique passphrases of at least 15 characters where supported, block known compromised values, and change credentials after suspected compromise or an authorised reset. Do not share passwords or embed them in scripts.
•	Service identities must have a named owner, narrow scope and a documented rotation and dependency plan. Use managed identities where available. Store recovery secrets separately from ordinary user access.


## Access Lifecycle

| Event	| Required action	| Proposed target |
| ----- | --------------- | --------------- |
| Joiner	| Manager confirms identity and role; data owner approves groups; administrator tests access	| Before first access |
| Role change	| Review old and new access together; remove superseded groups	| At role change |
| Leaver	| Disable access, revoke sessions where supported, recover devices and transfer data ownership	| At agreed departure time; urgent on notice for immediate termination |
| Temporary access	| Record sponsor and expiry; remove automatically where supported	| At approved expiry |
| Emergency access	| Record reason, custodian, use and post-event review	| Review next working day |


## Permission governance and assurance

| Role	| Default entitlement	| Restriction |
| ----- | ------------------- | ----------- |
| Staff	| Approved business applications and team files	| No infrastructure administration |
| Contractor or visitor	| Sponsored, time limited resources or guest Internet	| No implied internal network rights |
| Network administrator	| Named management systems from approved endpoint	| Separate privileged account |
| Security analyst	| Read relevant logs and incident records	| No routine alteration of source records |
| Backup operator	| Run approved backup and recovery actions	| Restore disclosure requires data-owner approval |

Authentication proves identity; authorisation determines which resource and operation that identity may use. Network reachability, VPN connection and domain membership must not be treated as permission to every share or management interface.

## Monitoring and review

Review privileged membership monthly and all resource memberships each term or every three months, whichever is sooner. Owners must confirm continuing need. Retain access requests, approvals, effective permission tests and removal records in a restricted register. Use the proposed SEC-04 schedule for associated security logs.
Proposed ordinary-account lockout is 10 failures in 15 minutes with a 15 minute lockout, subject to supported settings and testing. The separate proposed authentication alert is five failures in five minutes. Neither threshold is proven by the existing R06 network block alert. Never unlock an account until identity and the failure source are checked.


## Acceptance and evidence

The owner accepts implementation after one allowed and one denied test for each role, demonstrated leaver removal, a tested emergency account, and a documented exception register. PC-02 provides the test matrix. Record actual results rather than treating this policy as evidence of deployment.

## Review and exceptions

The owner reviews this document every six months and after a significant incident or system change. Record exceptions with the affected asset, business reason, risk, compensating control, approver and expiry. Approval does not replace a successful implementation test.




