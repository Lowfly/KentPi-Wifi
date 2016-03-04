#!/usr/bin/env python
# -*- coding: UTF8 -*-

import os
import sys
  
ctrl_interface="DIR=/var/run/wpa_supplicant GROUP=netdev"
update_config="1"

ssid="eduroam"
proto="RSN"
key_mgmt="WPA-EAP"
pairwise="CCMP"
auth_alg="OPEN"
eap="PEAP"
identity=""
password=""
phase2="auth=MSCHAPV2"

 
# ecrire dans un fichier

def setConfig():
	fichier = open("/etc/wpa_supplicant/wpa_supplicant.conf","w")
	
	fichier.writelines("ctrl_interface=" + ctrl_interface + "\n")
	fichier.writelines("update_config=" + update_config + "\n")
	fichier.writelines("network={\n")
	fichier.writelines("ssid=\"" + ssid + "\"\n")
	fichier.writelines("proto=" +  proto + "\n")
	fichier.writelines("key_mgmt=" + key_mgmt + "\n")
	fichier.writelines("pairwise=" + pairwise + "\n")
	fichier.writelines("auth_alg=" + auth_alg + "\n")
	fichier.writelines("eap=" + eap + "\n")
	fichier.writelines("identity=\"" + identity + "\"\n")
	fichier.writelines("password=\"" + password + "\"\n")
	fichier.writelines("phase2=\"" + phase2 + "\"\n")
	fichier.writelines("}")

	fichier.close()

if __name__ == "__main__":
	
	try:
		identity = sys.argv[1]
		password = sys.argv[2]		
		setConfig()
		os.system("ifdown wlan0")
		os.system("ifup wlan0")
	except:
		print ("\tusage : python wifi-setup.py [identity] [password]")
