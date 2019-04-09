import time
import RPi.GPIO as GPIO 

RUNNING = True

HIGH  = 1
LOW  = 0
ir = 5
led = 26

def InitSystem():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led,GPIO.OUT)
	GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	return



def DetectPerson():
	while True:
		input_state = GPIO.input(ir)
		time.sleep(0.3)	
		if input_state == 0:
			return LOW
		else:
			return HIGH
			
	
			
			
try:
	print("\nCounting using IR LED\n")
	print ("-----------------------------------------------\n" )
	InitSystem()
	count =0;
	while True :
		state = DetectPerson()
		GPIO.output(led, GPIO.LOW)
		time.sleep(1)
		count+=1
		GPIO.output(led, GPIO.HIGH)
		
			
			
	
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()
