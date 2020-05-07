'''
Created on 08-Apr-2020

@author: Pradheep

This class determines the actuation to show on sensehat display
'''
from project.device.utilities.SensorHandlerApp import sensorHandler


class Actuation(object):
    '''
    classdocs
    '''

    # Logic to determine the actuation 
    def actuate(self, data):
        if (data == 'temperature'):
            sensorHandler.senseDisplay('T') # Call the display adaptor
        elif (data == 'humidity'):
            sensorHandler.senseDisplay('H') # Call the display adaptor
        elif (data == 'pressure'):
            sensorHandler.senseDisplay('P') # Call the display adaptor
        
        
actuate = Actuation()
        
