COIT13236: Cyber Security Project (HT2, 2026) 

Project Proposal  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Team members: 

Adam Donovan – S0257097 

Jared Williams – 12239748 

Duane Van Itallie – Q9602377 

 

 

 

​​Project background and justification:	2 

​Problem statement and project objectives:	3 

​Current Infrastructure	3 

​Project Objectives and Scope	3 

​Innovative aspects of the proposed solution:	4 

​Project scope, assumptions, and constraints:	5 

​High-level requirements overview:	6 

​Work decomposition:	6 

​Delivery roadmap:	7 

​Risk identification and mitigation plan:	9 

​Quality considerations:	10 

​Team structure, roles, and responsibilities matrix:	10 

​Task leads for major deliverables:	11 

​Required tools and resources:	12 

​References:	13 

​​ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Project background and justification:  

Client – PrimeCore Minerals 

Locations – HQ Brisbane City, 4 site Offices at mine site 

Total Staff - ~600 including contractors/sub-contractors/visitors etc. 

Platform – EVE-NG (virtualised) 

Track – Network-led + Security 

Standards – Essential 8, ISO 27001 

Lead in units – VM, NET, NETSEC, SYSADMIN, CLOUD, WIRELESS 

 

PrimeCore Minerals is a fictional mining company with a city headquarters, four mine-site offices, approximately 600 staff, and a changing population of contractors and visitors. Its existing flat networks provide insufficient separation between trusted and untrusted users, limited visibility of security events, and weak resilience to link failure. This proposal recommends a scalable two-site proof-of-concept that can be extended to additional mine-site offices. 

The proposed solution uses segmented employee, visitor/contractor, and management networks; stateful firewall controls; encrypted inter-site connectivity; centralised logging and monitoring; and identity-based access for employee services. The project will demonstrate that permitted traffic succeeds, unauthorised cross-segment traffic is blocked and logged, and the design can be operated as a repeatable template. 

 

 

Problem statement and project objectives: 

Current Infrastructure 

Currently PrimeCore Minerals (PCM) operates a "Flat Network" at main office and all site offices each with independent internet connections. PCM are in the primary steps to upgrade and expand operations and will need a modern, scalable and secure network to cover existing sites and staff as well as the inclusion of possible future staff, on-site contractors and visiting staff as well as keeping the network secure against unplanned downtimes and unauthorized network access. 

 

The current problems faced by the company are; 

 

Employees, contractors, visitors, printers, and other devices share flat networks with no effective isolation. 

Visitors require internet access but must not be able to reach internal systems 	or management interfaces. 

The city office and mine sites require secure, scalable inter-site connectivity. 

Mine-site conditions create practical resilience risks, including unreliable links and wireless interference. 

The organisation needs evidence of policy enforcement through logging and monitoring. 

 

 

Project Objectives and Scope 

The objective for the project is to provide an upgraded network solution to PrimeCore Minerals current flat network design and enhance their security by separating users and controlling the access to internal systems, reliability by implementing a redundant backup connection with failover for network outages and allowing additional mine site offices and users to be added in the future to improve scalability. 

Connections between different locations across the network will also be secure and utilise centralised monitoring and logging providing the IT team with the ability to identify and investigate network problems and suspicious activity so they can respond promptly.  

 

Minimum Viable Product 

Outcome 

Evidence of completion 

Two routed sites 

HQ and Mine-Site A operating in the virtual lab. 

Network segmentation 

Employee, visitor/contractor, and management VLANs at each site. 

Firewall enforcement 

Documented allow/deny rules with denial logging. 

Secure visitor access 

Internet access works while internal destinations are blocked. 

Identity and monitoring 

Employee access control proof plus central syslog/monitoring evidence. 

Live demonstration 

Permitted and denied traffic tests with captured results. 

 

 

Dual-link or site-to-site VPN failover demonstration. 

Network Access Control using 802.1X and RADIUS. 

Ansible configuration templates for repeatable deployment. 

Simulated lateral-movement attempt, detection, and remediation walkthrough. 

 

To keep the project achievable, the MVP is limited to two sites. The team will only attempt stretch goals after the MVP acceptance tests pass. 

 

 

Innovative aspects of the proposed solution: 

This project will provide PrimeCore Minerals with a network structure that is more flexible and secure than their current flat network by  

Standard firewall and encryption settings throughout the network 

Reducing the outward-facing network connections between the company and the internet. 

This reduces the potential entry threats into the company infrastructure. 

Reduces ISP costs 

New offices can be added at the site without requiring a new ISP setup and router configuration and security setup and costs. 

Faster connections to server for site staff 

As the server and the users are using LAN connections instead, the network speed and latency will improve 

Network infrastructure easier to configure, monitor and log 

The IT team will have a cleaner picture of the network and can locate and act accordingly for any issues that arise. 

 

 

Project scope, assumptions, and constraints: 

The lab will be hosted in virtual machines, using EVE-NG as the network emulation platform. The topology will model a city headquarters and a mine-site office. Each site will contain an edge firewall/router, a switching layer, endpoints for employee and visitor traffic, and representative internal services. HQ will host the RADIUS, syslog, and monitoring services.  

 

The porject assumes the EVE-NG lab along with both virtual and physical devices will remain available during the development of the network. It also assumes the will have the resources needed to complete the any testing or documentation.  

 

The project is constrained by the time availble to the team throughout the term. To keep the workload realistic, the MVP will focus on two sites within the EVE-NG enviroment. Stretch goals will be considered once the main MVP requirements have been completed and tested. 

 

VLAN 

Purpose 

Example subnet at HQ 

10 - Employee 

Staff workstations and internal services 

192.168.1.0/24 

20 - Visitor 

Contractor and guest devices; internet only 

192.168.2.0/24 

99 - Management 

Administration of network infrastructure 

192.168.99.0/24 

  

Traffic path 

Policy 

Employee to approved services and internet 

Allow after authentication. 

Visitor to internet 

Allow web and DNS traffic only. 

Visitor to employee or management networks 

Deny and log. 

Employee to visitor or management networks 

Deny and log unless an approved administration exception exists. 

Management network to infrastructure 

Allow for authorised administrators only. 

 

 

 

 

High-level requirements overview:  

To ensure the PrimeCore network meets the security and operational requirements for all uses including the daily users (staff), management and IT team the following requirements have been identified and must be met  

 

Network Separation: We must separate employees, contractor and visitor network traffic to protect against unauthorised access to internal systems and sensitive company data. This allows guest devices to access online services easily while being blocked from accessing restricted network resources. 

Secure site connectivity: The Brisbane headquarters and mine sites must be connected through an encrypted tunnel to prevent malicious activity, such as man-in-the-middle (MitM) attacks, while company data travels between locations.  

Network access control: Firewall rules should be configured to secure any traffic travelling between different segments of the network. Setting up these clear rules ensures devices and accounts trying to cross over to another segment of the network must be authorised.  

Network monitoring and logs: Activity on the network must be recorded and monitored centrally. This provided the IT team a way to identify suspicious behaviour, investigate breaches and narrow down system failures.  

Data backup and recovery: The network should allow for easy backup and recovery steps for essential system data and network configurations so important information and services can be restored after a malicious attack or system failure. 

Traffic prioritisation: During periods of high network traffic, important business traffic should be prioritised to prevent communications from slowing down.  

 

 

Work decomposition:  

The PrimeCore Minerals Secure Multi-Office Network Project has been divided into eight phases to maintain a clearer structure from the planning through to the design, implementation and final demonstration.  

Phases 

Main task 

 

Phase 1 

 

Planning the project requirements, scope and MVP, risk assessment, organising resources and assigning responsibilities. 

Phase 2 

 

Designing network structure such as, VLAN structure, network separation and firewall, failover and traffic prioritisation. 

Phase 3 

 

EVE-NG setup, network construction, VLANs, routing, site connectivity and basic connectivity testing. 

Phase 4 

 

Setting up the firewall rules, user authentication, monitoring, logging and other security features for the network. 

Phase 5 

 

Site-to-site VPN, failover, traffic prioritisation and reliability testing. 

Phase 6 

 

Conducting security and network testing, troubleshooting and repeat testing. 

Phase 7 

 

Optional additional features such as NAC or automation, simulated attack and remediation testing, and evaluate the completed stretch goals. 

Phase 8 

 

Final documentation, testing, review, demonstration and submission 

 

Each phase is broken down into smaller tasks and assigned to a team member as the task lead. It is that members responsibility to complete their assigned tasks. Dependencies are also included so that tasks which rely on earlier configuration or design work are completed in the correct order. 

 

 

Delivery roadmap:  

The delivery roadmap was created using Microsoft Project and showcases how the project will develop over the duration of the term, each task is organised into phases and each phase is planned around the work that must be completed including an order and timing for each task.   

 

 

 

 

 

 

Risk identification and mitigation plan:  

The design applies defence in depth: logical segmentation, default-deny firewall policy, authenticated employee access, encrypted inter-site traffic, restricted management access, and centralised evidence collection. The proposal maps most directly to Essential Eight practices for restricting administrative privileges, patching systems, MFA for administration, and regular configuration backups. It also supports ISO/IEC 27001 network security, logging, access control, and secure information-transfer objectives. 

 

Risk 

Impact 

Mitigation 

Scope creep 

MVP is not completed 

Lock MVP to two sites and defer stretch goals. 

Lab resource limits 

Slow or unstable simulation 

Use lightweight images; snapshot VMs; build incrementally. 

Misconfiguration 

Security controls fail 

Peer review changes and use acceptance tests. 

Single service failure 

Authentication or logging unavailable 

Document a fallback procedure; consider a secondary service as stretch work. 

Wireless interference 

Unreliable access in real deployment 

Document 5 GHz preference, channel survey, and wired fallback. 

 

 

Quality considerations:  

Throughout the project the team will maintain a consistent standard of quality by following a structured process when documenting changes and issues, testing features, discussing revisions and providing feedback. Essential settings, configurations and architecture decisions will be reviewed by the supporting team member related to that deliverable to provide feedback before implementing the feature to the EVE-NG virtual network. The team member implementing the feature will then test the implemented feature to verify it functions as expected and satisfies its intended operational purpose.  

 

Testing will be an ongoing step throughout the development of the project rather than postponing until the final stage. After each major feature is implemented in the EVE-NG environment, the team member will ensure the feature performs correctly, meets the intended design criteria and works in unison with the existing network configuration. Any problems encountered will be documented, resolved and re-tested. If the problem persists, the supporting team member will be notified to review the issue and provide feedback. 

 

Before delivering the final network demonstration, the team will compare the completed network against the guidelines from the Essential Eight and ISO 27001 cybersecurity frameworks. This will be used to verify the security controls implemented and make any final changes before submission. Additionally, the team will conduct a final review of the project MVP and scope requirements to verify all the planned tasks have been completed and tested. 

 

 

 Team structure, roles, and responsibilities matrix:  

The project is deliberately structured as a group deliverable. Each person owns an independently reviewable technical output and contributes evidence to the final report. 

 

Team member and role 

Primary responsibility 

Contribution evidence 

Adam - Project Lead, Infrastructure and Repository Manager 

Writes and maintains the project proposal; builds and maintains the Proxmox/EVE-NG virtual lab; manages snapshots, controlled remote access, GitHub, project integration, and submission coordination. 

Proposal history; VM build notes; snapshot and remote-access record; GitHub activity; final integration checklist. 

Duane - Network Architect 

Designs the topology, VLANs, IP addressing, routing, switching, and network-device configurations; peer reviews the lab build. 

Topology and addressing diagrams; device configurations; routing and VLAN validation evidence. 

Jared - Security and Validation Lead 

Designs firewall controls and secure remote access; configures or validates logging and monitoring; owns the test matrix, evidence capture, and demo script. 

Firewall rule set; log/monitoring evidence; completed acceptance tests; demo run sheet. 

 

The group will hold a short weekly check-in, maintain a shared task board, store configurations in version control, and peer-review configuration changes before they are merged into the lab. Every member will contribute both an assigned technical output and documentation or testing evidence. 

 

 

Task leads for major deliverables:  

Deliverable 

Task lead 

Supporting Team Member 

Project proposal and project planning 

 

Adam 

Jared, Duane 

Network topology design  

 

Duane 

Jared 

EVE-NG virtual environment setup 

 

Adam 

Duane 

 

Firewall rules and network segmentation  

 

Jared 

Duane  

VLAN, Routing and IP addressing configuration 

 

Duane 

 

Adam 

Authentication and user access 

Adam 

Jared 

 

Monitoring and logging 

 

Adam 

Jared 

Site to site VPN failover  

 

Jared 

Duane 

Traffic prioritisation 

 

Jared 

Duane 

Network testing 

 

Jared 

Adam, Duane 

Optional NAC or automation 

 

Duane 

Adam 

Attack simulation and remediation 

 

Jared 

Duane 

Final report documentation 

 

All 

 

Final presentation and demonstration 

 

All 

 

 

 

Required tools and resources:  

Quality will be managed through traceability, review, testing, and evidence capture. Every MVP requirement will map to a configuration artefact, test case, and result. Changes will be made through version control, peer reviewed by a second team member, and tested in an isolated lab snapshot before integration. A defect register will record severity, owner, corrective action, and retest outcome. 

 

Quality control 

Method and acceptance standard 

Requirements traceability 

Each requirement maps to a design decision, configuration item, test case and evidence file. 

Configuration quality 

Peer review before deployment; version-controlled backups; documented rollback from snapshot. 

Security validation 

Default-deny policy tested with both allowed and blocked flows; blocked flows must be logged. 

Demo quality 

Repeatable script with known starting state, expected outcomes and contingency steps. 

Documentation quality 

Team proofreads against rubric, Harvard style, and final evidence checklist before submission. 

  

 

 

Resource 

Purpose / owner 

Proxmox home server 

Hosts the virtual lab; owner maintains remote access, backups and snapshots. 

EVE-NG and network images 

Emulates routers, switches and firewall appliances. 

Linux service VMs 

RADIUS, syslog and monitoring services using synthetic project data. 

Tailscale or equivalent private VPN 

Controlled remote access for group members without exposing management services publicly. 

Version control and shared workspace 

Configuration history, task allocation, review and evidence storage. 

Team skills 

Networking, firewall policy, Linux administration, testing, technical writing and presentation. 

 

 

References: 

Australian Signals Directorate 2023, 'Essential Eight explained', Australian Cyber Security Centre, Australian Government, viewed 2 August 2026, https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-explained  

 

International Organization of Standardization 2022, ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection – Information secuirty management systems - Requirements, International Organization for Standardization, viewed 3 August 2026, https://www.iso.org/standard/27001 

  
