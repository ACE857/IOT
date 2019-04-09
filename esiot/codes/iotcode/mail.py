import RPi.GPIO as GPIO
import time
import urllib2

LED = 12
sensor = 16
buzzer = 18
i=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(LED , GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

GPIO.output(LED , False)
print "We are ready"
cnt=0
try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(LED, True)
            print 'object!!'
            data=urllib2.urlopen("http://192.168.43.1:8080/photo.jpg")
            filename="pic"+str(i)+".jpg"
            image = open(filename, "wb")
            image.write(data.read())
            image.close()
            while GPIO.input(sensor):
                time.sleep(.1)
        else:
            GPIO.output(LED,False)
except KeyboardInterrupt:
    GPIO.cleanup()
    

