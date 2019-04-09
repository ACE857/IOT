import RPi.GPIO as GPIO
import time

red = 16
green = 12
yellow=18


GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.IN)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)



GPIO.output(buzzer,False)
print "IR Sensor Ready....."
print " "

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print "Object Detected"
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()