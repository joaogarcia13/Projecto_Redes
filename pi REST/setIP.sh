#!/bin/bash

echo "
subnet "$2" netmask 255.255.255.0 {
   range "$3" "$4";
   #option routers "$6";
   option domain-name-servers "$5";
}
" > dhcp.conf #adicionar a string as subnets

echo "ifconfig wlan0 "$1"/24 up
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
dhcpd -cf dhcp.conf wlan0
echo 'dhcp started'" > init-network.sh

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker build docker build -t dchp . 
docker run dhcp

docker build docker build -t hostapd . 
docker run hostapd

