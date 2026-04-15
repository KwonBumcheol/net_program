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