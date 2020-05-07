'''
Created on 06-Apr-2020

@author: Pradheep

This class logs the system resource values used during the runtime of the program
'''
import psutil
from threading import Thread
import logging
from time import sleep
from project.device.utilities.DataUtil import dataUtil 
from _datetime import datetime
from project.device.utilities.MqttPubApp import MqttPubApp

class SystemPerformanceMonitor(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.pub = MqttPubApp()
        
    def run(self):
        while True:
            cpu = psutil.cpu_percent()  # Get CPU usage
            mem = psutil.virtual_memory().percent  # Get RAM usage
            
            # Logging the values 
            cpulog = "CPU Utilization=" + str(cpu)
            memlog = "Memory Utilization=" + str(mem)
            dataUtil.logAndWrite(cpulog)
            dataUtil.logAndWrite(memlog)
            
            self.now = datetime.now()
            self.nowtime = str(self.now.strftime("%Y-%m-%dT%H:%M:%S"))
            
            sysJson = '{"device":{"cpu": '+ str(cpu) +',"mem": '+ str(mem) +', "timestamp":'+self.nowtime+' }}'
            #self.pub.publish("DtoG", sysJson)
            
            sleep(6)

        
