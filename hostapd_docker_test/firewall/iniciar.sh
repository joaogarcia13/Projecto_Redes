#docker image build -t firewall .
#docker run firewall

#Se tiver a funcionar como router as rotas tem que estar a ser permitidas
ufw default allow routed
#Prevenir ataques à máquina
ufw default deny incoming
ufw default deny outgoing
ufw allow ssh
ufw allow from any port ssh
ufw allow 5000
ufw --force enable
