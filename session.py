from protocol import Protocol
import socket
import json

class DiffieHellman:
    
    def __init__(self):
        self.addr = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.proto_sock = Protocol(sock)


    def make_header(self, data):
        pass

    def check_header(self, data):
        return json.loads(data)

    def read(self):
        data = self.proto_sock.read()
        dt = self.check_header(data)
        if 'encry' in dt.keys():
            self.proto_sock.write(data, (socket.gethostname(), dt['addr']))
        else:
            pass


    def write(self, data, addr):
        pass