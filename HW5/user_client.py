from socket import *
import time

BUF_SIZE = 1024

open('data.txt', 'w').close()

while True:
    D = input('choose device 1, 2, quit: ')
    
    if D == 'quit':
        # Device1에 quit 전송
        try:
            s1 = socket(AF_INET, SOCK_STREAM)
            s1.connect(('localhost', 7700))
            s1.send(b'quit')
            s1.close()
        except:
            pass

        # Device2에 quit 전송
        try:
            s2 = socket(AF_INET, SOCK_STREAM)
            s2.connect(('localhost', 8800))
            s2.send(b'quit')
            s2.close()
        except:
            pass

        print('quit')
        break
    
    if D == '1':
        port = 7700
    elif D == '2':
        port = 8800
    else:
        continue

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', port))
    s.send(b'Request')

    if D == '1':
        data = b''
        while len(data) < 3:
            pack = s.recv(3 - len(data))
            if not pack:
                break
            data += pack

        if len(data) == 3:
            msg = list(data)
            now = time.ctime()
            
            line = f"{now}: Device1: Temp={data[0]}, Humid={data[1]}, Ilum={data[2]}"
            print(line)
            
            with open('data.txt', 'a') as f:
                f.write(line + '\n')
    
    if D == '2':
        data = b''
        while len(data) < 5:
            pack = s.recv(5 - len(data))
            if not pack:
                break
            data += pack

        if len(data) == 5:
            msg = list(data)
            now = time.ctime()
            
            line = f"{now}: Device2: Heartbeat={data[0]}, Steps={data[1]}, Calories={data[2]}"
            print(line)
            
            with open('data.txt', 'a') as f:
                f.write(line + '\n')
                
    s.close()
