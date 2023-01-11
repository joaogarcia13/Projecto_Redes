#!/bin/bash

if [ $2 = "null" ];
then
    sudo ufw route deny in on $1 to any
elif [ $2 = "port" ];
then
    sudo ufw route deny in on $1 to any port $3
else
    sudo ufw route deny in on $1 to $3
fi