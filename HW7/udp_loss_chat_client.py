import socket

port = 3333
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('-> ')
    
    if msg == 'q':
        sock.sendto(msg.encode(), ('localhost', port))
        break
    
    # 메시지 전송 부분
    # 'ack' 응답 메시지를 수신하지 못하는 경우, 2초 간격으로 최대 5회 재전송 (총 6회)
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)  # 2초 간격 재전송을 위한 소켓의 timeout 설정
 
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except socket.timeout:
            reTx += 1
            continue
        else:
            break
        
    # 서버로부터 메시지 수신 부분
    sock.settimeout(None)  # 블로킹 모드로 전환
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<-', data.decode())
    sock.sendto(b'ack', addr)  # 서버에 ack 전송
 
    if data.decode().split(' ', 1)[-1] == 'q':
        break
 
    
sock.close()