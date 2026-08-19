# Physical Server

# Server Specifications

* Device - Dell Precision Tower T5810
* CPU - Intel Xeon E5
* RAM - 64GB DDR4 ECC RAM
* SSD - RAID 0 500GB

# Remoted Access to Proxmox

## Need Tailscale account

Download and sign in to the Tailscale app. Then use a web browser to connect to the proxmox server

# Proxmox Server

Proxmox V 9.2.10 installed
IP Address - 100.81.36.41:8006

# Users

## Adam Donovan

Username - adam

Password - F*****

## Jared Williams

Username - jared

Password - C*****

## Duane Van Italie

Username - duane

Password - C*****

# Pfsense

## Installing Pfsense on EVE-NG

* Download the iso image from pfsense.org/download
* Image name is "netgate-installer-v1.2-RELEASE-amd64.iso"
* SSH in to EVE to create a new directory
  mkdir -p /opt/unetlab/addons/qemu/pfsense-2.8
* Use WinSCP on Windows computer to upload the iso image to
  /opt/unetlab/addons/qemu/pfsense-2.8/
* 
