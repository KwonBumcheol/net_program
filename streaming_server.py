import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
videoFile = 'lizard.mp4'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 6000))
sock.listen(5)

while True:
    csock, addr = sock.accept()
    print("Client is connected")
    cap = cv2.VideoCapture(videoFile)
    
    while cap.isOpened():           # 동영상이 열려 있는 동안 반복
        ret, frame = cap.read()     # 프레임 한 장 읽기 - 캡쳐
        if ret:                     # 성공
            temp = csock.recv(BUF_SIZE)     # 'start' 수신
            if not temp:
                break
            
            result, imgEncode = cv2.imencode('.jpg', frame) # jpg 형식으로 압축/인코딩
            data = np.array(imgEncode)  # 이미지 -> np 배열로 변환
            byteData = data.tobytes()   # np 배열 -> byte 변환
            csock.send(str(len(byteData)).zfill(LENGTH).encode())   # 10개 문자열로 표현된 길이 전송(int -> str -> byte)
            
            temp = csock.recv(BUF_SIZE) # 'image' 수신
            if not temp:
                break
            
            csock.send(byteData)    # byte 변환 후 전송
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    csock.close()