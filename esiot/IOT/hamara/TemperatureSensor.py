import os
import glob
import time
import requests
import time
import smtplib

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      return temp_c


def send_mail(body):
    print("Sending Mail")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("ccaabhi@gmail.com", "abhinayS1!") 
    print("Logged In.")
    message = "SUBJECT: " + body + "\nTemp Sensed: " + str("ae yo !");
      
    s.sendmail("ccaabhi@gmail.com", "srjbsht857@gmail.com", message)
    print("Mail Sent.")
    s.quit()
    
i=1
while(True):
    current_temp = read_temp()
    print(current_temp)
    if current_temp > 33:
        send_mail("Temperature has peaked.")
    