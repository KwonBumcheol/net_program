from socket import *

BUFF_SIZE = 1024
port = 9999

sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(1.0)                # 1초 타임아웃

while True:
    msg = input('전송: ')

    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
        break
    
    reTx = 0
    while reTx < 3:
        sock.sendto(msg.encode(), ('localhost', port))
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            print(data.decode())
            break
        except timeout:
            reTx += 1
            print('재전송')
            
    # 최초 1번 + 재전송 2번 = 최대 3번
    # for attempt in range(3):
    #     sock.sendto(msg.encode(), ('localhost', port))
    #     print(f'{attempt + 1}번째 전송')

    #     try:
    #         data, addr = sock.recvfrom(BUFF_SIZE)
    #         print(data.decode())
    #         break                   # 수신 성공 시 종료

    #     except timeout:
    #         if attempt < 2:
    #             print('타임아웃! 재전송')
    #         else:
    #             print('전송 실패 (3회 초과)')
    
sock.close()
                

## TCP
# from socket import *

# while True:
#     msg = input('전송: ')

#     # 최초 1번 + 재전송 2번 = 최대 3번
#     for attempt in range(3):

#         s = socket(AF_INET, SOCK_STREAM)
#         s.settimeout(1.0)               # 1초 타임아웃
#         s.connect(('localhost', 9999))

#         s.send(msg.encode())
#         print(f'{attempt + 1}번째 전송')

#         try:
#             data = s.recv(1024)
#             print(f'수신: {data.decode()}')
#             s.close()
#             break                       # 수신 성공 시 종료

#         except timeout:
#             if attempt < 2:
#                 print('타임아웃! 재전송')
#             else:
#                 print('전송 실패 (3회 초과)')
        
#         s.close()

## 손실이 서버 -> 클라이언트 보내는 경우 (기출과 반대 상황)
# from socket import *

# s = socket(AF_INET, SOCK_DGRAM)
# s.settimeout(1.0)           # 1초 타임아웃
# addr = ('localhost', 9999)
# MAX_RETRY = 2               # 최대 재전송 횟수 (최초 전송 포함 총 3번)

# while True:
#     msg = input('메시지 입력: ')

#     for attempt in range(MAX_RETRY + 1):    # attempt: 0, 1, 2
#         if attempt == 0:
#             print(f'[전송] "{msg}"')
#         else:
#             print(f'[재전송 {attempt}/{MAX_RETRY}] "{msg}"')

#         s.sendto(msg.encode(), addr)

#         try:
#             data, _ = s.recvfrom(1024)
#             print(f'[수신] "{data.decode()}"')
#             break                           # 수신 성공 → 재전송 루프 탈출

#         except timeout:
#             if attempt < MAX_RETRY:
#                 print('[타임아웃] 1초 내 응답 없음 → 재전송')
#             else:
#                 print('[실패] 최대 재전송 횟수(2회) 초과 → 포기')