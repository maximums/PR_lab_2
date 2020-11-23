import socket
from protocol import Protocol

PORT = 17017

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	       
    proto_sock = Protocol(sock)
    proto_sock.start(PORT)
    msg = "\t<---WTF u said bitch?"
    print("bib-bip-bip...")
    while True:
        data = proto_sock.read()
        print(data)
        proto_sock.write("'"+data+"'" + msg)