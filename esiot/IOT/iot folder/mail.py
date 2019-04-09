import urllib
import os
import time
import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


sensor=29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

def send_email():
    msg = MIMEMultipart()

    msg['From'] ="narendrasingh16255@gmail.com"
    msg['To'] = "1998manishmks@gmail.com"
    msg['Subject'] ="iot"

    msg.attach(MIMEText("object detected"))

    

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   
    mailServer.starttls()
    
    mailServer.login("oooiampooja18@gmail.com","Jainathsingh001")
    mailServer.sendmail("oooiampooja18@gmail.com","1998manishmks@gmail.com", msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    server.quit()
    return
i=1
try:
    while(True):
        if GPIO.input(sensor):
            msg=MIMEMultipart()
            msg.attach(MIMEText('object detected'))
            msg['Subject']='IOT'
            send_email()
except KeyboardInterrupt:
    GPIO.cleanup()
