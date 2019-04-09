import RPi.GPIO as GPIO
import time
def f(x, y, z):
   GPIO.output(x,GPIO.LOW)
   GPIO.output(y,GPIO.HIGH)
   GPIO.output(z,GPIO.LOW) 


Red=40
Yellow=37
Green=35
GPIO.setmode(GPIO.BCM)
GPIO.setup(Red,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(Yellow,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(Green,GPIO.OUT)
GPIO.setwarnings(False)


try: 
   while True:
        f(Red, Yellow, Green)
        time.sleep(1)
        
        f(Yellow, Red, Green)
        
        time.sleep(1)
        
        f(Green, Red, Yellow)
        
        time.sleep(1)
          
      
except KeyboardInterrupt:
    GPIO.cleanup()

