'''
Created on 03-Apr-2020

@author: Pradheep
This class handles the sensehat LED actuation
'''
from sense_hat import SenseHat
from time import sleep
from project.device.utilities.DataUtil import dataUtil


class SensorHandlerApp(object):
    
    rate = 1  # display rate
    rotateDeg = 270  # sensehat display rotation angle
                
    def senseDisplay(self, message):
        sensehat.clear()  # Clear the display
        sensehat.set_rotation(self.rotateDeg)  # set rotation
        try:
            dataUtil.logAndWrite('Message displayed on SenseHat LED: ')
            sensehat.show_letter(message)  # show message on LED
            dataUtil.logAndWrite('Actuation Successful..')

        except:
            dataUtil.logAndWrite("Could not connect to the display!")  # Print error if cannot connect to the actuator
        sleep(self.rate) 
        sensehat.clear()
        sleep(self.rate)

        
sensorHandler = SensorHandlerApp()
sensehat = SenseHat()
