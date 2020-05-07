'''
Created on 28-Jan-2020

@author: Pradheep

This class gets the SMTP configuration from ConfigUtil class and sends an email when called
'''
import smtplib
from project.gateway.utilities.ConfigUtil import conf as ConfUtil
import logging
from project.gateway.utilities.DataUtil import dataUtil


class SmtpClientConnector():

    def sendEmail(self, body):
        # Set config parameters to variables
        subject = "IoT Device Notification"        
        configParams = ConfUtil.getValue('smtp.cloud')
        host = configParams.get("host")
        port = configParams.get("port")
        sender = configParams.get("fromaddr")
        receiver = configParams.get("toaddr")
        authToken = configParams.get("authtoken")
        
        # Send mail
        server = smtplib.SMTP(host, port)  # connect to smtp server
        server.starttls()  # Start TTLS service
        server.login(sender, authToken)  # Login to mailserver
        message = 'Subject: {}\n\n{}'.format(subject, body)  # set message contents
        server.sendmail(sender, receiver, message)  # Send an email
        logging.info('Email notification sent..')
        dataUtil.writeToFile('Email notification sent')

