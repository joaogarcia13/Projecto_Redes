sudo tc qdisc add dev $1 root handle 1:0 htb default 30 
sudo tc class add dev $1 parent 1:0 classid 1:1 htb rate 10gbit