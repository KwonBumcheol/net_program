import socket
import struct
import binascii

# UDP 헤더 클래스 정의
class Udphdr:
    def __init__(self, sport, dport, length, check):
        self.sport  = sport   # 송신자 포트번호 (2바이트)
        self.dport  = dport   # 수신자 포트번호 (2바이트)
        self.length = length  # UDP 패킷 길이  (2바이트)
        self.check  = check   # 체크섬          (2바이트)

    def pack_Udphdr(self):
        # UDP 헤더 = 총 8바이트 (H: unsigned short 2바이트 x 4)
        packed = struct.pack('!HHHH', self.sport, self.dport, self.length, self.check)
        return packed

# UDP 헤더 unpack 함수
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

# 각 필드값을 가져오는 함수들
def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]


# --- 실행 ---
udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(
    getSrcPort(unpacked_udphdr),
    getDstPort(unpacked_udphdr),
    getLength(unpacked_udphdr),
    getChecksum(unpacked_udphdr)
))