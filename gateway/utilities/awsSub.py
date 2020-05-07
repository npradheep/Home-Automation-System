# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
from project.gateway.utilities.DataUtil import dataUtil
import time
from threading import Thread
from project.gateway.utilities.ActuationLogic import actLogic

class awsSubscribe(Thread):
# For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("myClientID1")
    
    # Configure the MQTT Client
    myMQTTClient.configureEndpoint("endpoint", 443)
    myMQTTClient.configureCredentials("rootca", "private.key", ".cert.pem")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    
    def on_message(self, client, userdata, msg):
            data = msg.payload.decode()
            logging.info(data)
            dataUtil.writeToFile(data)
            actLogic.checkActuation(data)
            
   
    def run(self):
        # Connect to AWS IoT endpoint and publish a message
        self.myMQTTClient.connect()
        self.myMQTTClient.subscribe("data/cloud/actuationData", 0, self.on_message)
        #self.myMQTTClient.onMessage = self.on_message
        logging.info("[INFO] Subscribed!")
        dataUtil.writeToFile("[INFO] Subscibed!")
        while True:
            time.sleep(1)
    
    def __init__(self):
        Thread.__init__(self)  
        
        
    
awsSub = awsSubscribe()

