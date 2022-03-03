import os
import random
import json
import datetime
from paho.mqtt import client as mqtt_client

from dotenv import load_dotenv
load_dotenv()

detection_data = {}

try:
    broker_addr = os.getenv("MQTT_BROKER_ADDR")
    broker_port = int(os.getenv("MQTT_BROKER_PORT"))
    timeout = int(os.getenv("MQTT_BROKER_TIMEOUT"))
    mqtt_topic = os.getenv("MQTT_TOPIC")
    
except Exception as e:
    print("Unable to get MQTT Parameter from .env file")
    print(e)

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker_addr, broker_port)
    return client

def on_message(client, userdata, msg):
    # print(msg.payload, msg.topic)
    if(msg.topic == mqtt_topic):
        # print(f"Received from topic `{msg.topic}`")
        # print(type(msg.payload.decode()))
        data = json.loads(msg.payload.decode())
        timestamp = datetime.datetime.now()
        
        global detection_data
        detection_data = data
        
        print(f"MQTT - {timestamp} - {type(data)} {detection_data}")
    
        
def subscribe(client: mqtt_client):
    client.subscribe(mqtt_topic)
    
    client.on_message = on_message

def get_detection_data():
    return detection_data

def reset_detection_data():
    global detection_data
    detection_data = {"detection":0,"xpos":0,"ypos":0}

def runMQTT():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    return client
