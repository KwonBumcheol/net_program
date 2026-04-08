import socket

BUFF_SIZE = 1024
port = 5555

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect(('localhost', port)) # 전송할 상대방 지정

for i in range(10):
    time = 0.1
    data = 'Hello, IoT'
    
    while True:
        c_sock.send(data.encode())
        print('Packet send({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)
        
        try:
            data = c_sock.recv(BUFF_SIZE)
        except socket.timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            print('Response', data.decode())
            break