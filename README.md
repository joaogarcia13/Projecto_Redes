# Projecto_Redes

Container with dhcp, ufw, tc and hostapd and flask interface

build with:
sudo docker build -t <container_name> .

sudo docker run -i -t --restart=always --network=host --privileged <container_name>
