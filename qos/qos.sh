#!/bin/bash

interface = $1
ipsrc = $2
ipdst = $3
velocidadeDownload = $4
velocidadeUpload = $5
  
#Aqui criamos um classe principal com um determinado bitrate
sudo tc class add dev $interface parent 1:0 classid 1:1 htb rate $criarVariavelParaAVelocidadeQueQueremosNaClasse #A classe chama-se 1:1

#Criar as classes que vão controlar as larguras de banda, estás classes estão associadas à classe de cima no parente 1:1, que é como se chama a classe de cima
#rate = capacidade de banda alocada
#ceil = total de banda que podem pedir às outras classes quando estão subcarregados
sudo tc class add dev $interface parent 1:1 classid 1:10 htb rate 10mbit ceil 5mbit
sudo tc class add dev $interface parent 1:1 classid 1:20 htb rate 250kbit ceil 100kbit 

#Aplicar os filtros com as classes que queremos
#parent tem de ser o número da classe principal e depois no flowid o número da classe que queremos associar
#NOTA: Upload não estou a conseguir controlar
sudo tc filter add dev $interface parent 1: protocol all u32 match ip src $ipsrc flowid 1:1
sudo tc filter add dev $interface parent 1: protocol all u32 match ip dst $ipdst flowid 1:2 #destino é que bloqueia o download 

#Para elimiar um filtro
sudo tc filter del dev $interface parent 1:0

tc filter del dev <device> pref <priority> handle <filterhandle> <filtertype>
sudo tc filter del dev wlan0 pref 49152 handle 800::800 u32