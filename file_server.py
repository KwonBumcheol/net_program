from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',7777))
sock.listen(10)
print('File server is running...')

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE) # 'Hello' 메시지 수신
    if not msg:
        conn.close()
        continue    # 다음 클라이언트 대기
    elif msg != b'Hello':
        print('client:', addr, msg.decode())
        conn.close()
        continue
    else:
        print('client:', addr, msg.decode())
    # 'Filename' 메시지 전송
    conn.send(b'Filename')
    # 파일 이름 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    print('client:', addr, filename)
    
    try:
        filesize = os.path.getsize(filename)    # 해당 파일 크기 확인
    except:
        conn.send(b'Nofile')
        conn.close()
        continue
    else:       # 파일 크기 전송
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)
    
    f = open(filename, 'rb')    # 파일 열기
    data = f.read()             # 파일 읽기
    conn.sendall(data)          # 파일 전송
    
    msg = conn.recv(BUF_SIZE)   # 'Bye' 메시지 수신
    if not msg:
        pass
    else:
        print('client:', addr, msg.decode())
    
    f.close()
    conn.close()