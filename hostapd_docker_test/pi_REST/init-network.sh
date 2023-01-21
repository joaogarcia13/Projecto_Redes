ifconfig wlan0 192.168.201.1/24 up
#iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables-nft -t nat -C POSTROUTING -o eth0 -j MASQUERADE && iptables-nft -t nat -D POSTROUTING -o eth0 -j MASQUERADE
iptables-nft -C FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT && iptables-nft -D FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables-nft -C FORWARD -i wlan0 -o eth0 -j ACCEPT && iptables-nft -D FORWARD -i wlan0 -o eth0 -j ACCEPT
dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'
