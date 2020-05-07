'''
Created on 01-Apr-2020

@author: Pradheep

This class handles the data such as converting to and from JSON objects and writing it to a an external log file
'''

import json
from _datetime import datetime
import logging


class DataUtil(object):
    '''
    classdocs
    '''

        # Convert sensor object to dictionary
    def toDictSensor(self, sensorObject):
        return {'value': sensorObject.getCurrentValue(), 'timestamp': sensorObject.getTimeStamp(), 'averageValue': sensorObject.getAverageValue(), 'sampleCount': sensorObject.getCount(), 'minimumValue': sensorObject.getMinValue(), 'maximumValue': sensorObject.getMaxValue()}
    
        # Final JSON object
    def tofinalJSON(self, temperature, humidity, pressure):
        arr = {'temperature': temperature, 'humidity': humidity, 'pressure':pressure}
        return json.dumps(arr)
        
        # Convert sensor data object to JSOn 
    def toJsonFromSensorData(self, SensorObject):
        y = json.dumps(dataUtil.toDictSensor(SensorObject))
        return y
        
        # Write data to a file on local disk
    def writeToFile(self, data):
            f = open('DeviceAppLog.txt', "a")
            f.write(str(datetime.now()) + ':  ' + data + '\n')
            f.close()
            
        # Logs and writes the passed data
    def logAndWrite(self, data):
        logging.info(data)
        self.writeToFile(data)


dataUtil = DataUtil()
