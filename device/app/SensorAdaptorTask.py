'''
Created on 06-Apr-2020

@author: Pradheep

This class fetches the sensor data from the respective sensors, 
maintains it in a object, converts it into JSON and publishes 
it to the Gateway device
'''
from sense_hat import SenseHat
from project.device.dataClasses.SensorData import hSensorData, tSensorData, pSensorData
from threading import Thread
from time import sleep
from project.device.utilities.DataUtil import DataUtil, dataUtil
from project.device.utilities.MqttPubApp import mqttpub


class SensorAdaptorTask(Thread):
    '''
    classdocs
    '''

    def __init__(self):
        Thread.__init__(self)           
        self.sense = SenseHat()     
    
    def getTemperature(self):
        temp = self.sense.get_temperature()  # Get temperature data
        tSensorData.addValue(temp)  # Update the object
        return temp
    
    def getHumidity(self):
        temp = self.sense.get_humidity()  # Get humidity data
        hSensorData.addValue(temp)  # Update the object
        return temp
    
    def getPressure(self):
        temp = self.sense.get_pressure()  # Get pressure data
        pSensorData.addValue(temp)  # Update the object
        return temp
        
    def run(self):
        while True:
            # Get values
            self.getTemperature()
            self.getHumidity()
            self.getPressure()
            
            # Convert to JSON
            temperature = DataUtil.toDictSensor(self, tSensorData)
            humidity = DataUtil.toDictSensor(self, hSensorData)
            pressure = DataUtil.toDictSensor(self, pSensorData)
            
            # Create JSON object
            jsonData = DataUtil.tofinalJSON(self, temperature, humidity, pressure)
            
            # Publish JSON object to Gateway Device
            mqttpub.publish("DtoG", jsonData)
            
            
            dataUtil.logAndWrite('Published sensor data to Gateway: ' + jsonData)
            sleep(10)

        
