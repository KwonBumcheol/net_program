import socket

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol    # TCP(6) / UDP(17)
        self.check = 0
        self.saddr = socket.inet_aton(saddr)
        self.daddr = socket.inet_aton(daddr)
        
test = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(test), ('localhost', 2500))   # TypeError: cannot convert 'Iphdr' object to bytes - byte 형변환x