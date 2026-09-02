Switch name - PCM-SITE-OFFICE-SITE-A
open vSwitch installed

LAN switch template:

# switch PCM-MINE-SITE-A
# 8-port switch with port names ranging from ens3-ens10
#
#
#
# set the name of the server
sudo hostnamectl set-hostname 'host-name-of-server'
sudo nano /etc/hosts
#	enter hostname into file
#
#
# set the timezone to be UTC+9.5 QLD-AUS timezone
sudo timedatectl set-timezone Australia/Brisbane
#
#
# create the main OVS bridge
ovs-vsctl add-br br0
#
#
# create LAN trunk and assign it to physical interface (last port on switch)
ovs-vsctl add-port br0 ens10 trunks=10,11,20,30,40,41,50,90,91,99
# replace X with the port number connecting to the router. remove vlan numbers if they aren't required in that office.
#
#
# assign vlan to specific port on switch
ovs-vsctl add-port br0 ens'X' tag=10 
# X is the port number on the switch and number 10 is the vlan number. change it if a different vlan is being tied to that port
#
#
# set admin password
ovs-vsctl set Open_vSwitch . other_config:passwd="Coit13236"
#
#
# show configuration
ovs-vsctl show
#



<img width="842" height="252" alt="image" src="https://github.com/user-attachments/assets/e51a0f44-34ff-45c0-8fe5-603e9a51e495" />

