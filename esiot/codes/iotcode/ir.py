import RPi.GPIO as GPIO
import time

led = 12
ir_sensor = 16
buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(ir_sensor, GPIO.IN)

GPIO.output(led, False)
print "We are ready"
cnt=0
try:
    while True:
        if GPIO.input(ir_sensor):
            cnt=cnt+1
            GPIO.output(led, False)
            print "Object Found"
            print cnt
            if cnt%5==0:
                GPIO.output(buzzer, True)
        while GPIO.input(ir_sensor):
            time.sleep(0.5)
        else:
            GPIO.output(led,True)
            GPIO.output(buzzer,False)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    
