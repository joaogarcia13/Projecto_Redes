#!/bin/bash

ufw default allow routed
ufw default deny incoming
ufw default deny outgoing
ufw allow ssh
ufw allow from any port ssh
ufw allow 5000
ufw allow 9100
ufw allow from any port 9100
ufw allow from any port 9090
ufw --force enable