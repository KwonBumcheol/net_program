from socket import *

BUFF_SIZE = 1024
port = 4444

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print("Listening...")

mailbox = {}

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = data.decode()
    
    parts = msg.split() # send 1 hello,iot
    
    # quit
    if msg == 'quit':
        break
    
    # send
    if parts[0] == 'send':
        mboxID = parts[1]
        message = ' '.join(parts[2:])
        
        if mboxID not in mailbox:
            mailbox[mboxID] = []
            
        mailbox[mboxID].append(message)
        print(f'save [{mboxID}]: {message}')
        
        s_sock.sendto(b'OK', addr)
    # receive
    elif parts[0] == 'receive':
        mboxID = parts[1]
        
        if mboxID in mailbox and len(mailbox[mboxID]) > 0:
            msg_out = mailbox[mboxID].pop(0)
            s_sock.sendto(msg_out.encode(), addr)
        else:
            s_sock.sendto(b'No messages', addr)
            
s_sock.close()