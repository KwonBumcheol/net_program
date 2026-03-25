from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)  # 수신 HTTP Request
    
    if not data:
        break
    
    msg = data.decode()    # 문자열 변환
    req = msg.split('\r\n') # 파싱
    
    request_line = req[0]   # HTTP Request 첫줄만 - GET /index.html HTTP/1.1'
    method, path, version = request_line.split()
    filename = path[1:] # / 뒤부터 -> index.html

    # 웹 서버 코드 작성
    # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기
    # HTTP HEADER
    # HTTP BODY
    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html; charset=utf-8'
        body = f.read()
        
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(body.encode())
        f.close()
    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'
        body = f.read()
        
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(body)
        f.close()
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        body = f.read()
        
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(body)
        f.close()
    else:
    # 파일 존재X
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
    c.close()
    