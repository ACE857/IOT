import socket

s = socket.socket()
host = '' #ip of raspberry pi
port = 1234
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Thank you for connecting ..........this is the code for iot')
  c.close()