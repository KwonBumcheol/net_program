from socket import *

BUFF_SIZE = 1024
port = 4444

sock = socket(AF_INET, SOCK_DGRAM)
# sock.settimeout(2)  # 2초 대기

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    
    sock.sendto(msg.encode(), ('localhost', port))
    
    # quit
    if msg == 'quit':
        break
    
    data, addr = sock.recvfrom(BUFF_SIZE)
    print(data.decode())
    
sock.close()
    