sudo ifconfig wlan0 192.168.201.1/24 up
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'
