import paho.mqtt.client as mqtt
import time
import logging
import json
from project.device.app.Actuation import actuate
from project.device.utilities.DataUtil import dataUtil

'''This class is used to subscribe and recieve data from the MQTT broker'''


class MqttSubApp():

    # defined to override the default on connect method
    def on_connect(self, client, userdata, flags, rc):
        dataUtil.logAndWrite("Subscribe to Gateway: Connected with result code " + str(rc)) 
    
    # defined to override the default on message method
    def on_message(self, client, userdata, msg):
        if (msg.topic == 'GtoD'):
            data = msg.payload.decode()
            dataUtil.logAndWrite('Received actuation data from Gateway: ' + data) 
            actuate.actuate(data)  # Calls the actuator method on each received actuation data
            
    # Subscribe and get data
    def subscribe(self, topic):
        logging.basicConfig(level=logging.DEBUG)    
        logger = logging.getLogger(__name__)
        
        client = mqtt.Client()  # Create MQTT object
        client.connect("127.0.0.1", 1883, 10)  # Set connection parameters
        client.subscribe(topic, 1)  # Subscribe to topic with qos level 1
        
        client.on_connect = self.on_connect  # Override method with customized method
        client.on_message = self.on_message  # Override method with customized method
        
        client.loop_forever()  # Listen indefinitely


mqttsub = MqttSubApp()
