#!/bin/bash

if [$# -eq 1];
then
    tc filter del dev $1
else
    tc filter del dev $1 pref $2 handle $3 $4
fi
