from socket import *

s = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', 6789)

s.sendto(b'Hello', addr)                # Hello 전송

data, _ = s.recvfrom(1024)
if data.decode() == 'Filename':
    filename = input('파일 이름 입력: ')
    s.sendto(filename.encode(), addr)   # 파일 이름 전송

    data, _ = s.recvfrom(65536)         # 파일 수신
    msg = data.decode('utf-8', errors='ignore')

    if msg == 'No File':
        print('파일 없음')
    else:
        f = open(filename, 'wb')
        f.write(data)
        f.close()
        print('파일 수신 완료')

    s.sendto(b'Bye', addr)              # Bye 전송