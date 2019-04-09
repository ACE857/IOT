import RPi.GPIO as GPIO
import time
import requests

sensor = 29
buzzer = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Ready.....")
print (" ")
key = 0

try:
    while true:
      if GPIO.input(sensor):
          print ("Object Detected")
          #GPIO.output(buzzer,True)
          key = key+1
          if (key == 3):
          
              
              url = "https://smsapi.engineeringtgr.com/send/"
              params = dict(
                Mobile='8668277807',
                Password='P3365A',
                Key='krristNW4nJShoV2PgQ8jwqv',
                Message='Yo to IOT Lab',
                To='8698615856')
              resp = requests.get(url, params)
              print(resp, resp.text)
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()