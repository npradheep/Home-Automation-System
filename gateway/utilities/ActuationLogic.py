'''
Created on 02-May-2020

@author: Pradheep
'''
import json
from project.gateway.utilities.MqttPubApp import mqttpub
from project.gateway.utilities.DataUtil import dataUtil
import logging
from project.gateway.utilities.SmtpClientConnector import SmtpClientConnector
smtp = SmtpClientConnector()

class ActuationLogic(object):
    
    def checkActuation(self,data):
        data = data.replace("'", "\"")
        d = json.loads(data)
        
        if (d['temp']!=0):
            mqttpub.publish('GtoD', 'temperature')
            tlog = 'Temperature beyond threshold, actuation command sent: ' + str(d['temp'])
            self.actuationTrue(tlog)
        else:
            tlog = 'Temperature - no actuation'
            self.actuationFalse(tlog)
            
            
        if (d['hum']!=0):
            mqttpub.publish('GtoD', 'humidity')
            hlog = 'Humidity beyond threshold, actuation command sent: ' + str(d['hum'])
            self.actuationTrue(hlog)
        else:
            hlog = 'Humidity - no actuation'
            self.actuationFalse(hlog)
            
            
        if (d['pres']!=0):
            mqttpub.publish('GtoD', 'pressure')
            plog = 'Pressure beyond threshold, actuation command sent: ' + str(d['pres'])
            self.actuationTrue(plog)   
        else:
            plog = 'Pressure - no actuation'
            self.actuationFalse(plog)
            
            
            
    # If actuation is set
    def actuationTrue(self, log):
        #smtp.sendEmail(log) 
        logging.info(log)
        dataUtil.writeToFile(log)
    
        # If actuation is not set
    def actuationFalse(self, log):
        logging.info(log)
        dataUtil.writeToFile(log)
        
        
actLogic = ActuationLogic()
        