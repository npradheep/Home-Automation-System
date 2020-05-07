'''
Created on 28-Jan-2020

@author: Pradheep
 
This class parses the configuration file and makes the data usable in python
'''
import configparser
import os.path
import sys

parser = configparser.ConfigParser()
path = '../../ConnectedDevicesConfig.props'


class ConfigUtil():
     
    # Checks if the file has any valid configuration data
    def hasConfig(self):
        return True if parser.sections() else False
     
    # Loads the configuration file       
    def loadConfig(self, path):
        if os.path.exists(path) is True:  # Checks if path exists
            parser.read(path)
            return True
        else:
            return False
    
    # Parses the config file       
    def getValue(self, section):
        conf.loadConfig(path) if (conf.hasConfig()) == True else sys.exit('Not a valid Configuration file')
        return dict(parser.items(section))  # Formats the parsed values as a dictionary and returns it
    
    def __init__(self):
        self.loadConfig(path) 

        
conf = ConfigUtil()

