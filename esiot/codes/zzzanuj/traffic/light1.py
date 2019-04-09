import RPi.GPIO as GPIO
import time

LED_RED_1 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_1,GPIO.OUT)
try:
    while True:
        GPIO.output(LED_RED_1,True)
        print("agni@")
    
except KeyboardInterrupt:
    GPIO.cleanup()  

