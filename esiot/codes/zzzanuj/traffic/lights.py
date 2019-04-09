import RPi.GPIO as GPIO
import time


LED_RED_1 = 18
LED_RED_2 = 26
LED_GREEN_1 =14
LED_GREEN_2 = 22
LED_YELLOW_1 = 15
LED_YELLOW_2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_1,GPIO.OUT)
GPIO.setup(LED_YELLOW_1,GPIO.OUT)
GPIO.setup(LED_GREEN_1,GPIO.OUT)
GPIO.setup(LED_RED_2,GPIO.OUT)

GPIO.setup(LED_GREEN_2,GPIO.OUT)

GPIO.setup(LED_YELLOW_2,GPIO.OUT)

def red1(flag):
    if flag:
        GPIO.output(LED_RED_1,True)
    else:
        GPIO.output(LED_RED_1,False)

def red2(flag):
    if flag:
        GPIO.output(LED_RED_2,True)
    else:
        GPIO.output(LED_RED_2,False)
        
def green1(flag):
    if flag:
        GPIO.output(LED_GREEN_1,True)
    else:
        GPIO.output(LED_GREEN_1,False)
        
def green2(flag):
    if flag:
        GPIO.output(LED_GREEN_2,True)
    else:
        GPIO.output(LED_GREEN_2,False)
        
def yellow1(flag):
    if flag:
        GPIO.output(LED_YELLOW_1,True)
    else:
        GPIO.output(LED_YELLOW_1,False)
        
def yellow1(flag):
    if flag:
        GPIO.output(LED_YELLOW_2,True)
    else:
        GPIO.output(LED_YELLOW_2,False)


GPIO.output(LED_RED_1,False)
GPIO.output(LED_YELLOW_1,False)
GPIO.output(LED_GREEN_1,False)
GPIO.output(LED_RED_2,False)


GPIO.output(LED_GREEN_2,False)

GPIO.output(LED_YELLOW_2,False)

print("djnfd")

try: 
   while True:
       GPIO.output(LED_RED_1,True)
       GPIO.output(LED_YELLOW_1,True)
       GPIO.output(LED_GREEN_1,True)
       GPIO.output(LED_RED_2,True)
       print("kgfxdgf");
       
       
       GPIO.output(LED_GREEN_2,True)
       
       GPIO.output(LED_YELLOW_2,True)
       time.sleep(0.5)


except KeyboardInterrupt:
    GPIO.cleanup()
