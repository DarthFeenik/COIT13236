# Ubuntu Installation on to EVE-NG
* Please Note: Some of the image files use have incorrect linux directories. Follow the text instructions for proper installation of linux server and desktop.


# Ubuntu Server

* Download the .iso for Ubuntu Server
* Use WinSCP to copy the files onto EVE Prime-Core network

<img width="1370" height="704" alt="image" src="https://github.com/user-attachments/assets/c600c70a-dcdd-45b4-ba0d-8d0d548f9711" />

<img width="925" height="265" alt="image" src="https://github.com/user-attachments/assets/88f79945-fdd0-4d45-ae6c-7e99dda08911" />


* SSH into Prime-Core (The VM network on EVE-NG)

* Make the directory for the linux server
* Make sure the directory starts with "linux-" or EVE-NG wont recognise it

mkdir -p /opt/unetlab/addons/qemu/linux-ubuntu-server-26.04
  mkdir -p /opt/unetlab/addons/qemu/ub-server

Move the ubuntu server iso to the created directory
  mv ubuntu-26.04-live-server-amd64.iso /opt/unetlab/addons/qemu/linux-ubuntu-server-26.04/

<img width="1053" height="155" alt="image" src="https://github.com/user-attachments/assets/1325b03f-7d47-4a14-ae94-39c62a4adc25" />

Then follow these steps to run the installer;

* Change into ubserver directory - cd /opt/unetlab/addons/qemu/linux-ubuntu-server-26.04/
* Rename the iso installer to "cdrom.iso" - mv ubuntu-26.04-live-server-amd64.iso cdrom.iso
* Create a 30GB disk - /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 30G
* Fix permissions - /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
* Check the steps have worked - ls -lh

<img width="1388" height="239" alt="image" src="https://github.com/user-attachments/assets/e5a8b533-1acf-428f-bbcd-fee5986f535f" />

# Install Ubuntu Server on EVE-NG

## Ubuntu Server Config

| Name:  | PC-SRV-LNX-1 |
| Image:  | linux-ubuntu-server-24.04.4 |
| CPU:    | 2 |
| RAM:    | 4096 MB |
| Ethernet:  | 1 |
| Console:    | VNC |










# Ubuntu Desktop

* Follow previous steps to get the .iso file on to EVE

* SSH into Prime-Core (The VM network on EVE-NG)

* Make the directory for the linux desktop

  mkdir -p /opt/unetlab/addons/qemu/linux-ubuntu-desktop-26.04

Move the ubuntu server iso to the created directory
  mv ubuntu-26.04-desktop-amd64.iso /opt/unetlab/addons/qemu/linux-ubuntu-desktop-26.04/

Then follow these steps to run the installer;

* Change into ubserver directory - cd /opt/unetlab/addons/qemu/linux-ubuntu-desktop-26.04/
* Rename the iso installer to "cdrom.iso" - mv ubuntu-26.04-desktop-amd64.iso cdrom.iso
* Create a 40GB disk - /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 40G
* Fix permissions - /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
* Check the steps have worked - ls -lh

<img width="1402" height="318" alt="image" src="https://github.com/user-attachments/assets/087d6ba7-8be8-4182-b62c-49f0fbb52f31" />





