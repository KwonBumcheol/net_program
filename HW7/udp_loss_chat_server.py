import socket
import random

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    # 클라이언트로부터 메시지 수신 부분
    # 메시지 수신 후, 50% 확률로 응답하지 않고, 50% 확률로 'ack' 응답 메시지를 클라이언트로 전송
    sock.settimeout(None)   # 소켓의 블로킹 모드 설정. None인 경우, 무한정 블로킹됨
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
        
    # 클라이언트로 메시지 전송 부분
    # 'ack' 응답 메시지를 수신하지 못하는 경우, 2초 간격으로 최대 5회 재전송 (총 6회)
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)  # 2초 간격 재전송을 위한 소켓의 timeout 설정
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:
            reTx += 1
            continue
        else:
            break