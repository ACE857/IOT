import RPi.GPIO as GPIO
import time

nw = {
        'red': 17,
        'yellow': 10,
        'green': 6
    }
ne = {
        'red': 18,
        'yellow': 12,
        'green': 7
    }
se = {
        'red': 19,
        'yellow': 13,
        'green': 8
      }
sw = {
        'red': 20,
        'yellow': 16,
        'green': 9
        }
GPIO.setmode(GPIO.BCM)
for item in [nw, ne, sw, se]:
    for key, value in item.items():
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, GPIO.LOW)

try :
    while True:
        
        GPIO.output(ne['red'], GPIO.LOW)
        GPIO.output(sw['red'], GPIO.LOW)
        
        GPIO.output(nw['green'], GPIO.LOW)
        GPIO.output(se['green'], GPIO.LOW)
        
        
        GPIO.output(nw['red'], GPIO.HIGH)
        GPIO.output(se['red'], GPIO.HIGH)
        
        GPIO.output(ne['green'], GPIO.HIGH)
        GPIO.output(sw['green'], GPIO.HIGH)
        time.sleep(2)
        
        GPIO.output(nw['red'], GPIO.LOW)
        GPIO.output(se['red'], GPIO.LOW)
        
        GPIO.output(ne['green'], GPIO.LOW)
        GPIO.output(sw['green'], GPIO.LOW)
        
        GPIO.output(ne['red'], GPIO.HIGH)
        GPIO.output(sw['red'], GPIO.HIGH)
        
        GPIO.output(nw['green'], GPIO.HIGH)
        GPIO.output(se['green'], GPIO.HIGH)
        time.sleep(2)
        
        
except KeyboardInterrupt :
     GPIO.cleanup()
        

        
        
        
        