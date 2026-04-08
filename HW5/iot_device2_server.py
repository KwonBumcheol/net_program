from socket import *
import random
import sys

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8800))
sock.listen(10)
print('Device2 running...')

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
    
    hrate = random.randint(40, 140)
    step = random.randint(2000, 6000)
    calo = random.randint(1000, 4000)
    
    # conn.send(hrate.to_bytes(1, 'big'))
    # conn.send(step.to_bytes(2, 'big'))
    # conn.send(calo.to_bytes(2, 'big'))
    conn.sendall(
        hrate.to_bytes(1, 'big') +
        step.to_bytes(2, 'big') +
        calo.to_bytes(2, 'big')
    )
    print(f'temp: {hrate}, step: {step}, calo: {calo}')
    
    conn.close()
    