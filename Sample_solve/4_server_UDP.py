from socket import *
import random

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('localhost', 9999))

print('서버 시작')

while True:
    data, addr = s.recvfrom(1024)
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

    s.sendto(packet, addr)
    
## 손실복구 25% 응답 x
# from socket import *
# import random

# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('localhost', 9999))

# print('서버 시작')

# while True:
#     data, addr = s.recvfrom(1024)
#     msg = data.decode()

#     temp  = 0
#     humid = 0
#     lumi  = 0

#     if msg == '1':
#         temp = random.randint(1, 50)
#     elif msg == '2':
#         humid = random.randint(1, 100)
#     elif msg == '3':
#         lumi = random.randint(1, 150)

#     # ✅ 25% 확률로 손실 발생
#     if random.random() < 0.25:
#         print('손실 발생 (응답 안 함)')
#         continue                        # 응답 안 하고 넘어감

#     packet  = temp.to_bytes(2, 'big')
#     packet += humid.to_bytes(2, 'big')
#     packet += lumi.to_bytes(2, 'big')

#     s.sendto(packet, addr)