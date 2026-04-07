from socket import *

sock = create_connection(('localhost', 9999))

data_size = 20      # 수신할 데이터의 크기
rx_size = 0         # 지금까지 받은 데이터 크기
total_data = []     # 저장 공간
while rx_size < data_size:
    # 최대 4바이트 수신하도록 설정
    data = sock.recv(4)
    if not data:
        break
    
    rx_size += len(data)
    total_data.append(data.decode())
    print(total_data)
    
message = ''.join(total_data)
print(message)
sock.close()