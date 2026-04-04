from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('google.com', 80))

sock.send(b'GET / HTTP/1.1\r\n\r\n')

# post http request
# body = "name=abc&age=20"
# request = (
#     "POST / HTTP/1.1\r\n"
#     "Host: google.com\r\n"
#     "Content-Type: application/x-www-form-urlencoded\r\n"
#     f"Content-Length: {len(body)}\r\n"
#     "\r\n"
#     f"{body}"
# )

# sock.send(request.encode())

data = sock.recv(10000)

print(data.decode())
sock.close()
