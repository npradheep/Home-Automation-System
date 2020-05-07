'''
Created on 06-Apr-2020

@author: Pradheep

This class serves as a deiver app for the device
'''
from project.device.app import SensorAdaptorTask
from project.device.app.SystemPerformanceMonitor import SystemPerformanceMonitor
from project.device.utilities.MqttSubApp import mqttsub

sensorAdaptor = SensorAdaptorTask.SensorAdaptorTask()
sysMon = SystemPerformanceMonitor()

sensorAdaptor.start()  # Get values from sensor and publish to gateway
sysMon.start()  # Displays the system resource utilization stats
mqttsub.subscribe('GtoD')  # Subscribe to actuation data sent by gateway
