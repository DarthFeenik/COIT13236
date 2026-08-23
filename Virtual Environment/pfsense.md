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

<img width="729" height="412" alt="image" src="https://github.com/user-attachments/assets/53225b37-3d48-42cc-8623-c5915b66a61d" />

<img width="736" height="415" alt="image" src="https://github.com/user-attachments/assets/8b50f334-44f4-424d-9c73-bf0048c955ab" />

<img width="737" height="414" alt="image" src="https://github.com/user-attachments/assets/253b2e08-243a-4149-a1b5-cebdbb8dcada" />

<img width="730" height="413" alt="image" src="https://github.com/user-attachments/assets/b0951549-312d-4849-8408-bfd3c5ccd849" />

<img width="730" height="415" alt="image" src="https://github.com/user-attachments/assets/756d7d43-df3a-464c-a01b-32c4d3de8dfc" />

<img width="728" height="414" alt="image" src="https://github.com/user-attachments/assets/441f7acc-a4de-4f9e-88b0-5eeb01caf132" />

<img width="736" height="413" alt="image" src="https://github.com/user-attachments/assets/87c33ea5-ad00-4cf3-9169-754471d7c283" />

<img width="710" height="390" alt="image" src="https://github.com/user-attachments/assets/707a6d35-ccf2-4bc5-baa5-e256bcfb5892" />

<img width="728" height="412" alt="image" src="https://github.com/user-attachments/assets/4c0fd5dd-e89d-4704-b58d-dd468a75c5c5" />



