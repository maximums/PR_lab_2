
import socket
from protocol import Protocol

PORT = 17017

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	       
    proto_sock = Protocol(sock)
    proto_sock.start(PORT)
    msg = "I kill people with the guns"
    print("Waiting for client...")
    while True:
        data = proto_sock.read()
        print(data)
        proto_sock.write(msg)