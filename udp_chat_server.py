import socket

port = 3333
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())
    if data.decode() == 'q':
        break
    
    resp = input('-> ')
    sock.sendto(resp.encode(), addr)
    if resp == 'q':
        break
    
sock.close()