# Security implementation test results

## T01 Employee Wi-Fi access to firewall management address

Date: 13 September 2026. Executed by Adam; evidence reviewed from supplied screenshots.

Purpose: verify that R06 blocks a controlled IPv4 ICMP request from the employee Wi-Fi client to the firewall management address and that matching records are retrievable centrally. Supports the access monitoring elements of SEC-01 and log collection elements of SEC-04.

| Test field | Recorded value |
| --- | --- |
| Source | HQ-EMP-LAPTOP, 192.168.11.100 |
| Destination | Firewall management address, 192.168.99.1 |
| Ingress | EMPLOYEE_WIFI_VLAN, vtnet2.11 |
| Rule | R06 Block Employee WIFI Access to Management |
| Tracking ID | 1787829015 |
| Destination alias | MANAGEMENT_NETWORK, 192.168.99.0/24 |
| Expected result | No ping replies; matching R06 block records retrievable in Grafana |
| Actual client result | 4 transmitted, 0 received, 100% packet loss |
| Actual central result | 4 matching ICMP block records with exact tracker, interface and addresses |
| Outcome | Passed for the stated scope |

Command executed on employee client:

```bash
date -u
ping -c 4 -W 2 192.168.99.1
```

Grafana Explore query:

```logql
{job="pfsense", site="brisbane-hq"} |= ",1787829015," |= ",192.168.11.100,192.168.99.1,"
```

Evidence:

- ../Evidence/T01%20Employee%20Ping%20Blocked.png
- ../Evidence/T01%20Grafana%20R06%20Four%20Blocks.png
- ../Evidence/HQ%20R06%20Logging%20Tracking%20ID.png
- ../Evidence/HQ%20Firewall%20Aliases.png

Limitations: this is an ICMP test against a firewall-owned management address. It does not prove all management hosts/services are blocked, nor validate alert thresholds, email delivery or acknowledgement/escalation. Four controlled requests produced four matching records here; this does not establish that arbitrary log counts equal unique connection attempts.

Timing: client date output precedes the command and is not the packet-send timestamp. Raw firewall records show 02:07:06–09 UTC, while Grafana's displayed record times are around 12:07:04–07. Validate clock synchronisation and timestamp interpretation before calculating delivery latency.

## Pending tests

- Threshold detection below, at and above the configured count/window, with source isolation.
- Administrator notification receipt and explicit acknowledgement.
- Missed-acknowledgement escalation and failed-delivery handling.
- Authentication, file auditing, evidence retention and logging-health tests.

## SMTP connectivity remediation and retest
On 13 September 2026, direct SMTP connectivity initially timed out. Adam configured a logged SERVER_VLAN IPv4 TCP allowance from HQ-MONITOR 192.168.90.60 to the GMAIL_SMTP hostname alias on destination port 587 (tracker 1789275475). The supplied nc -4 retest reports a successful connection to smtp.gmail.com at 172.217.194.108. Outcome: TCP connectivity passed for this attempt. TLS, authentication and notification receipt remain pending. Evidence: ../Evidence/HQ%20MONITOR%20SMTP%20Pass%20Rule.png, ../Evidence/GMAIL%20SMTP%20Host%20Alias.png and ../Evidence/HQ%20MONITOR%20SMTP%20Connectivity%20Succeeded.png.

### SMTP destination mismatch retest
After the observed GMAIL_SMTP table omitted 172.217.194.108 and a narrow alias update was instructed, the supplied nc retest successfully connected to that address on TCP 587. Evidence: ../Evidence/GMAIL%20SMTP%20Alias%20Address%20Mismatch.png and ../Evidence/SMTP%20Fixed%20IP%20Retest%20Succeeded.png. Outcome: TCP connectivity restored for the tested address. Email authentication and receipt still pending; temporary static address requires review.

### Independent Gmail authentication test
The direct Python SMTP test from HQ-MONITOR returned AUTHENTICATION SUCCEEDED. Adam identifies the credential as the first generated Google app password. TLS certificate verification was enabled; the test authenticated only and sent no email. This narrows the remaining investigation to the credential/configuration used by Grafana, without proving the newer app password is invalid. Evidence: ../Evidence/Gmail%20Direct%20Authentication%20Succeeded.png. Next retest Grafana with the verified credential and confirm mailbox receipt.

## T02 Manual contact-point email delivery
Date: 13 September 2026. Tester: Adam. Expected: Grafana contact-point test succeeds and the notification is received in the configured mailbox. Actual: Grafana reports Test notification sent successfully; supplied inbox screenshot shows [FIRING:1] TestAlert Grafana from PrimeCore Security Monitoring. Outcome: passed for manual test delivery to the demonstrated inbox. Evidence: ../Evidence/SEC03%20Grafana%20Test%20Send%20Succeeded.png and ../Evidence/SEC03%20Test%20Email%20Received.png. This does not establish event-triggered alerting, acknowledgements, escalation, all team recipients or measured timing targets. Rule threshold tests remain pending.

## T03 R06 below-threshold evaluation
Supplied Grafana evidence shows 4 records for source 192.168.11.100, threshold above 9, and condition false (0), state Normal. Outcome: passed for source parsing and below-threshold behaviour at count 4. Evidence: ../Evidence/R06%20Four%20Records%20Normal.png. Exact 9/10 boundary, above-threshold firing, source isolation, notification and recovery remain pending.

## T04 R06 threshold comparison
On 13 September 2026 Adam sent nine ICMP requests and then ten additional requests from 192.168.11.100 to 192.168.99.1. Both batches were unanswered. Grafana shows Normal at nine records and condition Firing (1) at approximately 19 within the five-minute window. Passed for nine-record non-firing and above-threshold condition evaluation; exact ten-record boundary was not isolated. Rule header remains Normal in the supplied second screenshot, so subsequent scheduled state and actual R06 notification must be checked. Evidence: ../Evidence/R06%20Nine%20Records%20Normal.png, ../Evidence/R06%20Nineteen%20Records%20Condition%20Firing.png, ../Evidence/R06%20Nine%20Plus%20Ten%20Ping%20Test.png. Recovery, event-triggered email and source-isolation tests remain pending.

## T05 R06 scheduled notification and recovery
Date: 13 September 2026. Outcome: passed for the demonstrated flow. Scheduled instance enters Firing for 192.168.11.100; actual rule-specific email received with A=19 and C=1. A subsequent RESOLVED email and Normal (Nodata) instance confirm resolution via configured NoData-to-OK handling. Displayed instance times are 17:14:40 firing and 17:19:40 normal; source/client/collector timing has not been independently reconciled for a latency claim. Resolution email A=-1 C=-1 is not a negative log count. Evidence: ../Evidence/R06%20Scheduled%20Instance%20Firing.png, ../Evidence/R06%20Firing%20Email%20Received.png, ../Evidence/R06%20Resolved%20Email%20Received.png, ../Evidence/R06%20Normal%20NoData%20Recovery.png. This supersedes earlier pending scheduled-state and event-email results. Exact-ten threshold, multi-source isolation, independent collector-health checks, human acknowledgement and escalation are still pending.


## Screenshot evidence appendix

### Figure E1 Controlled management access test

![Controlled management access test](../Evidence/T01%20Employee%20Ping%20Blocked.png)

Four ICMP requests to 192.168.99.1 received no replies. The corresponding firewall records provide the additional evidence linking this result to the tested rule.

### Figure E2 Correlated firewall records

![Correlated firewall records](../Evidence/T01%20Grafana%20R06%20Four%20Blocks.png)

Grafana retrieves four matching R06 records for source 192.168.11.100 and destination 192.168.99.1. This establishes the demonstrated collection and retrieval path.

### Figure E3 Scheduled alert settings

![Scheduled alert settings](../Evidence/R06%20Alert%20Corrected%20Settings.png)

The alert evaluates every 30 seconds and uses a threshold above nine matching events. NoData is mapped to OK; this must not be interpreted as proof of collector health.

### Figure E4 Firing notification received

![Firing notification received](../Evidence/R06%20Firing%20Email%20Received.png)

The rule-specific email reports A=19 and C=1 for source 192.168.11.100. Receipt demonstrates notification delivery, but not human acknowledgement or escalation.

### Figure E5 Resolved notification received

![Resolved notification received](../Evidence/R06%20Resolved%20Email%20Received.png)

The resolved email records NoData handling. A=-1 and C=-1 are state indicators, not negative event counts, and automated resolution does not close an incident.
