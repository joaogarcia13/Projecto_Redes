if [$# -eq 1];
then
    sudo tc filter del dev $1
else
    tc filter del dev $1 pref $2 handle $3 $4
fi
