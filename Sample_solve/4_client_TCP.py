from socket import *
import struct

while True:
    for req in ['1', '2', '3']:
        s = socket(AF_INET, SOCK_STREAM)       # TCP
        s.connect(('localhost', 9999))          # 연결

        s.send(req.encode())                    # '1', '2', '3' 문자열 전송

        # 6바이트 수신 (기존 코드 방식 그대로)
        data = b''
        while len(data) < 6:
            pack = s.recv(6 - len(data))
            if not pack:
                break
            data += pack

        if len(data) == 6:
            # temp  = int.from_bytes(data[0:2], 'big')
            # humid = int.from_bytes(data[2:4], 'big')
            # lumi  = int.from_bytes(data[4:6], 'big')
            temp, humid, lumi = struct.unpack('>HHH', data)
            print(f'Temp={temp}, Humid={humid}, Lumi={lumi}')

        s.close()                               # 매번 연결 종료
        
## 클 1 서버 2
# from socket import *

# while True:
#     D = input('서버 선택 (1/2/quit): ')

#     if D == 'quit':
#         break

#     if D == '1':
#         port = 9999
#     elif D == '2':
#         port = 8888
#     else:
#         continue

#     for req in ['1', '2', '3']:
#         s = socket(AF_INET, SOCK_STREAM)      # 매번 새 소켓 생성
#         s.connect(('localhost', port))         # 해당 서버에 연결

#         s.send(req.encode())

#         data = b''
#         while len(data) < 6:
#             pack = s.recv(6 - len(data))
#             if not pack:
#                 break
#             data += pack

#         if len(data) == 6:
#             temp  = int.from_bytes(data[0:2], 'big')
#             humid = int.from_bytes(data[2:4], 'big')
#             lumi  = int.from_bytes(data[4:6], 'big')
#             print(f'서버{D} - Temp={temp}, Humid={humid}, Lumi={lumi}')

#         s.close()

## 1, 2, 3 input()
# from socket import *

# while True:
#     D = input('서버 선택 (1/2/quit): ')

#     if D == 'quit':
#         break

#     if D == '1':
#         port = 9999
#     elif D == '2':
#         port = 8888
#     else:
#         continue

#     # ✅ 변경된 부분
#     req = input('요청 선택 (1/2/3): ')

#     if req not in ['1', '2', '3']:
#         continue

#     s = socket(AF_INET, SOCK_STREAM)
#     s.connect(('localhost', port))

#     s.send(req.encode())

#     data = b''
#     while len(data) < 6:
#         pack = s.recv(6 - len(data))
#         if not pack:
#             break
#         data += pack

#     if len(data) == 6:
#         temp  = int.from_bytes(data[0:2], 'big')
#         humid = int.from_bytes(data[2:4], 'big')
#         lumi  = int.from_bytes(data[4:6], 'big')
#         print(f'서버{D} - Temp={temp}, Humid={humid}, Lumi={lumi}')

#     s.close()
