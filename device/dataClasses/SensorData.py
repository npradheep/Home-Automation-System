'''
Created on 01-Apr-2020

@author: Pradheep

This class gets the sensor data and maintains a record to calculate the statistics and log it to the console
'''
from _datetime import datetime
import logging
from project.device.utilities.DataUtil import dataUtil


class SensorData():
   # init variables
    currentValue = 0
    minimumValue = 10000
    maximumValue = 0
    totalValue = 0
    averageValue = 0
    sampleCount = 0
    name = "null"
    log = "null"
    nowtime = 0
    
    logger = logging.getLogger('log')
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    # Keeps track of the total sum of all the temperature values for the purpose of finding average
    def addValue(self, data):
        self.currentValue = data
        self.totalValue += data
        self.sampleCount += 1
        if (self.maximumValue < data) :
            self.maximumValue = data  # Sets maximum temperature value
        if (self.minimumValue > data) :
            self.minimumValue = data  # Sets minimum temperature value
        self.getAverageValue()
        self.now = datetime.now()
        self.nowtime = str(self.now.strftime("%Y-%m-%dT%H:%M:%S"))
        self.log = "\n" + self.getName() + ":\n Time   : " + str(self.getTimeStamp()) + "\n Current: " + str(data) + "\n Average: " + str(self.getAverageValue()) + "\n Samples: " + str(self.getCount()) + "\n Min    : " + str(self.getMinValue()) + "\n Max    : " + str(self.getMaxValue()) + "\n"
        dataUtil.logAndWrite(self.log)  # Prints log to console
    
    # Returns log value
    def getLog(self):
        return self.log
        
    # Returns timestamp
    def getTimeStamp(self):
        return self.nowtime
    
    # Returns average value
    def getAverageValue(self):
        self.averageValue = (self.totalValue / self.sampleCount)
        return self.averageValue
    
    # Returns Sample Count
    def getCount(self):
        return self.sampleCount
    
    # Returns current value
    def getCurrentValue(self):
        return self.currentValue
    
    # Returns max value
    def getMaxValue(self):
        return self.maximumValue
    
    # Returns min value
    def getMinValue(self):
        return self.minimumValue
    
    # Rey=turns the name
    def getName(self):
        return self.name
    
    # Sets the name of the sensor
    def setName(self, String):
        self.name = String
    

tSensorData = SensorData()
tSensorData.setName("TemperatureSensor")
pSensorData = SensorData()
pSensorData.setName("PressureSensor")
hSensorData = SensorData()
hSensorData.setName("HumiditySensor")
