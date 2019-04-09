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

def send_mail(body):
    print("Sending Mail")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("ccaabhi@gmail.com", "abhinayS1!") 
    print("Logged In.")
    message = "SUBJECT: " + body + "\nTemp Sensed: " + str("ae yo !");
      
    s.sendmail("ccaabhi@gmail.com", "srjbsht857@gmail.com", message)
    print("Mail Sent.")
    s.quit()
i=1
try:
    #while(True):
        #if GPIO.input(sensor):
            msg=MIMEMultipart()
            msg.attach(MIMEText('object detected'))
            msg['Subject']='IOT'
            send_mail("askjdk")
except KeyboardInterrupt:
    GPIO.cleanup()


