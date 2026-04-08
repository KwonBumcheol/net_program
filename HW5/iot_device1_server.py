from socket import *
import random
import sys

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7700))
sock.listen(10)
print('Device1 running...')

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg == b'quit':
        print('client:', addr, 'quit')
        conn.close()
        continue
    elif msg != b'Request':
        print('client: ',addr, msg.decode())
        conn.close()
        continue
    else:
        print('client: ',addr, msg.decode())
    
    temp = random.randint(0, 40)
    hum = random.randint(0, 100)
    lum = random.randint(70, 150)
    
    # conn.send(temp.to_bytes(1, 'big'))
    # conn.send(hum.to_bytes(1, 'big'))
    # conn.send(lum.to_bytes(1, 'big'))
    conn.sendall(temp.to_bytes(1, 'big') + hum.to_bytes(1, 'big') + lum.to_bytes(1, 'big'))
    print(f'temp: {temp}, hum: {hum}, lum: {lum}')
    
    conn.close()
    