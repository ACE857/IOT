import time
import RPi.GPIO as GPIO 
import smtplib 
import time

RUNNING = True

HIGH  = 1
LOW  = 0
DetectPin = 5

def send_mail(body):
    print("Sending Mail")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("ccaabhi@gmail.com", "abhinayS1!") 
    print("Logged In.")
    message = "SUBJECT: " + body + "\nBODY: " + body + str(time.time());
      
    s.sendmail("ccaabhi@gmail.com", "malikpankaj66@gmail.com", message)
    print("Mail Sent.")
    s.quit()

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DetectPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return

def DetectPerson():
    while True:
        input_state = GPIO.input(DetectPin)
        time.sleep(0.3)	
        if input_state == 0:
            return LOW
        else:
            return HIGH                         
                    
try:
    InitSystem()
    count = 0;
    while RUNNING:
        state = DetectPerson()
        if state == HIGH:
            print("Object Detected")
            send_mail("Object Detected")
	
except KeyboardInterrupt:
    RUNNING = False
    print("\Stopping Program.")
 
finally:
    GPIO.cleanup()
