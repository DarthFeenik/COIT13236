# SEC-01 alert acknowledgement and response

Administrator: Adam Donovan

Acknowledged: 13 September 2026, 1720 AEST

Alert: Repeated Employee WiFi Management Blocks

Source: 192.168.11.100 — HQ-EMP-LAPTOP

Observed count: 19 matching blocked events within five minutes.



Investigation: Reviewed the Grafana alert and associated firewall logs. Confirmed that the events corresponded to the authorised ping test from the employee WiFi laptop to management address 192.168.99.1. The test received no replies, and the firewall recorded the blocked traffic.


Response: Stopped the test traffic and retained the firewall rule. No device isolation or escalation was required because this was an authorised test with an identified source and purpose.


Outcome: Received the firing and resolved notifications. Grafana returned to Normal through its configured NoData handling after the matching events left the query window. Screenshots were retained as test evidence.


Disposition: Closed as an authorised security validation test.
