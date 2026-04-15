from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))

for i in range(3):
    s.send(b'ping')
    send_time = time.time()         # 보낸 시간 기록

    data = s.recv(1024)
    recv_time = time.time()         # 받은 시간 기록

    rtt = recv_time - send_time     # RTT 계산
    print(f'Success (RTT: {rtt:.6f})')

s.close()

## UDP
# from socket import *
# import time

# s = socket(AF_INET, SOCK_DGRAM)
# addr = ('localhost', 7000)

# for i in range(3):
#     s.sendto(b'ping', addr)
#     send_time = time.time()         # 보낸 시간 기록

#     data, _ = s.recvfrom(1024)
#     recv_time = time.time()         # 받은 시간 기록

#     rtt = recv_time - send_time
#     print(f'Success (RTT: {rtt:.6f})')