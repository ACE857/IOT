#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('shanks-18d6d-firebase-adminsdk-lgquf-adc900e6a1.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://shanks-18d6d.firebaseio.com/'
})

reader = SimpleMFRC522()

def checkForData():
    ref = db.reference('newProduct/bool')
    while True :
        x = str(ref.get())
        if x!="false" :
            break;
    ref = db.reference('newProduct/productName')
    return str(ref.get())

def writeData(text) :
    print("now please scan your card")
    reader.write(text)
    print("Written")

try:
        print("Wating for user input....")
        data = checkForData()
        print("vola Product Found "+data)
        writeData(data)
        
finally:
        GPIO.cleanup()