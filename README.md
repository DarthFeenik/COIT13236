# COIT13236
## CQU Project 2026, Term 2

# AC-1 Secure Multi-Site Network for an Aged-Care Provider

## Project Overview

| Field | Details | 
| --- | --- | 
| Client | Sunhaven Care | 
| Sites | 4 Sites + ~300 staff |
| Platform | GNS3 |
| Track | Network lead + security |
| Standards | Essential 8, ISO 270001 |
| Lean-In Units | NET, NETSEC, SYSADMIN, CLOUD |

## The Problem

Sunhaven Care's network grew organically into a flat, unsegmented architecture — nurse-call systems, staff devices, resident Wi-Fi and back-office applications all share the same network. This creates serious risks to:
* Clinical availability — critical systems can be disrupted by unrelated traffic
* Resident data privacy — no separation between IoT, clinical, and corporate systems
* Security posture — no firewall enforcement, no access control, no monitoring

## Minimum Viable Outcome (MVP)

* [ ] Two fully built and routed sites
* [ ] Network segmentation (VLANs per traffic class)
* [ ] Firewall rules enforcing cross-segment policies
* [ ] Authentication enforcement (IAM)
* [ ] Network monitoring in place
* [ ] Live demo: permitted vs. denied cross-segment traffic (denied paths logged)

## Stretch Goals

* [ ] Site-to-Site (S2S) VPN with failover
* [ ] Network Access Control (NAC)
* [ ] Ansible-based configuration management
* [ ] Simulated attack scenario + remediation walkthrough

# Architecture

| Segment | Description | 
| --- | --- | 
| Clinical | Nurse call systems, medical records, clinical applications | 
| Corporate | Staff Devices, Back Office, Admin |
| Resident | Guest/Resident Wi-Fi |
| IoT | Nurse call sensors, building automation, smart devices |





