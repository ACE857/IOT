from gpiozero import LED
from signal import pause
import RPi.GPIO as GPIO
import time
import urllib2
import cookielib
from getpass import getpass
username = "7378658056"
passwd = "Manishtisu1998"
message = "hello mummy ji"
number = ["8698604931","8698600586","7889523902"]
message = "+".join(message.split(' '))

#Logging into the SMS Site
url = 'http://site24.way2sms.com/Login1.action?'
dat = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
#Cookies are to be handled
	
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# a Web browser is visiting the site
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

GPIO.setmode(GPIO.BCM)
LED_PIN = 27
IR_PIN = 5
indicator = LED(LED_PIN)
GPIO.setup(IR_PIN,GPIO.IN)
count =1



while(True) :
        got_something = GPIO.input(IR_PIN)
        if(got_something):
            indicator.on()
            print("{:>3} not yet".format(count))
        else :
            indicator.off()
            print("{:>3}detected".format(count))
            i=0
            while(i<1):
                x=str(i)+".jpg"
                data = urllib2.urlopen("http://10.53.53.152:8080/photo.jpg")
                image = open(x,"wb")
                image.write(data.read())
                image.close()
                time.sleep(1)
                i+=1
                
                try:
                    usock = opener.open(url, dat)
                except Exception:
                    print ("Error while logging in.")
                for j in number:
                    jession_id = str(cj).split('~')[1].split(' ')[0]
                    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
                    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+j+'&message='+message+'&msgLen=136'
                    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
                    try:
                        sms_sent_page = opener.open(send_sms_url,send_sms_data)
                    except Exception:
                        print ("Error while sending message")
                    print ("SMS has been sent.")
                                
                
                
                
                
                
        count+=1
        time.sleep(0.2)

                

