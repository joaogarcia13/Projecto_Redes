#Por a fazer que se não disse qual filtro apaga todos
sudo tc filter add dev $1 parent 1:0 protocol all u32 match ip dst $2 flowid $3

#Tenho de criar um qdisc para o upload
#Uma classe principal para o upload
sudo tc filter add dev eth0 parent 2: protocol all u32 match ip src 192.168.1.39 classid 2:20 #ASsim bloqueia o upload mas para todos