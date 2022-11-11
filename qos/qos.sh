#!/bin/bash

interface = $1
ipsrc = $2
ipdst = $3
velocidadeDownload = $4
velocidadeUpload = $5

iniciarQos() {
    sudo tc qdisc add dev $interface root handle 1:0 
}

aplicarNovaRegra() {

}