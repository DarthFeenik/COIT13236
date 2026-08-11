# COIT13236
## CQU Project 2026, Term 2

# PD-1 Secure Multi-Office Network at a Mine Site

## Project Overview

| Field         | Details                                      |
| ------------- | -------------------------------------------- |
| Client        | PrimeCore Minerals                           |
| Sites         | Brisbane HQ + 4 Mine-Site Offices            |
| Users         | ~600 staff, contractors and visitors         |
| Platform      | EVE-NG                                       |
| Track         | Network-led + Security                       |
| Standards     | Essential Eight, ISO/IEC 27001               |
| Lead-In Units | VM, NET, NETSEC, SYSADMIN, CLOUD, WIRELESS   |

## The Problem

PrimeCore Minerals currently operates flat networks at its Brisbane headquarters and mine-site offices, with each site using independent internet connections. As the company expands, the existing network does not provide sufficient security, scalability or resilience for additional employees, contractors and visitors.\

The current network creates multiple problems:
-
-
-
-

## Minimum Viable Outcome (MVP)

* [ ] Two fully built and routed sites: Brisbane HQ and Mine-Site Office A
* [ ] Network segmentation using Employee, Visitor/Contractor and Management VLANs
* [ ] Firewall rules enforcing cross-segment policies
* [ ] Visitor network with internet access only
* [ ] Employee login and access control
* [ ] Live demo: permitted vs. denied cross-segment traffic (denied paths logged)
* [ ] Centralised monitoring and logging

## Stretch Goals

* [ ] Site-to-Site (S2S) VPN with failover
* [ ] Network Access Control (NAC) using 802.1X / RADIUS
* [ ] Traffic prioritisation and QoS
* [ ] Ansible-based configuration management
* [ ] Simulated attack scenario + remediation walkthrough

# Architecture

## Traffic Segments

| Segment            | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| Employee VLAN 10   | Staff workstations and access to approved internal services       |
| Visitor VLAN 20    | Contractors and visitors with internet-only access                |
| Management VLAN 99 | Restricted administration of routers, switches and firewalls      |
| Internal Services  | RADIUS, syslog, monitoring and other approved company services    |

## Capability Menu

| Capability                    | Priority             |
| ------------------------------ | -------------------- |
| Network Segmentation          | Basic (B)            |
| Firewall / IDS                | Basic (B)            |
| Identity and Access Management | Advanced (A)         |
| Monitoring and Logging       | Basic (B)             |
| VPN / High Availability       | Advanced/Basic (A/B) |

# Technology Stack

- Network Emulator: EVE-NG
- Virtualisation Environment: Proxmox / Virtual Machines
- Network Security: Stateful firewall and VLAN segmentation
- Authentication: RADIUS / 802.1X
- Monitoring and Logging: Centralised Syslog and Network Monitoring
- Secure Site Connectivity: Site-to-Site VPN
- Automation: Ansible (stretch goal)
- Compliance Frameworks: Essential Eight, ISO/IEC 27001








