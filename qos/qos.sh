#!/bin/bash

interface = $1
ipsrc = $2
ipdst = $3
velocidadeDownload = $4
velocidadeUpload = $5
  
#Aqui criamos um classe principal com um determinado bitrate
sudo tc class add dev $interface parent 1:0 classid 1:1 htb rate $criarVariavelParaAVelocidadeQueQueremosNaClasse #A classe chama-se 1:1

#Criar as classes que vão controlar as larguras de banda, estás classes estão associadas à classe de cima no parente 1:1, que é como se chama a classe de cima
sudo tc class add dev $interface parent 1:1 classid 1:10 htb rate 10mbit ceil 5mbit
sudo tc class add dev $interface parent 1:1 classid 1:20 htb rate 250kbit ceil 100kbit

#Aplicar os filtros com as classes que queremos
sudo tc filter add dev $interface parent 1: protocol all u32 match ip src $ipsrc flowid 1:1
sudo tc filter add dev $interface parent 1: protocol all u32 match ip dst $ipdst flowid 1:2

#Vincular o tráfego às filas 
iptables –t mangle –A FORWARD –p tcp --sport 80 –i eth0 –j CLASSIFY --set-class 1:10
iptables –t mangle –A FORWARD –p tcp --sport 443 –i eth0 –j CLASSIFY --set-class 1:10
Iptables –t mangle –A FORWARD –p tcp --sport 25 –i eth0 –j CLASSIFY --set-class 1:20
Iptables –t mangle –A FORWARD –p tcp --sport 110 –i eth0 –j CLASSIFY --set-class 1:20

Iptables –t mangle –A FORWARD –p tcp -s 192.168.1.23 –i eth0 –j CLASSIFY --set-class 1:20 #Com IP
Iptables –t mangle –A FORWARD –p tcp -d 192.168.1.23 –i eth0 –j CLASSIFY --set-class 1:20 #Com IP

#Para elimiar um filtro
sudo tc filter del dev $interface parent 1:0