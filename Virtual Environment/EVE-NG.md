# EVE-NG Community Version

## Installing EVE-NG on Proxmox

Proxmox

└── EVE-NG VM

    ├── HQ router/firewall
    
    ├── Mine-site router/firewall
    
    ├── HQ managed switch
    
    ├── Mine-site managed switch
    
    ├── Server (Ubuntu)
    
    ├── HQ client(s)
    
    └── Mine-site client(s)
    

EVE-NG VM Settings

Name: eve-ng
ISO: EVE-NG Community
OS type: Linux
Disk: 80 GB 
CPU: 4 8
RAM: 16GB
Network: vmbr0, model VirtIO
CPU type: host


Run EVE-NG VM on Proxmox

Connect to EVE-NG IP Address (192.168.1.186)


## Installing pfsense

* Download the pfsense installer - netgate-installer-v1.2-RELEASE-amd64.iso
* SSH in to EVE to create a directory - mkdir -p /opt/unetlab/addons/qemu/pfsense-2.8
* Use WinSCP to transfer the iso in to EVE - /opt/unetlab/addons/qemu/pfsense-2.8/
* Change directory to - cd /opt/unetlab/addons/qemu/pfsense-2.8/
* Move the iso installer and rename it - mv netgate-installer-v1.2-RELEASE-amd64.iso cdrom.iso
* Now create the VM giving it 10GB - /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 10G
* Fix permissions for EVE - /opt/unetlab/wrappers/unl_wrapper -a fixpermissions


Now use the web browser to connect to EVE to add pfsense node in to the virtual network.

## pfsense configuration

* Name:        PC-FW-1
* Image:       pfsense-2.8
* CPU:         2
* RAM:         4096 MB
* Ethernet:    4
* Console:     VNC

## VNC Client

Chrome wont play nice with the VNC so need to install a dedicated program.

I installed TightVNC to SSH in to pfsense to install it.

192.168.1.198
       │
       │ TCP 32769 ✓
       ▼
EVE-NG 192.168.1.186
       │
       ▼
QEMU VNC server ✓
       │
       ▼
PC-FW-1 / pfSense
