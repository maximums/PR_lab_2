import socket
from protocol import Protocol
from another import Server

PORT = 17020
CLIENT_PORT = 17018

if __name__ == "__main__":
    sr2 = Server((CLIENT_PORT, PORT))
    sr2.listening()