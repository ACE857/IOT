import os
import RPi.GPIO as GPIO
import urllib.request as urllib2
import time

HIGH  = 1
LOW  = 0
ir = 5
led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_UP)

i=1
try:
    while(True):
        if GPIO.input(ir) == LOW:
            print("object detected")
            s="photo"+str(i)+".jpg"
            data=urllib2.urlopen("http://[192.168.43.110]:8080/photo.jpg")
            image=open(s,"wb")
            image.write(data.read())
            image.close()
            i=i+1
except KeyboardInterrupt:
    GPIO.cleanup()
            
