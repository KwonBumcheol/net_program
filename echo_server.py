from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    if not data:    # data 빈 bytes 객체일 경우 -> 무한루프 탈출
        break
    print("Received message: ", data.decode())
    
    conn.send(data)

conn.close()
sock.close()