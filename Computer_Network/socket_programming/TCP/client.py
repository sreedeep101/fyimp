import socket

c = socket.socket()
print('client socket has been created')

SERVER_IP = 'localhost'
SERVER_PORT = 5000
c.connect((SERVER_IP , SERVER_PORT))

while True:
  RECIVED_MESSAGE = c.recv(1024).decode('utf-8')
  print('SERVER : ' , RECIVED_MESSAGE )

  if(RECIVED_MESSAGE == 'exiting...'):
    break

  MESSAGE_SEND = input('YOUR MESSAGE : ')
  c.send(bytes(MESSAGE_SEND,'utf-8'))

c.close()
print('client stoped')
  
