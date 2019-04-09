import RPi.GPIO as GPIO
import time

CURRENT_FLOOR = 0
REQUESTED_FLOOR = 999

FLOOR0 = 17
FLOOR1 = 18
FLOOR2 = 19
FLOOR3 = 20

LED_RED_FLOOR0 = 6
LED_RED_FLOOR1 = 7
LED_RED_FLOOR2 = 8
LED_RED_FLOOR3 = 9

LED_GREEN_FLOOR0 = 10
LED_GREEN_FLOOR1 = 12
LED_GREEN_FLOOR2 = 13
LED_GREEN_FLOOR3 = 16

LED_YELLOW0 = 21
LED_YELLOW1 = 22
LED_YELLOW2 = 23
LED_YELLOW3 = 24
LED_YELLOW4 = 25
LED_YELLOW5 = 26
LED_YELLOW6 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOOR0, GPIO.IN)
GPIO.setup(FLOOR1, GPIO.IN)
GPIO.setup(FLOOR2, GPIO.IN)
GPIO.setup(FLOOR3, GPIO.IN)

GPIO.setup(LED_RED_FLOOR0, GPIO.OUT)
GPIO.setup(LED_RED_FLOOR1, GPIO.OUT)
GPIO.setup(LED_RED_FLOOR2, GPIO.OUT)
GPIO.setup(LED_RED_FLOOR3, GPIO.OUT)

GPIO.setup(LED_GREEN_FLOOR0, GPIO.OUT)
GPIO.setup(LED_GREEN_FLOOR1, GPIO.OUT)
GPIO.setup(LED_GREEN_FLOOR2, GPIO.OUT)
GPIO.setup(LED_GREEN_FLOOR3, GPIO.OUT)

GPIO.setup(LED_YELLOW0, GPIO.OUT)
GPIO.setup(LED_YELLOW1, GPIO.OUT)
GPIO.setup(LED_YELLOW2, GPIO.OUT)
GPIO.setup(LED_YELLOW3, GPIO.OUT)
GPIO.setup(LED_YELLOW4, GPIO.OUT)
GPIO.setup(LED_YELLOW5, GPIO.OUT)
GPIO.setup(LED_YELLOW6, GPIO.OUT)

def glow_red(floor, flag):
    if floor == 0:
        GPIO.output(LED_RED_FLOOR0, flag)
    if floor == 1:
        GPIO.output(LED_RED_FLOOR1, flag)
    if floor == 2:
        GPIO.output(LED_RED_FLOOR2, flag)
    if floor == 3:
        GPIO.output(LED_RED_FLOOR3, flag)

def glow_green(floor, flag):
    if floor == 0:
        GPIO.output(LED_GREEN_FLOOR0, flag)
    if floor == 1:
        GPIO.output(LED_GREEN_FLOOR1, flag)
    if floor == 2:
        GPIO.output(LED_GREEN_FLOOR2, flag)
    if floor == 3:
        GPIO.output(LED_GREEN_FLOOR3, flag)
        
def glow_yellow(floor, flag):
    if floor == 0:
        GPIO.output(LED_YELLOW0, flag)
    if floor == 1:
        GPIO.output(LED_YELLOW1, flag)
    if floor == 2:
        GPIO.output(LED_YELLOW2, flag)
    if floor == 3:
        GPIO.output(LED_YELLOW3, flag)
    if floor == 4:
        GPIO.output(LED_YELLOW4, flag)
    if floor == 5:
        GPIO.output(LED_YELLOW5, flag)
    if floor == 6:
        GPIO.output(LED_YELLOW6, flag)
    
def unglow_all_yellow():
    GPIO.output(LED_YELLOW0, False)
    GPIO.output(LED_YELLOW1, False)
    GPIO.output(LED_YELLOW2, False)
    GPIO.output(LED_YELLOW3, False)
    GPIO.output(LED_YELLOW4, False)
    GPIO.output(LED_YELLOW5, False)
    GPIO.output(LED_YELLOW6, False)
    
def unglow_all_green():
    GPIO.output(LED_GREEN_FLOOR0, False)
    GPIO.output(LED_GREEN_FLOOR1, False)
    GPIO.output(LED_GREEN_FLOOR2, False)
    GPIO.output(LED_GREEN_FLOOR3, False)

def glow_yellow_down(cur_floor, req_floor):
    global CURRENT_FLOOR
    
    unglow_all_yellow()
    

    for i in range(cur_floor, req_floor-1, -1):
        unglow_all_yellow()
        glow_yellow(2*i, True)
        CURRENT_FLOOR = i
        unglow_all_green()
        glow_green(CURRENT_FLOOR, True)
        time.sleep(1)
    
        if CURRENT_FLOOR != REQUESTED_FLOOR:
            unglow_all_yellow()
            glow_yellow(2*i-1, True)
            time.sleep(1)
        
    
    unglow_all_yellow()
    
def glow_yellow_up(cur_floor, req_floor):
    global CURRENT_FLOOR
    
    unglow_all_yellow()
    

    for i in range(cur_floor, req_floor+1):
        unglow_all_yellow()
        glow_yellow(2*i, True)
        CURRENT_FLOOR = i
        unglow_all_green()
        glow_green(CURRENT_FLOOR, True)
        time.sleep(1)
    
        if CURRENT_FLOOR != REQUESTED_FLOOR:
            unglow_all_yellow()
            glow_yellow(2*i+1, True)
            time.sleep(1)
        
    
    unglow_all_yellow()
        

glow_green(CURRENT_FLOOR, True)
    

try:
    while True :
        global CURRENT_FLOOR
        
        print(CURRENT_FLOOR, REQUESTED_FLOOR)
        
        if not GPIO.input(FLOOR0):
            print("Ground Call")
            REQUESTED_FLOOR = 0
            glow_red(REQUESTED_FLOOR, True)
            time.sleep(0.5)
        if not GPIO.input(FLOOR1):
            print("First Floor Call")
            REQUESTED_FLOOR = 1
            glow_red(REQUESTED_FLOOR, True)
            time.sleep(0.5)
        if not GPIO.input(FLOOR2):
            print("Second Floor Call")
            REQUESTED_FLOOR = 2
            glow_red(REQUESTED_FLOOR, True)
            time.sleep(0.5)
        if not GPIO.input(FLOOR3):
            print("Third Floor Call")
            REQUESTED_FLOOR = 3
            glow_red(REQUESTED_FLOOR, True)
            time.sleep(0.5)
            
        
        if REQUESTED_FLOOR == CURRENT_FLOOR:
            glow_red(CURRENT_FLOOR, False)
            continue
        
        if REQUESTED_FLOOR < 4:
            if CURRENT_FLOOR < REQUESTED_FLOOR:
                glow_yellow_up(CURRENT_FLOOR, REQUESTED_FLOOR)
            else:
                glow_yellow_down(CURRENT_FLOOR, REQUESTED_FLOOR)
            
            
except KeyboardInterrupt :
    
    GPIO.output(LED_RED_FLOOR0, False)
    GPIO.output(LED_RED_FLOOR1, False)
    GPIO.output(LED_RED_FLOOR2, False)
    GPIO.output(LED_RED_FLOOR3, False)
    
    GPIO.output(LED_GREEN_FLOOR0, False)
    GPIO.output(LED_GREEN_FLOOR1, False)
    GPIO.output(LED_GREEN_FLOOR2, False)
    GPIO.output(LED_GREEN_FLOOR3, False)
    
    GPIO.output(LED_YELLOW0, False)
    GPIO.output(LED_YELLOW1, False)
    GPIO.output(LED_YELLOW2, False)
    GPIO.output(LED_YELLOW3, False)
    GPIO.output(LED_YELLOW4, False)
    GPIO.output(LED_YELLOW5, False)
    GPIO.output(LED_YELLOW6, False)
    
    GPIO.cleanup()
