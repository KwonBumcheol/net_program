from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

s.send(b'Hello')    # 1. 'Hello' 메시지 전송

msg = s.recv(BUF_SIZE)  # 2. 'Filename' 메시지 수신
if not msg:
    s.close()
    sys.exit()
elif msg != b'Filename':    # 예외처리: 'Filename'이 안 온 경우
    print('server:', msg.decode())
    s.close()
    sys.exit()
else:
    print('server:', msg.decode())

filename = input('Enter a filename: ')
s.send(filename.encode()) # 파일 이름 전송

msg = s.recv(BUF_SIZE)  # 파일 크기 수신
if not msg:
    s.close()
    sys.exit()
elif msg == b'Nofile':      # 예외처리: 'Nofile' 파일이 없는 경우를 받으면
    print('server:', msg.decode())
    s.close()
    sys.exit()
else:
    rx_size = len(msg)
    data = msg
    while rx_size < LENGTH: # 파일 크기 4바이트씩 받기
        msg = s.recv(BUF_SIZE)
        if not msg:
            s.close()
            sys.exit()
        data = data + msg
        rx_size += len(msg)
    if rx_size < LENGTH:
        s.close()
        sys.exit()
    filesize = int.from_bytes(data, 'big')
    print('server:', filesize)  # 4바이트
    
rx_size = 0
f = open(filename, 'wb')        # 파일 열기
while rx_size < filesize:       # 실제 파일 수신
    data = s.recv(BUF_SIZE)
    if not data:
        break
    f.write(data)
    rx_size += len(data)
    
if rx_size < filesize:
    s.close()
    sys.exit()

print('Download complete')
s.send(b'Bye')
f.close()
s.close()
