#!/bin/bash

sudo tc class add dev $1 parent 1:1 classid $2 htb rate $3mbit ceil $4mbit

