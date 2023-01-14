#Por a fazer que se não disse qual filtro apaga todos
sudo tc filter add dev $1 parent 1:0 protocol all u32 match ip dst $2 flowid $3