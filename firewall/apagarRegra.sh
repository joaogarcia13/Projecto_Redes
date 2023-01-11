if [$# -eq 0]
then
    sudo ufw route delete deny in on $1 to any
else
    if [$2 == "port"]
    then
        sudo ufw route delete deny in on $1 to any port $3
    else
        sudo ufw route delete deny in on $1 to $3
    fi
fi