import paho.mqtt.client as mqtt
''' This class is used to publish data to the MQTT broker'''


class MqttPubApp():

    def publish(self, topic, json):
        client = mqtt.Client()  # Initializing the MQTT object
        client.connect("127.0.0.1", 1883, 10)  # Setting the connection parameters
        client.publish(topic, json, 0);  # Publishing the message
        client.disconnect()  # disconnect

                
mqttpub = MqttPubApp()
