# Central firewall logging implementation

## Purpose and verified outcome

The PrimeCore Minerals lab collects pfSense firewall records centrally on HQ-MONITOR and makes them available through Grafana. Supplied console and Grafana screenshots verify file receipt and successful log retrieval. This supports the monitoring elements of SEC-01 and SEC-04. Detection thresholds, notification delivery and incident escalation remain to be implemented and validated.

## Implemented data path

pfSense syslog sender (configured receiver match: 192.168.90.1) → HQ-MONITOR (192.168.90.60), rsyslog UDP 514 → /var/log/pfsense.log → Alloy file reader → local Loki HTTP endpoint → Grafana Explore.

HQ-MONITOR runs Ubuntu 26.04. Grafana listens on TCP 3000; Loki listens on TCP 3100 and 9096. Actual permitted network access must be checked separately from listener state.

## Observed configuration

Rsyslog matches the sender IP 192.168.90.1 and writes matching events to /var/log/pfsense.log. Alloy configuration is stored in /etc/alloy/config.alloy and defines a file reader with job=pfsense and site=brisbane-hq labels. It forwards to http://127.0.0.1:3100/loki/api/v1/push.

Verified Grafana query:

```logql
{job="pfsense", site="brisbane-hq"}
```

The supplied Explore screenshot shows a log-volume graph and returned firewall records over the selected Last 1 hour range. This is evidence of a working query, not a saved dashboard or tested alert rule.

## Capacity improvement

Adam expanded the root logical volume and ext4 filesystem from approximately 14 GiB to 24 GiB using existing free LVM space. Verification shows 11 GB available, filesystem use reduced from 92% to 54%, and 4 GB left free in the volume group. This provides space for continued monitoring work; it does not validate long-term retention capacity.

## Evidence references

- ../Evidence/HQ%20MONITOR%20Storage%20Resize%20Verified.png
- ../Evidence/HQ%20MONITOR%20Service%20Listeners.png
- ../Evidence/HQ%20MONITOR%20Received%20Firewall%20Logs.png
- ../Evidence/HQ%20MONITOR%20Alloy%20Pipeline.png
- ../Evidence/HQ%20MONITOR%20Grafana%20Log%20Retrieval.png

## Saved dashboard verified 13 September 2026

Subsequent evidence shows the saved PrimeCore Security Monitoring dashboard with an HQ Firewall Logs panel returning records over Last 6 hours. This completes the saved log-view milestone that was pending at the initial Explore check. Evidence: ../Evidence/HQ%20MONITOR%20Saved%20Dashboard.png. No threshold alert or notification result is shown.

## Remaining validation

1. The firewall log dashboard is now saved. A blocked-record count can be added separately, clearly distinguished from a count of incidents or unique connection attempts.
2. Identify firewall interface and subnet roles before classifying sources as internal or external.
3. Validate source timestamps against collection timestamps before relying on timing targets.
4. Generate a controlled, identifiable lab event and match its source record to the Grafana result.
5. Parse fields and test procedure-specific thresholds without confusing broadcast noise or retransmitted packets with distinct incidents.
6. Configure notification delivery and separately validate acknowledgement and escalation.
7. Verify file rotation, retention, access control and logging-health alerts.

## Contribution attribution

Adam supplied evidence and executed the demonstrated storage change. Original authorship and dates of the existing monitoring configuration require confirmation before final first-person submission wording. AI assisted with inspection guidance, interpretation and this technical description. The final report should distinguish existing configuration, changes made this reporting period and validation performed.

## Notification delivery milestone
On 13 September 2026, Adam demonstrated successful Grafana contact-point test submission and inbox receipt through Gmail. Supporting evidence is SEC03_Grafana_Test_Send_Succeeded.png and SEC03_Test_Email_Received.png in the evidence directory. This supersedes the earlier pending manual mail-delivery status. The R06 event-triggered alert, threshold boundaries, acknowledgement and escalation are still pending. The test supports part of SEC-03 rather than full implementation of that procedure.

## Verified R06 automated alert and notification
On 13 September 2026, Adam demonstrated Normal at nine matching records, an above-threshold scheduled alert at 19 records for source 192.168.11.100, receipt of its rule-specific email and receipt of a subsequent resolved email. The rule evaluates every 30 seconds, counts R06 IPv4 inbound block records over five minutes by source, and uses threshold above nine. Recovery occurred through NoData mapped to OK, not an explicit zero-valued observation. This implements and tests part of SEC-01 and SEC-03. It does not complete all incident response, acknowledgement/escalation, health monitoring or retention requirements. Supporting screenshots are recorded under T05 in Security Test Results.md. These results supersede earlier pending event-triggered notification status.


## Screenshot evidence appendix

### Figure E1 Alloy collection configuration

![Alloy collection configuration](../Evidence/HQ%20MONITOR%20Alloy%20Pipeline.png)

The configuration reads /var/log/pfsense.log, applies the pfSense and Brisbane HQ labels and forwards records to Loki. It does not establish an enforced retention period.

### Figure E2 Central log retrieval

![Central log retrieval](../Evidence/HQ%20MONITOR%20Grafana%20Log%20Retrieval.png)

Firewall records are visible through Grafana with the recorded job and site labels. Availability in this view does not establish continuous collector health.

### Figure E3 Correlated firewall records

![Correlated firewall records](../Evidence/T01%20Grafana%20R06%20Four%20Blocks.png)

Grafana retrieves four matching R06 records for source 192.168.11.100 and destination 192.168.99.1. This establishes the demonstrated collection and retrieval path.
