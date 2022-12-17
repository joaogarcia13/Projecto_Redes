#!/bin/bash

ifconfig wlan0 $1/24 #pedir mascara 

echo "
subnet "$2" netmask 255.255.255.0 {
   range "$3" "$4";
   option routers "$1";
   option domain-name-servers 192.168.227.20;
}
" > dhcpd.conf #adicionar a string as subnets
#definir dns mais tarde possivelmente hipoteticamente quem sabe

#kill hostapd e dhcp
/usr/sbin/hostapd hostapd.conf
ifconfig wlan0 $1/24 up
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
dhcpd -cf dhcp.conf wlan0

#falta apanhar erros
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker build docker build -t dchp . 
docker run dhcp

docker build docker build -t hostapd . 
docker run hostapd
