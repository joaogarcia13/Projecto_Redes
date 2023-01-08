#docker image build -t firewall .
#docker run firewall

#Se tiver a funcionar como router as rotas tem que estar a ser permitidas
sudo ufw default allow routed
#Prevenir ataques à máquina
sudo ufw default deny incoming
#Outging fica inativo = não conseguimos fazer atualizações à máquina, fazer uma API para atualizar e ativamos e depois desativamos o outgoing
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 5000
sudo ufw enable