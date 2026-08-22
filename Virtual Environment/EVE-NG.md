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

EVE-NG Pfsense settings

| Name | PC-FW-1 |
| Image | pfsense-2.8 | 
| CPU | 2 |
| RAM | 4096MB |
| Console | VNC |

Connect to pfsense using TightVNC

* 192.168.1.186::32769

<img width="427" height="308" alt="image" src="https://github.com/user-attachments/assets/e8ab14ed-2e8d-4da3-b760-10cb768ee5df" />

<img width="715" height="400" alt="image" src="https://github.com/user-attachments/assets/929df5d5-b720-4697-924f-44c1a9de5b54" />

<img width="719" height="402" alt="image" src="https://github.com/user-attachments/assets/2d95ee9a-44bd-45fd-b27a-63f42139c888" />

<img width="731" height="412" alt="image" src="https://github.com/user-attachments/assets/91015c06-dd5d-45cb-a7e9-f1827be7d7f8" />

<img width="730" height="411" alt="image" src="https://github.com/user-attachments/assets/bb863244-ead6-4c89-866a-32e3d4180eab" />

<img width="730" height="412" alt="image" src="https://github.com/user-attachments/assets/8a87b1d3-d72c-44b1-9f38-04666787f1fd" />

<img width="729" height="412" alt="image" src="https://github.com/user-attachments/assets/53225b37-3d48-42cc-8623-c5915b66a61d" />

<img width="736" height="415" alt="image" src="https://github.com/user-attachments/assets/8b50f334-44f4-424d-9c73-bf0048c955ab" />

<img width="737" height="414" alt="image" src="https://github.com/user-attachments/assets/253b2e08-243a-4149-a1b5-cebdbb8dcada" />

<img width="730" height="413" alt="image" src="https://github.com/user-attachments/assets/b0951549-312d-4849-8408-bfd3c5ccd849" />

<img width="730" height="415" alt="image" src="https://github.com/user-attachments/assets/756d7d43-df3a-464c-a01b-32c4d3de8dfc" />

<img width="728" height="414" alt="image" src="https://github.com/user-attachments/assets/441f7acc-a4de-4f9e-88b0-5eeb01caf132" />

<img width="736" height="413" alt="image" src="https://github.com/user-attachments/assets/87c33ea5-ad00-4cf3-9169-754471d7c283" />

<img width="710" height="390" alt="image" src="https://github.com/user-attachments/assets/707a6d35-ccf2-4bc5-baa5-e256bcfb5892" />

<img width="728" height="412" alt="image" src="https://github.com/user-attachments/assets/4c0fd5dd-e89d-4704-b58d-dd468a75c5c5" />





