from socket import *
import random

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('localhost', 9999))

print('서버 시작')

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    print(f'수신: {msg}')

    # 25% 확률로 손실 발생
    if random.random() < 0.25: # if random.random() <= 0.25: - 차이 없음
        print('손실 발생 (응답 안 함)')
        continue

    s.sendto(msg.encode(), addr)    # 수신한 메시지 그대로 응답
    
## TCP
# from socket import *
# import random

# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('localhost', 9999))
# s.listen(10)

# print('서버 시작')

# while True:
#     c, addr = s.accept()

#     data = c.recv(1024)
#     msg = data.decode()
#     print(f'수신: {msg}')

#     # 25% 확률로 손실 발생
#     if random.random() < 0.25:
#         print('손실 발생 (응답 안 함)')
#         c.close()
#         continue

#     c.send(msg.encode())            # 수신한 메시지 그대로 응답
#     c.close()