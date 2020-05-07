'''
Created on 06-Apr-2020

@author: Pradheep

This class logs the system resource values used during the runtime of the program
'''
import psutil
from threading import Thread
import logging
from time import sleep
from project.gateway.utilities.DataUtil import dataUtil
from _datetime import datetime
from project.gateway.utilities.awsConnect import awsConnect, awsConnector

class SystemPerformanceMonitor(Thread):

    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            cpu = psutil.cpu_percent()  # Get CPU usage
            mem = psutil.virtual_memory().percent  # Get RAM usage
            logger = logging.getLogger('log')
            logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
            
            # Logging the values 
            cpulog = "CPU Utilization=" + str(cpu)
            memlog = "Memory Utilization=" + str(mem)
            logger.info(cpulog)
            logger.info(memlog)
            dataUtil.writeToFile(cpulog)
            dataUtil.writeToFile(memlog)
            
            self.now = datetime.now()
            self.nowtime = str(self.now.strftime("%Y-%m-%dT%H:%M:%S"))
            
            sysJson = '{"gateway":{"cpu": '+ str(cpu) +',"mem": '+ str(mem) +', "timestamp":'+self.nowtime+'}}'
            #awsConnector.awsPublish("data/gateway/sensorData", sysJson)
            
            sleep(6)

        
