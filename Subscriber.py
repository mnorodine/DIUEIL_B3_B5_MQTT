# Subscriber

import time
import paho.mqtt.client as mqtt


broker 	= "test.mosquitto.org"
port 	= 1883
topic	= "DIUEIL/JMPQ/Temperature"

client = mqtt.Client("Subdevice")
client.connect(broker, port)

def on_connect(client, userdata, flags, rc):
	print("Connexion au broker MQTT ", broker, " sous le topic ", topic)
	client.subscribe(topic)





def on_message(client, userdata, message):
	
    msg = time.strftime("%B %d,%Y at %H:%M%p Mronabeja Temperature ", time.gmtime()) + message.payload.decode("utf-8") +"\n"
    fp = open("Lecture_capteur_MQTT.txt", "a")
    fp.write(msg)

    fp.close()

    print(msg)


while True:
	client.on_connect = on_connect
	client.on_message = on_message
	client.loop_forever()

    