#!/bin/bash

interface = $1
ipsrc = $2
ipdst = $3
velocidadeDownload = $4
velocidadeUpload = $5
  
sudo tc class add dev $interface parent 1:0 classid 1:1 hfsc sc rate $velocidadeDownload ul rate $velocidadeUpload #temos de ter cuidado com o que é introduzido
sudo tc filter add dev $interface parent 1: protocol all u32 match ip src $ipsrc flowid 1:1
sudo tc filter add dev $interface parent 1: protocol all u32 match ip dst $ipdst flowid 1:2

#Para elimiar um filtro
sudo tc filter del dev $interface parent 1:0