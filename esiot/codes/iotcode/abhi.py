import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(12, True)
        GPIO.output(18, False)
        time.sleep(1)
        GPIO.output(18, True)
        GPIO.output(12, False)
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    