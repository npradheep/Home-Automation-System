# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
from project.gateway.utilities.DataUtil import dataUtil

class awsConnect:
# For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("myClientID")
    
    # Configure the MQTT Client
    myMQTTClient.configureEndpoint("endpoint", 443)
    myMQTTClient.configureCredentials("/AmazonRootCA1.pem", "private.key", "cert.pem")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    
    def awsPublish(self, topic, message):
        # Connect to AWS IoT endpoint and publish a message
        self.myMQTTClient.connect()
        self.myMQTTClient.publish(topic, message, 0)
        logging.info("[INFO] Published!")
        dataUtil.writeToFile("[INFO] Published!")
        self.myMQTTClient.disconnect()
        
awsConnector = awsConnect()

