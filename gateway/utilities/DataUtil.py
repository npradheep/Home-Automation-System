'''
Created on 01-Apr-2020

@author: Pradheep

This class handles the data such as converting to and from JSON objects and writing it to a an external log file
'''
from project.device.dataClasses.SensorData import hSensorData, tSensorData, pSensorData
import json
from _datetime import datetime


class DataUtil(object):
    '''
    classdocs
    '''

        # Convert sensor object to dictionary
    def toDictSensor(self, sensorObject):
        return {'Value': sensorObject.getCurrentValue(), 'Time': sensorObject.getTimeStamp(), 'averageValue': sensorObject.getAverageValue(), 'sampleCount': sensorObject.getCount(), 'minimumValue': sensorObject.getMinValue(), 'maximumValue': sensorObject.getMaxValue()}
    
        # Final JSON object
    def tofinalJSON(self, temperature, humidity, pressure):
        arr = {'temperature': temperature, 'humidity': humidity, 'pressure':pressure}
        return json.dumps(arr)
        
        # Convert sensor data object to JSOn 
    def toJsonFromSensorData(self, SensorObject):
        y = json.dumps(dataUtil.toDictSensor(SensorObject))
        return y
    
        # Write Sensor data JSON to file
    def writeToFile(self, data):
            f = open('GatewayAppLog.txt', "a")
            f.write(str(datetime.now()) + ':  ' + data + '\n')
            f.close()

               
dataUtil = DataUtil()
