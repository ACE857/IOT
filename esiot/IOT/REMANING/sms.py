import requests
import json
import os
import RPi.GPIO as GPIO

HIGH  = 1
LOW  = 0
ir = 23
led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_UP)

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response

try:
    while(True):
        if GPIO.input(ir) == HIGH:
            print("object detected")
            response = sendPostRequest(URL, 'DIDM9LIGB65SLIQOB3S0CCWZLTWC2ZQO', '5H3V5M789T35NOED', 'stage', '9765484264', 'ABCDEF', 'Alert Object Detected' )
            break
except KeyboardInterrupt:
    GPIO.cleanup()

#
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)

