#!/bin/bash

cpu=$(vmstat 1 2|tail -1|awk '{print $15}')
temp=$(cat /sys/class/thermal/thermal_zone*/temp)
mem=$(grep MemTotal /proc/meminfo)
info="$cpu|$mem|$temp"
echo $info
