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
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'" > pi_REST/init-network.sh

