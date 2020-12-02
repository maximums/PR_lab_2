import json
import socket
import random
import threading 
from _thread import *
from transport import Protocol
from diffie_hellman import DiffieHellman

class Client:
    
    def __init__(self, port):
        self.server_port = ''
        self.port = port
        self.client_secret = random.randint(500, 1500)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.read_sock = Protocol(sock)
        self.read_sock.start(port)
        self.hellman = DiffieHellman()
        self.write_sock = Protocol(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
        self.main()
    
    def listening(self):
        while True:
            data = self.read_sock.read()
            data = json.loads(data)
            if 'encry' in data.keys():
                msg = self.hellman.decry(data['data'], self.top_secret_key)
                print('msg: ', msg)
            else:
                print('something ', data['data'])

    def speak(self):
        while True:
            data = input()
            self.write_sock.write(self.make_header(self.hellman.encry(data, self.top_secret_key)), self.server_port)

    def check_header(self, data):
        fdata = json.loads(data)
        if fdata['type'] == 'SERVER':
            self.server_port = fdata['addr']
        else:
            print('ciota neto')

    def make_header(self, data):
        fdata = {"type" : "CLIENT", "addr" : self.port, "data" : data}
        return json.dumps(fdata)

    def handshake(self):
        self.write_sock.write(self.make_header('SYN'), self.server_port)
        data = self.read_sock.read()
        data = json.loads(data)
        self.top_secret_key = self.hellman.get_secret_key(data['key'], self.client_secret)
        data.update({'encry': 'Diffie Hellman', 'key':self.hellman.generate_key(self.client_secret)})
        data = json.dumps(data)
        self.write_sock.write(data, self.server_port)

    def main(self):
        data = self.read_sock.read()
        self.check_header(data)
        print('SERVER PORT -> ', self.server_port ,'\n', json.loads(data)['data'])
        self.handshake()
        start_new_thread(self.speak, ())
        self.listening()
