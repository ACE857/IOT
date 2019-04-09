import time
import RPi.GPIO as GPIO 

TRUE = 1

relay1 = 12
relay2 = 16
latch = 7


GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(latch,GPIO.OUT)

def relayState(relay,val):
	if relay==1:
		GPIO.output(relay1,val)
	if relay==2:
		GPIO.output(relay2,val)
	if relay==3:
		GPIO.output(latch,val)
		
try:
    while TRUE:
		relayState(1,1)
		time.sleep(1)
		relayState(1,0)
		time.sleep(1)
		relayState(2,1)
		time.sleep(1)
		relayState(2,0)
		time.sleep(1)
		relayState(3,1)
		time.sleep(1)
		relayState(3,0)
		time.sleep(1)
	
	
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()