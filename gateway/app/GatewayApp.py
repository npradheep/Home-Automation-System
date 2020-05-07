'''
Created on 06-Apr-2020

@author: Pradheep

This class serves as a driver for the Gateway app
'''
from project.gateway.utilities.MqttSubApp import mqttsub
from project.gateway.utilities.CloudGET import cloudGetData
from project.gateway.app.SystemPerformanceMonitor import SystemPerformanceMonitor
from project.gateway.utilities.awsSub import awsSub

sysMon = SystemPerformanceMonitor()

awsSub.start()
sysMon.start()  # Displays the system resource utilization stats
#cloudGetData.start()  # Acts as a listener to the cloud data
mqttsub.subscribe('DtoG')  # Subscribe to the sensor values published bu the device app

