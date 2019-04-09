import RPi.GPIO as GPIO
import time

led = 12
sensor = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

GPIO.output(led, False)
print "We are ready"
cnt=0
try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(led, True)
            print "Sensing Temperature"
        else:
            GPIO.output(led,False)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    

