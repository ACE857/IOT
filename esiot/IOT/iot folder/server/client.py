import socket               

s = socket.socket()        
host = ''# ip of raspberry pi 
port = 1234               
s.connect((host, port))
print(s.recv(1024))
s.close()