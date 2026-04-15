from socket import *
import struct

# 수신한 12바이트 버퍼를 언패킹
def unpack_SensorHdr(buffer):
    # !: 빅엔디언, H: 2바이트, B: 1바이트, I: 4바이트
    unpacked = struct.unpack('!HHBBBBI', buffer[:12])
    return unpacked

# 각 필드값을 가져오는 함수
def getSender(u):   return u[0]     # 송신자 ID
def getReceiver(u): return u[1]     # 수신자 ID
def getLumi(u):     return u[2]     # 조도
def getHumid(u):    return u[3]     # 습도
def getTemp(u):     return u[4]     # 온도
def getAir(u):      return u[5]     # 기압
def getSeq(u):      return u[6]     # 순서번호

# TCP 소켓 생성 및 서버 연결
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5050))

s.send(b'Hello')                    # 'Hello' 전송

# 12바이트 수신 (TCP는 한 번에 안 올 수 있으므로 누적)
data = b''
while len(data) < 12:
    pack = s.recv(12 - len(data))   # 남은 바이트만큼 수신
    if not pack:
        break
    data += pack                    # 누적

# 수신 완료 시 언패킹 후 출력
if len(data) == 12:
    u = unpack_SensorHdr(data)
    print(f'Sender:{getSender(u)}, Receiver:{getReceiver(u)}, '
          f'Lumi:{getLumi(u)}, Humi:{getHumid(u)}, '
          f'Temp:{getTemp(u)}, Air:{getAir(u)}, Seq:{getSeq(u)}')

s.close()                           # 연결 종료

## TCP 다른 코드
# from socket import *

# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 5050))

# s.send(b'Hello')

# # 12바이트 수신
# data = b''
# while len(data) < 12:
#     pack = s.recv(12 - len(data))
#     if not pack:
#         break
#     data += pack

# if len(data) == 12:
#     sender   = int.from_bytes(data[0:2],  'big')
#     receiver = int.from_bytes(data[2:4],  'big')
#     lumi     = int.from_bytes(data[4:5],  'big')
#     humid    = int.from_bytes(data[5:6],  'big')
#     temp     = int.from_bytes(data[6:7],  'big')
#     air      = int.from_bytes(data[7:8],  'big')
#     seq      = int.from_bytes(data[8:12], 'big')

#     print(f'Sender:{sender}, Receiver:{receiver}, Lumi:{lumi}, Humi:{humid}, Temp:{temp}, Air:{air}, Seq:{seq}')

# s.close()


## UDP
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)
# addr = ('localhost', 5050)

# s.sendto(b'Hello', addr)

# data, _ = s.recvfrom(1024)          # UDP는 한 번에 수신

# if len(data) == 12:
#     sender   = int.from_bytes(data[0:2],  'big')
#     receiver = int.from_bytes(data[2:4],  'big')
#     lumi     = int.from_bytes(data[4:5],  'big')
#     humid    = int.from_bytes(data[5:6],  'big')
#     temp     = int.from_bytes(data[6:7],  'big')
#     air      = int.from_bytes(data[7:8],  'big')
#     seq      = int.from_bytes(data[8:12], 'big')

#     print(f'Sender:{sender}, Receiver:{receiver}, Lumi:{lumi}, Humi:{humid}, Temp:{temp}, Air:{air}, Seq:{seq}')