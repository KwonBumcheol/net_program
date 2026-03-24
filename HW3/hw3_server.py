from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5555))
s.listen(1)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        cal = data.decode().replace(" ", "")
        
        try:
            if '+' in cal:
                x, y = cal.split('+')
                result = int(x) + int(y)
            elif '-' in cal:
                x, y = cal.split('-')
                result = int(x) - int(y)
            elif '*' in cal:
                x, y = cal.split('*')
                result = int(x) * int(y)
            elif '/' in cal:
                x, y = cal.split('/')
                result = round(int(x) / int(y), 1)
                
            client.send(str(result).encode())
            # client.send(result.to_bytes(4, 'big'))
                
        except:
            break
        
    client.close()