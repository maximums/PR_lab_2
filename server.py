import socket
from protocol import Protocol
from another import Server

PORT = 17017
CLIENT_PORT = 17019

if __name__ == "__main__":
    sr1 = Server((CLIENT_PORT, PORT))
    sr1.listening()