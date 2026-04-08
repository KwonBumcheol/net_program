import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter a message: ')
    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'q':
        break
    
    data, addr = sock.recvfrom(BUFFSIZE)
    print('Server says: ', data.decode())
    
sock.close()