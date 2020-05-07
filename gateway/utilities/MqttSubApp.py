import paho.mqtt.client as mqtt
import time
import logging
import json
from project.gateway.utilities.CloudPub import cloudpub
from project.gateway.utilities.DataUtil import dataUtil
from project.gateway.utilities.awsConnect import  awsConnector

'''This class is used to subscribe and receieve data from the MQTT broker'''


class MqttSubApp():

    # defined to override the default on connect method
    def on_connect(self, client, userdata, flags, rc):
        dataUtil.writeToFile("Subscribe to Device: Connected with result code " + str(rc)) 
        logging.info("Subscribe to Device: Connected with result code " + str(rc))
    
    # defined to override the default on message method
    def on_message(self, client, userdata, msg):
        if (msg.topic == 'DtoG'):
            data = msg.payload.decode()
            awsConnector.awsPublish("data/gateway/sensorData", data)
            log = 'Received data from device -' + data
            logging.info(log)
            dataUtil.writeToFile(log) 
   
    def subscribe(self, topic):
  
        client = mqtt.Client()  # Create MQTT object
        client.connect("127.0.0.1", 1883, 10)  # Set connection parameters
        client.subscribe(topic, 1)  # Subscribe to topic with qos level 1
        
        client.on_connect = self.on_connect  # Override method with customized method
        client.on_message = self.on_message  # Override method with customized method
        
        client.loop_forever()  # Listen indefinitely

        
mqttsub = MqttSubApp()
