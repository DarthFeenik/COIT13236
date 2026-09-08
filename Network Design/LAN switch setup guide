	1. Add Linux node and change image. Assign correct number of LAN ports and make sure link is VNC
	2. Place near router and connect to a port that has only 1 vlan on it.
		a. Later it will be turned off and connected to the correct port as it will be a trunk port
	3. Turn on switch and log in
	4. Change the switch hostname by running: sudo hostnamectl set-hostname new-server-name (write hostname on LAN port layout spreadsheet)
	5. Place the hostname in the hosts file by running: sudo nano /etc/hosts
	6. Run: Hostnamectl
	7. Set timezone to be Brisbane time by running: sudo timedatectl set-timezone Australia/Brisbane
	8. Run: sudo apt update and upgrade until OS is up to date
	9. Run: sudo apt install -y openvswitch-switch
	10. Run: sudo nano /etc/netplan/00-installer-config.yaml
		a. Make sure it only has the following in it
		  network:
		    version: 2
		    renderer: networkd
	11. Save file (Ctrl+o --> Enter --> Ctrl+x)
	12. Run: sudo netplan apply
	13. Reboot switch
	14. Run sudo ovs-vsctl add-br br0
	15. Confirm it's running by running: sudo ovs-vsctl show
	16. Confirm port numbers on switch by running: ip a
		a. Ens3 is normally port0, ens4 will be port1 etc.
Have assigned ports and what they are connecting to written in the LAN Port Layout spreadsheet)
	17. For ports with a single vlan, run: sudo ovs-vsctl add-port br0 ensX tag=Y (where X = port number and Y = vlan number)
	18. For ports that will be trunks, run: sudo ovs-vsctl add-port br0 ensX trunks=Y,Y,Y… (where X = port number and Y vlan numbers)
	19. Confirm command has taken by running: sudo ovs-vsctl show
		a. Eg. Ens3 --> tag:10; ens4 --> tag:11; etc.
	20. Run: Sudo ovs-vsctl add-port br0 vlan99 tag=99 -- set interface vlan99 type=internal
	21. Run: sudo ip link set vlan99 up
	22. Run: sudo ip addr add 192.168.YY.ZZZ/24 dev vlan99 (where YY = IP octet associated with vlan and ZZZ is the device IP address)
	23. Test network is working by running: ping 192.168.99.2 OR 192.168.199.2 (if from mine site)
The commands above setup vlan99 and assign IP address to device however the following commands are needed to make it permanent so switch can be restarted without it loosing it's IP address or settings.
	19. Run: sudo nano /etc/systemd/network/vlan99.network
	20. Setup the file with the following config:
		[Match]
		Name=vlan99
		
		[Network]
		Address=192.168.YY.ZZZ/24
		Gateway=192.168.YY.1
		DNS=192.168.YY.1
		DNS=8.8.8.8
	Save and exit the config file (save by going Ctrl+o --> Enter --> Ctrl+x)
	21. Run: sudo systemctl enable systemd-networkd
	22. Run: sudo systemctl restart systemd-networkd
	23. Reboot server
	24. Ping gateway, 8.8.8.8, 1.1.1.1 and google.com to confirm network is working
