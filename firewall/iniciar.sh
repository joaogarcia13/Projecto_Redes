sudo ufw default allow routed
sudo ufw default deny incoming
sudo ufw default deny outgoing
sudo ufw allow ssh
sudo ufw allow from any port ssh
sudo ufw allow 5000
sudo ufw allow 9100
sudo ufw allow from any port 9100
sudo ufw allow from any port 9090
sudo ufw --force enable