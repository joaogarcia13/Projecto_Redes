#!/bin/bash

interface = $1

sudo tc qdisc add dev $interface root handle 1:0 hfsc default 1 #falta escolhermos qual é a classe que vamos utilizar
