import paho.mqtt.client as mqttClient
import time
import logging
from project.gateway.utilities.DataUtil import dataUtil

'''
global variables

This class serves as a publisher method for publishing data to the cloud sevice
'''


class CloudPub:
    global connected 
    connected = False  # Stores the connection status
    BROKER_ENDPOINT = "things.ubidots.com"
    PORT = 1883
    MQTT_USERNAME = "BBFF-YTny7Ru968fIz6EHhT3P8mRgLDiIXp"  # Put your TOKEN here
    MQTT_PASSWORD = ""
    TOPIC = "/v1.6/devices/"
    DEVICE_LABEL = "raspberry"
    
    '''
    Functions to process incoming and outgoing streaming
    '''
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.logAndWrite("[INFO] Connected to broker")
            global connected  # Use global variable
            connected = True  # Signal connection
    
        else:
            self.logAndWrite("[INFO] Error, connection failed")
    
    def on_publish(self, client, userdata, result):
        self.logAndWrite("[INFO] Published!")
    
    def connect(self, mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
        global connected
    
        if not connected:
            mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
            mqtt_client.on_connect = self.on_connect
            mqtt_client.on_publish = self.on_publish
            mqtt_client.connect(broker_endpoint, port=port)
            mqtt_client.loop_start()
    
            attempts = 0
    
            while not connected and attempts < 1:  # Waits for connection
                self.logAndWrite("[INFO] Attempting to connect...")
                time.sleep(1)
                attempts += 1
    
        if not connected:
            self.logAndWrite("[ERROR] Could not connect to broker")
            return False
    
        return True
    
    # The actual publish method
    def publish(self, payload):
        topic = "{}{}".format(self.TOPIC, self.DEVICE_LABEL)
        self.connect(self.mqtt_client, self.MQTT_USERNAME, self.MQTT_PASSWORD, self.BROKER_ENDPOINT, self.PORT)  # Connection parameters
        self.mqtt_client.publish(topic, payload, 1)  # Publish
            
    def __init__(self):
        self.mqtt_client = mqttClient.Client()
    
    def logAndWrite(self, data):
        logging.info(data)
        dataUtil.writeToFile(data)
        
    
cloudpub = CloudPub()
