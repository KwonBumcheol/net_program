from socket import *
import argparse

s = socket(AF_INET, SOCK_STREAM)

parser = argparse.ArgumentParser()              # 객체 생성 - 파서 만들기
parser.add_argument('-s', default='localhost')  # 명령행 인자 추가(ip, port) -s == --server
parser.add_argument('-p', type=int, default=2500) # 인자 파싱
args = parser.parse_args()

s.connect((args.s, args.p))
print('connected to ', args.s, args.p)

while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode())
    
    data = s.recv(1024)
    if not data:
        break
    
    print('Received message: ', data.decode())

s.close()