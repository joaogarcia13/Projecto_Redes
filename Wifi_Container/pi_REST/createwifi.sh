#!/bin/bash

pkill hostapd

sleep 5

if [ $# -eq 2 ]
then
	echo "interface=wlan0
#If this fails, try rt1871xdrv a 
driver=nl80211
# Name of the new network: best use the hostname
ssid=$1

# Pick a channel not already in use
channel=6
# Change to b for older devices?
hw_mode=g
macaddr_acl=0
auth_algs=3
# Disable this to insure the AP is visible:
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=$2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP" > hostapd.conf

/usr/sbin/hostapd hostapd.conf

elif [ $# -eq 1 ]
then
	echo "interface=wlan0
#If this fails, try rt1871xdrv a 
driver=nl80211
# Name of the new network: best use the hostname
ssid=$1

# Pick a channel not already in use
channel=6
# Change to b for older devices?
hw_mode=g
macaddr_acl=0
auth_algs=3
# Disable this to insure the AP is visible:
ignore_broadcast_ssid=0
#wpa=2
#wpa_passphrase=$2
#wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP
#rsn_pairwise=CCMP" > hostapd.conf

/usr/sbin/hostapd hostapd.conf

else
	echo "Expected 1 or 2 arguments, got $#."
fi
