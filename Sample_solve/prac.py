from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(10)

print('서버 시작')

c, addr = s.accept()

while True:
    data = c.recv(1024)
    msg = data.decode()

    if msg == 'ping':
        c.send(b'pong')

c.close()