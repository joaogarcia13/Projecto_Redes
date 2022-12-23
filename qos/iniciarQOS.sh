#!/bin/bash

interface = $1

sudo tc qdisc add dev $interface root handle 1:0 htb default 30 #falta escolhermos qual é a classe que vamos utilizar
