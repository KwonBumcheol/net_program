import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6000))

while True:
    sock.send(b'start')
    
    # 이미지 크기 정보 확인
    rx_size = 0 # 받은 총 이미지 데이터 저장용
    data = b''  # 수신한 크기 정보 저장
    while rx_size < LENGTH:     # 이미지 데이터 수신
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        data = data + rx_buf
        rx_size += len(rx_buf)
        
    if rx_size < LENGTH:
        break
    
    frame_len = int(data)
    
    sock.send(b'image')
    
    # 실제 이미지 송.수신
    rx_size = 0
    byteData = b''
    while rx_size < frame_len:
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        byteData = byteData + rx_buf
        rx_size += len(rx_buf)
        
    if rx_size < frame_len:
        break
    
    data = np.frombuffer(byteData, dtype='uint8')
    imgDecode = cv2.imdecode(data, 1)
    cv2.imshow('image', imgDecode)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()