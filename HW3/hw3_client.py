from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5555))

while True:
    msg = input('Calculate to send: ')
    if msg == 'q':
        break
    
    s.send(msg.encode())
    
    print('Result: ', s.recv(1024).decode())
    
s.close()