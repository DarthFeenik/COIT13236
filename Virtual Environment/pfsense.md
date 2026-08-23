# Installing Pfsense

## Upload pfsense to EVE

Download the pfsense .iso and then use WinSCP to upload it to the EVE-NG virtual machine.

The image will be called netgate-installer-v1.2-RELEASE-amd64.iso


<img width="1073" height="688" alt="image" src="https://github.com/user-attachments/assets/dd2d6859-8df0-4e11-9ccc-71413453012c" />


SSH in to EVE and the file will be there.


<img width="797" height="175" alt="image" src="https://github.com/user-attachments/assets/2f0d0fb9-397b-47c2-9edc-9f850ade2b28" />


SSH in to EVE to create a directory - mkdir -p /opt/unetlab/addons/qemu/pfsense-2.8

Move the installer from root to the pfsense folder Then change directory to the pfsense folder.

<img width="846" height="210" alt="image" src="https://github.com/user-attachments/assets/6fe4a20b-c2af-4fd0-b70b-38074d6fdad9" />



Once inside the pfsense folder, rename it to "cdrom.iso" - mv netgate-installer-v1.2-RELEASE-amd64.iso cdrom.iso


Now create the VM giving it 10GB - /opt/qemu/bin/qemu-img create -f qcow2 virtioa.qcow2 10G

Fix permissions for EVE - /opt/unetlab/wrappers/unl_wrapper -a fixpermissions

Verify the changes made inside the directory - ls -lh /opt/unetlab/addons/qemu/pfsense-2.8/


<img width="1032" height="382" alt="image" src="https://github.com/user-attachments/assets/a17e6cda-deda-4752-a726-65219e00386d" />

# EVE-NG pfsense set up

## EVE-NG 

Remote in to EVE-NG to install the pfsense .iso

## pfsense configuration

* Name:        PC-FW-1
* Image:       pfsense-2.8
* CPU:         2
* RAM:         4096 MB
* Ethernet:    4
* Console:     VNC

<img width="595" height="1120" alt="image" src="https://github.com/user-attachments/assets/4451ea10-cb2f-4a0e-837d-7bd77edffa8a" />







## VNC Client

Chrome wont play nice with the VNC so need to install a dedicated program.

I installed TightVNC to SSH in to pfsense to install it.

Connect to pfsense using TightVNC

* 192.168.1.186::32769

<img width="427" height="308" alt="image" src="https://github.com/user-attachments/assets/e8ab14ed-2e8d-4da3-b760-10cb768ee5df" />

<img width="715" height="400" alt="image" src="https://github.com/user-attachments/assets/929df5d5-b720-4697-924f-44c1a9de5b54" />

<img width="719" height="402" alt="image" src="https://github.com/user-attachments/assets/2d95ee9a-44bd-45fd-b27a-63f42139c888" />

<img width="731" height="412" alt="image" src="https://github.com/user-attachments/assets/91015c06-dd5d-45cb-a7e9-f1827be7d7f8" />

<img width="730" height="411" alt="image" src="https://github.com/user-attachments/assets/bb863244-ead6-4c89-866a-32e3d4180eab" />

<img width="730" height="412" alt="image" src="https://github.com/user-attachments/assets/8a87b1d3-d72c-44b1-9f38-04666787f1fd" />

Had to change the IP Range from 192.168.1.1 to 10.10.10.1 to stop the EVE network from clashing with my home network.

<img width="720" height="404" alt="image" src="https://github.com/user-attachments/assets/8fd8bb24-d70a-4df7-95f6-a9921fa78722" />


<img width="736" height="415" alt="image" src="https://github.com/user-attachments/assets/8b50f334-44f4-424d-9c73-bf0048c955ab" />

<img width="737" height="414" alt="image" src="https://github.com/user-attachments/assets/253b2e08-243a-4149-a1b5-cebdbb8dcada" />

<img width="730" height="413" alt="image" src="https://github.com/user-attachments/assets/b0951549-312d-4849-8408-bfd3c5ccd849" />

<img width="730" height="415" alt="image" src="https://github.com/user-attachments/assets/756d7d43-df3a-464c-a01b-32c4d3de8dfc" />

<img width="728" height="414" alt="image" src="https://github.com/user-attachments/assets/441f7acc-a4de-4f9e-88b0-5eeb01caf132" />

<img width="736" height="413" alt="image" src="https://github.com/user-attachments/assets/87c33ea5-ad00-4cf3-9169-754471d7c283" />

<img width="710" height="390" alt="image" src="https://github.com/user-attachments/assets/707a6d35-ccf2-4bc5-baa5-e256bcfb5892" />


## DO NOT SELECT REBOOT

<img width="730" height="411" alt="image" src="https://github.com/user-attachments/assets/65797d71-7724-43fa-a347-2a30ebe0d86e" />

## Select Shell to avoid install issues

If you reboot the installer without removing "cdrom.iso" from EVE it will just run the installer again and cause the pfsense installation to become corrupted.

Choose to run "Shell"

<img width="735" height="418" alt="image" src="https://github.com/user-attachments/assets/00ebc280-c9d8-4a94-ada7-30c1de839659" />


The type the command - poweroff

<img width="679" height="476" alt="image" src="https://github.com/user-attachments/assets/a81e8c93-f00b-4deb-97f9-97fcd5fe9930" />

## After pfsense installation

After pfsense has been installed SSH back in to EVE-NG

Find where the virtioa.qcow2 has been installed - find /opt/unetlab/tmp -name virtioa.qcow2 -type f -ls

<img width="1309" height="147" alt="image" src="https://github.com/user-attachments/assets/ce41b65c-baae-42bf-b3cf-020bc3c6ee15" />

Change the directory to the folder that contains the correct "virtioa.qcow2"

** NOTE - Due to previous issues there are 2 versions installed here, one with 197KB of data and one with 1.9GB of data. the larger file is the correct one.

Verify the correct image by running below commands

<img width="1800" height="433" alt="image" src="https://github.com/user-attachments/assets/89d98b10-d7c2-4443-a69d-037b243a83d7" />

Finally we need to commit the image we have installed to pfsense, then remove the installer to avoid future issues, fix the permissions for EVE-NG and verify it has all worked with no issues.


<img width="1438" height="314" alt="image" src="https://github.com/user-attachments/assets/93bf524a-26d7-49dc-aeda-102ba6211505" />


Once installation is successful and the cdrom.iso has been removed. Remote back into EVE-NG and start the firewall. The firewall should boot and then make you change the default admin password.

The new password is "coit13236"







