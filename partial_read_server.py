from socket import *

server = create_server(('', 9999))
conn, addr = server.accept()

conn.send(b'This it IoT world!!!')
conn.close()