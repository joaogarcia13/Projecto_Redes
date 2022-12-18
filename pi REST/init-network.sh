ifconfig wlan0 192.168.254.0/24 up
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'

