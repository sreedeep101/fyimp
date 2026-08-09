import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print('server socket created successfully')    

ip = 'localhost'
port = 5000
s.bind((ip,port))
print('server running in the socket : ' , ip ,':',port)
s.listen(3)
print('waiting for the client...')

c,address = s.accept()
print('connection established with the client : ', address)
c.send(bytes('Welcome to the server!!','utf-8'))

while True:
  message = c.recv(1024).decode('utf-8')
  print('client : ',message)
  if( message == 'bye'):
    c.send(bytes('exiting...','utf-8'))
    break

  replay = input('Replay : ')
  c.send(bytes(replay,'utf-8'))

s.close()
print('server Stopped')
