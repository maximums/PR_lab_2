import socket
from protocol import Protocol

PORT = 17017

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    proto_sock = Protocol(sock)
    proto_sock.connect(PORT)
    while True:
        proto_sock.write(input())
        data = proto_sock.read()
        # proto_sock.write(data + ' too')
        # data = input()
        print(data)