sudo ifconfig wlan0 192.168.200.1/24 up
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo dhcpd -cf $HOME/dhcp.conf wlan0
echo 'dhcp started'
