import socket
from protocol import Protocol
from other import Client

CLIENT_PORT = 17019

if __name__ == "__main__":
    cl2 = Client(CLIENT_PORT)
