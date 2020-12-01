import socket
from protocol import Protocol
from other import Client

CLIENT_PORT = 17018

if __name__ == "__main__":
    cl2 = Client(CLIENT_PORT)
