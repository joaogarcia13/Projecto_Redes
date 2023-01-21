#!/bin/bash

echo "
default-lease-time 600;
max-lease-time 7200;

subnet $2 netmask 255.255.255.0 {
   range $3 $4;
   option routers $1;
   option domain-name-servers $5;
}
" > dhcp.conf #adicionar a string as subnets

echo "sudo ifconfig wlan0 $1/24 up
#iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables-nft -t nat -C POSTROUTING -o eth0 -j MASQUERADE || iptables-nft -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables-nft -C FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT || iptables-nft -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables-nft -C FORWARD -i wlan0 -o eth0 -j ACCEPT || iptables-nft -A FORWARD -i wlan0 -o eth0 -j ACCEPT
dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'" > pi_REST/init-network.sh

