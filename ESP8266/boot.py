# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

##*********************************************************************************************
# Initialisation du module WIFI en mode station.
#
#
#----------------------------------------------------------------------------------------------
ssid = "Galaxy A10s1304"
password = 'Junior@976'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

#///////////////////////////////////////////////////////////////////////////////////////////////
# Connexion au WIFI
# On attend jusqu'à ce que la connexion soit établie.
# Pour notre cas d'utilisation, il n'y a aucune raison d'aller plus loins sans la connexion WIFI.
#///////////////////////////////////////////////////////////////////////////////////////////////

while station.isconnected() == False:
  pass




mqtt_server = 'test.mosquitto.org'
mqtt_port   = 1883
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = 'notification'
topic_pub = b'DIUEIL/JMPQ/Temperature'

last_message = 0
message_interval = 5 # Intervale en seconde entre deux messages  
counter = 0




print('Connexion WIFI établie')
print(station.ifconfig())