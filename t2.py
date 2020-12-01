import json
import socket
import threading 
from _thread import *
from protocol import Protocol

class Client:
    
    def __init__(self, port):
        self.server_port = ''
        self.port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.proto_sock = Protocol(sock)
        self.proto_sock.start(port)
        self.read_sock = Protocol(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
        self.main()

    def check_header(self, data):
        # print('client check_header()')
        fdata = json.loads(data)
        # print(fdata['data'])
        if fdata['type'] == 'SERVER':
            self.server_port = fdata['addr']
            print(fdata['addr'])
        # elif fdata['type'] == 'INIT':
        #     sel
        else:
            print('ciota neto')

    def make_header(self, data):
        # print('client make_header()')
        fdata = {"type" : "CLIENT", "addr" : self.port, "data" : data}
        return json.dumps(fdata)

    def main(self):
        # print('client main()')
        data = self.proto_sock.read()
        self.check_header(data)
        print('SERVER PORT -> ', self.server_port)
        # cd ..\..\univer3\alexB\PR_lab_2
        # caroce s1 il trece pe s2 in connectedState doar ca clientul in timpul acesta vrea sa scrie iar ser sa trimtia
        while True:
            dat = input()
            if dat == 'ggg':
                tmp = self.proto_sock.read()
                print(tmp)
            msg = self.make_header(dat)
            self.proto_sock.write(msg, self.server_port)
            dt = self.read_sock.read()
            self.check_header(dt)
            print(dt)
