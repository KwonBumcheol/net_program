from socket import *
import struct
import random

# 센서 데이터 패킷 클래스
class SensorHdr:
    def __init__(self, sender, receiver, lumi, humid, temp, air, seq):
        self.sender   = sender      # 송신자 ID  (2바이트)
        self.receiver = receiver    # 수신자 ID  (2바이트)
        self.lumi     = lumi        # 조도       (1바이트)
        self.humid    = humid       # 습도       (1바이트)
        self.temp     = temp        # 온도       (1바이트)
        self.air      = air         # 기압       (1바이트)
        self.seq      = seq         # 순서번호   (4바이트)

    def pack_SensorHdr(self):
        # !: 빅엔디언, H: 2바이트, B: 1바이트, I: 4바이트
        # 총 2+2+1+1+1+1+4 = 12바이트
        packed = struct.pack('!HHBBBBI', self.sender, self.receiver, self.lumi, self.humid, self.temp, self.air, self.seq)
        return packed

# TCP 소켓 생성
s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5050))
s.listen(10)

print('서버 시작')

while True:
    c, addr = s.accept()            # 클라이언트 연결 수락

    data = c.recv(1024)             # 클라이언트 메시지 수신
    msg = data.decode()

    if msg == 'Hello':              # 'Hello' 수신 시 데이터 전송
        # 각 필드 랜덤 생성
        sensor = SensorHdr(
            sender   = random.randint(1, 50000),    # 송신자 ID
            receiver = random.randint(1, 50000),    # 수신자 ID
            lumi     = random.randint(1, 100),      # 조도
            humid    = random.randint(1, 100),      # 습도
            temp     = random.randint(1, 100),      # 온도
            air      = random.randint(1, 100),      # 기압
            seq      = random.randint(1, 100000)    # 순서번호
        )
        c.send(sensor.pack_SensorHdr())             # 12바이트 패킷 전송

    c.close()                       # 연결 종료
    

## UDP
# from socket import *
# import random

# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('localhost', 5050))

# print('서버 시작')

# while True:
#     data, addr = s.recvfrom(1024)
#     msg = data.decode()

#     if msg == 'Hello':
#         sender   = random.randint(1, 50000)
#         receiver = random.randint(1, 50000)
#         lumi     = random.randint(1, 100)
#         humid    = random.randint(1, 100)
#         temp     = random.randint(1, 100)
#         air      = random.randint(1, 100)
#         seq      = random.randint(1, 100000)

#         packet  = sender.to_bytes(2, 'big')
#         packet += receiver.to_bytes(2, 'big')
#         packet += lumi.to_bytes(1, 'big')
#         packet += humid.to_bytes(1, 'big')
#         packet += temp.to_bytes(1, 'big')
#         packet += air.to_bytes(1, 'big')
#         packet += seq.to_bytes(4, 'big')

#         s.sendto(packet, addr)