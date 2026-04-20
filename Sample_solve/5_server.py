from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(10)

print('서버 시작')

c, addr = s.accept()

while True:
    data = c.recv(1024)
    
    if not data:
        break
    
    msg = data.decode()

    if msg == 'ping':
        c.send(b'pong')

c.close()

## UDP
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('localhost', 7000))

# print('서버 시작')

# while True:
#     data, addr = s.recvfrom(1024)
#     msg = data.decode()

#     if msg == 'ping':
#         s.sendto(b'pong', addr)