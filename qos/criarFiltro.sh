#!/bin/bash

sudo tc filter add dev $1 parent 1:0 protocol all u32 match ip dst $2 flowid $3

prio = $(sudo tc filter show dev wlan0 | head -n 2 | awk '{print $7}' | head -n 1)
filterHandle = $(sudo tc filter show dev wlan0 | head -n 3 | awk '{print $12}' | tail -n 1)
filterType = $(sudo tc filter show dev wlan0 | head -n 2 | awk '{print $8}' | head -n 1)

info = "$prio-$filterHandle-$filterType"
echo $info