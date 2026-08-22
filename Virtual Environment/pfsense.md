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


Follow the rest of the set up in the EVE-NG virtal machine. 



