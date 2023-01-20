#!/bin/bash

if [ $2 = "null" ];
then
    ufw route delete deny in on $1 to any
elif [ $2 = "port" ];
then
    ufw route delete deny in on $1 to any port $3
else
    ufw route delete deny in on $1 to $3
fi
