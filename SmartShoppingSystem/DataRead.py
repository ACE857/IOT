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


Dict = {}
user = ""

def dataread(id,text):
    text=text.strip()
    if(len(text)<=0):
        return ""
    if len(text)>0 and text[0]=='u' :
        return text
    if text not in Dict.keys() :
        Dict[text] = { 'id' : [ id ], 'text' : text }
    else :
        if id not in Dict[text]['id'] :
            Dict[text]['id'].append(id)
    print("\n\n\nThis is new list\n")
    print(Dict)
    return ""
    
# end of read data function

def uploadlist(u):
    ref = db.reference("shoppingCart/"+u+'/cart')
    ref2 = db.reference("shoppingCart/"+u+'/user')
    ref2.update({
            "userid" : u
            })
    for x in Dict.keys() :
        print("THIS IS X : "+x)
        ref.update({
            Dict[x]['text'].strip() :
                {
                    'price' : "10",
                    'text' : Dict[x]['text'].strip(),
                    'qty' : str(len(Dict[x]['id']))
                }
            })

                
y=0
z=""
while(1):
    
    try:
            id, text = reader.read()
            x = dataread(id,text)
            if(len(x)>0):
                x=x.strip()
                z=x
            print("user is "+ z)
            if(len(z)>0):
                uploadlist(z)
            
    finally:
            GPIO.cleanup()



    










