from socket import *

s = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', 9999)

while True:
    for req in ['1', '2', '3']:
        s.sendto(req.encode(), addr)        # '1', '2', '3' 전송

        data, _ = s.recvfrom(1024)          # 6바이트 수신

        temp  = int.from_bytes(data[0:2], 'big')
        humid = int.from_bytes(data[2:4], 'big')
        lumi  = int.from_bytes(data[4:6], 'big')
        print(f'Temp={temp}, Humid={humid}, Lumi={lumi}')
        
## 클 1, 서버 2
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)

# addr1 = ('localhost', 9999)      # 서버1 주소
# addr2 = ('localhost', 8888)      # 서버2 주소

# while True:
#     D = input('서버 선택 (1/2/quit): ')

#     if D == 'quit':
#         break

#     if D == '1':
#         addr = addr1
#     elif D == '2':
#         addr = addr2
#     else:
#         continue

#     for req in ['1', '2', '3']:
#         s.sendto(req.encode(), addr)

#         data, _ = s.recvfrom(1024)

#         temp  = int.from_bytes(data[0:2], 'big')
#         humid = int.from_bytes(data[2:4], 'big')
#         lumi  = int.from_bytes(data[4:6], 'big')
#         print(f'서버{D} - Temp={temp}, Humid={humid}, Lumi={lumi}')

## 1, 2, 3 input()
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)

# while True:
#     D = input('서버 선택 (1/2/quit): ')

#     if D == 'quit':
#         break

#     if D == '1':
#         addr = ('localhost', 9999)
#     elif D == '2':
#         addr = ('localhost', 8888)
#     else:
#         continue

#     # ✅ 변경된 부분
#     req = input('요청 선택 (1/2/3): ')

#     if req not in ['1', '2', '3']:
#         continue

#     s.sendto(req.encode(), addr)

#     data, _ = s.recvfrom(1024)

#     temp  = int.from_bytes(data[0:2], 'big')
#     humid = int.from_bytes(data[2:4], 'big')
#     lumi  = int.from_bytes(data[4:6], 'big')
#     print(f'서버{D} - Temp={temp}, Humid={humid}, Lumi={lumi}')

## 손실복구 - 1초간격 2회전송
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)
# s.settimeout(1.0)                       # 1초 타임아웃
# addr = ('localhost', 9999)

# while True:
#     req = input('요청 선택 (1/2/3): ')

#     if req not in ['1', '2', '3']:
#         continue

#     # ✅ 최대 3번 전송 (최초 1번 + 재전송 2번)
#     for attempt in range(3):
#         s.sendto(req.encode(), addr)
#         print(f'전송 {attempt + 1}회')

#         try:
#             data, _ = s.recvfrom(1024)

#             temp  = int.from_bytes(data[0:2], 'big')
#             humid = int.from_bytes(data[2:4], 'big')
#             lumi  = int.from_bytes(data[4:6], 'big')
#             print(f'Temp={temp}, Humid={humid}, Lumi={lumi}')
#             break                       # 수신 성공 시 반복 종료

#         except timeout:
#             print(f'타임아웃! 재전송')
#             continue                    # 재전송
#     else:
#         print('전송 실패 (3회 초과)')   # 3번 모두 실패 시