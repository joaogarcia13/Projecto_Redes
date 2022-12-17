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

#falta apanhar erros
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker build docker build -t dchp . 
docker run dhcp

docker build docker build -t hostapd . 
docker run hostapd



