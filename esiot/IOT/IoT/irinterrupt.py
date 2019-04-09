import RPi.GPIO as GPIO
import time  

GPIO.setmode(GPIO.BCM)  
      
    # GPIO 5 set up as input, pulled up to avoid false detection.  
    # port wired to connect to GND on button press.  
    # So we'll be setting up falling edge detection   
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

GPIO.setup(3,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT) 
            
    # now we'll define two threaded callback functions  
    # these will run in another thread when our events are detected  
def my_callback(channel):  
	GPIO.output(3,0)
	GPIO.output(23,0)
	GPIO.output(24,0)  
	time.sleep(0.1)
          
         
    # when a falling edge is detected on port 5, regardless of whatever   
    # else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback, bouncetime=10)  
      
          
try: 
	while 1:
		GPIO.output(3,1)
		GPIO.output(23,1)
		GPIO.output(24,1)  
		time.sleep(1)
      
except KeyboardInterrupt:  
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
	GPIO.cleanup()           # clean up GPIO on normal exit  