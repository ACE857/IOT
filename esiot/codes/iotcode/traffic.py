import RPi.GPIO as GPIO
import time

def f(x, y, z):
   GPIO.output(x, True)
   GPIO.output(y, False)
   GPIO.output(z, False) 


Red=22
Yellow=21
Green=20

Red2=20
Yellow2=21
Green2=22

GPIO.setmode(GPIO.BCM)
GPIO.setup(Red,GPIO.OUT)
GPIO.setup(Yellow,GPIO.OUT)
GPIO.setup(Green,GPIO.OUT)


try: 
   while True:
        f(Red, Yellow, Green)
        f(Green2, Yellow2, Red2 )
        time.sleep(2)
        f(Yellow, Red, Green)
        f(Yellow2, Red2, Green2)
        time.sleep(1)
        f(Green, Red, Yellow)
        f(Red2, Yellow2, Green2)
        time.sleep(2)
          
      
except KeyboardInterrupt:
    GPIO.cleanup()
