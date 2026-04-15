from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 6789))
print('File server is running...')

while True:
    msg, addr = sock.recvfrom(BUF_SIZE)     # 'Hello' 메시지 수신
    if msg != b'Hello':
        continue
    else:
        print('client:', addr, msg.decode())

    sock.sendto(b'Filename', addr)           # 'Filename' 메시지 전송

    msg, addr = sock.recvfrom(BUF_SIZE)     # 파일 이름 수신
    filename = msg.decode()
    print('client:', addr, filename)

    try:
        filesize = os.path.getsize(filename)    # 파일 크기 확인
    except:
        sock.sendto(b'No File', addr)            # 파일 없을 경우
        print('파일 없음')
        continue

    f = open(filename, 'rb')
    data = f.read()
    f.close()

    # 최초 1번 + 재전송 2번 = 최대 3번
    sock.settimeout(2.0)                        # 2초 타임아웃
    for attempt in range(3):
        sock.sendto(data, addr)                  # 파일 전송
        print(f'{attempt + 1}번째 전송')

        try:
            msg, addr = sock.recvfrom(BUF_SIZE) # 'Bye' 수신 대기
            if msg == b'Bye':
                print('client:', addr, msg.decode())
                print('전송 완료')
                break

        except timeout:
            if attempt < 2:
                print('타임아웃! 재전송')
            else:
                print('전송 실패 (3회 초과)')

    sock.settimeout(None)                        # 타임아웃 해제