import json
import socket
from hamming import Hamming

class Protocol:

    BUFF_SIZE = 4096

    def get_data_bytes(self, data):
        data = data.decode('utf-8')
        return data.split('/')

    def make_payload(self, data):
        lt = self.get_data_bytes(data)
        l = len(lt)-1
        msg = ''
        for i in range(l):
            dta = self.hamming.detect_error(lt[i])
            if dta == 0:
                msg += self.hamming.data_extract(lt[i])
            else:
                msg += self.hamming.data_extract(dta)
        return msg[::-1]
    
    def __init__(self, sockt):
        self.sock = sockt
        self.addr = socket.gethostname()
        self.hamming = Hamming()
          
    def write(self, data, addr):
        data_bytes = self.hamming.make_bytes(data)
        self.sock.sendto(data_bytes.encode('utf-8'), (self.addr, addr))

    def read(self):
        data, client_addr = self.sock.recvfrom(self.BUFF_SIZE)
        self.addr_port = client_addr[1]
        resp = self.make_payload(data)
        return resp

    def start(self, server_port):
        self.sock.bind((self.addr, server_port))
