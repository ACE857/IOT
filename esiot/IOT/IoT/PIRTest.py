import time
import RPi.GPIO as GPIO 

RUNNING = True

HIGH  = 1
LOW  = 0
PIRPin = 17
Buzzer = 6

def InitSystem():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIRPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(Buzzer,GPIO.OUT)
	
	return



def DetectPerson():
	#while True:
	input_state = GPIO.input(PIRPin)
	time.sleep(0.3)	
	if input_state == 0:
		return LOW
	else:
		return HIGH
			
	
			
			
try:
	print "\n\n         Home Automation Testing\n\n"
	print  "-----------------------------------------------\n" 	
	InitSystem()
	count =0;
	count_flag =0
	door_flag =0
	elapsed =0
	start = time.time()
	while RUNNING:
		state = DetectPerson()
		if state == LOW:
			GPIO.output(Buzzer,1)
			time.sleep(1)
			GPIO.output(Buzzer,0)
			
			#print "Waiting for Next Person. Time elapsed %d\n" %elapsed
			
				
		elapsed = time.time() - start
		if elapsed > 120:		#2 min timeout
			print "\nTimeout Occured. Restart Program"
			break;
			
	
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\nStopping"
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()
