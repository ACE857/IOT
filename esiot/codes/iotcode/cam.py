import os
import RPi.GPIO as GPIO
import urllib2
import time

sensor = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
i = 1
try:
    while(True):
        if GPIO.input(sensor):
            s = "photo"+str(i)+".jpg"
            data = urllib2.urlopen("http://192.168.43.1:8080/photo.jpg")
            image = open(s,"wb")
            image.write(data.read())
            image.close()
            i = i+1
except KeyboardInterrupt:
    GPIO.cleanup()