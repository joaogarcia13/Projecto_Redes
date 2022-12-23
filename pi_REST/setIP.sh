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
echo 'dhcp started'" > init-network.sh

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker build docker build -t dchp . 
docker run dhcp

docker build docker build -t hostapd . 
docker run hostapd

