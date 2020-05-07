'''
Created on 08-Apr-2020

@author: Pradheep

This class acts as a cloud data listener and gets the data each time something is updated
'''
from ubidots import ApiClient
import time
from threading import Thread
from project.gateway.utilities.MqttPubApp import mqttpub
from project.gateway.utilities.SmtpClientConnector import SmtpClientConnector
import logging
from project.gateway.utilities.DataUtil import dataUtil

smtp = SmtpClientConnector()


class CloudGET(Thread):
    
    # declaring required variables 
    tLast = None
    pLast = None
    hLast = None
    tstamp = None
    hstamp = None
    pstamp = None
    
    def __init__(self):
        Thread.__init__(self)
        api = ApiClient(token='BBFF-YTny7Ru968fIz6EHhT3P8mRgLDiIXp') 
        
        # Get cloud variables
        self.tempact = api.get_variable('5e8d31b51d84726d64f4a1e7')
        self.presact = api.get_variable('5e8d31cc1d84726e869ab59e')
        self.humact = api.get_variable('5e8d31c21d84726e88d71d66') 
        self.getData()  # Get data from variables
        
        # Check the timestamp
        if self.tLast is not None: self.tstamp = self.tLast[0]['timestamp']
        if self.pLast is not None: self.pstamp = self.pLast[0]['timestamp']
        if self.hLast is not None: self.hstamp = self.hLast[0]['timestamp']
        
    def run(self):
        while True:
            # get all actuator variable data
            self.getData()
            
            # Check if there is any new actuation required
            self.getPresAct()
            self.getTempAct()
            self.getHumAct() 
            
            time.sleep(60)
        
        # Check if there is a change in timestamp
    def checkActuation(self, actdata, stamp):
        if (stamp != None and actdata[0]['timestamp'] != stamp):
            stamp = actdata[0]['timestamp']
            return True
        
        # et data from the respective cloud variables
    def getData(self):
        try:
            self.tLast = self.tempact.get_values(1)
            self.pLast = self.presact.get_values(1)
            self.hLast = self.humact.get_values(1)
        except:
            pass
    
        # If actuation is set
    def actuationTrue(self, log):
        smtp.sendEmail(log) 
        logging.info(log)
        dataUtil.writeToFile(log)
    
        # If actuation is not set
    def actuationFalse(self, log):
        logging.info(log)
        dataUtil.writeToFile(log)
        
        # get temperature actuation data
    def getTempAct(self):
        if (self.checkActuation(self.tLast, self.tstamp)):
            mqttpub.publish('GtoD', 'temperature')
            tlog = 'Temperature beyond threshold, actuation command sent: \n' + str(self.tLast)
            self.actuationTrue(tlog)
        else:
            tlog = 'Temperature - no actuation'
            self.actuationFalse(tlog)
    
            # get humidity actuation data
    def getHumAct(self):
        if (self.checkActuation(self.hLast, self.hstamp)):
            mqttpub.publish('GtoD', 'humidity') 
            hlog = 'Humidity beyond threshold, actuation command sent: \n' + str(self.hLast)
            self.actuationTrue(hlog)
        else:
            hlog = 'Humidity - no actuation'
            self.actuationFalse(hlog)
            
            # get pressure actuation data
    def getPresAct(self):
        if (self.checkActuation(self.pLast, self.pstamp)):
            mqttpub.publish('GtoD', 'pressure') 
            plog = 'Pressure beyond threshold, actuation command sent: \n' + str(self.pLast)
            self.actuationTrue(plog)   
        else:
            plog = 'Pressure - no actuation'
            self.actuationFalse(plog)

     
cloudGetData = CloudGET()

        
