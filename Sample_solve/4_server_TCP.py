from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(10)

print('서버 시작')

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()        # '1', '2', '3'

    temp  = 0
    humid = 0
    lumi  = 0

    if msg == '1':
        temp = random.randint(1, 50)
    elif msg == '2':
        humid = random.randint(1, 100)
    elif msg == '3':
        lumi = random.randint(1, 150)

    # 2바이트씩 빅엔디언으로 변환 후 전송 (6바이트)
    packet  = temp.to_bytes(2, 'big')
    packet += humid.to_bytes(2, 'big')
    packet += lumi.to_bytes(2, 'big')

    c.send(packet)
    c.close()