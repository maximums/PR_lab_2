import json
import socket
import random
from protocol import Protocol
from diffie_hellman import DiffieHellman

class Server:
    
    def __init__(self, PORT):
        self.client_port, self.server_port = PORT
        self.serv_secret = random.randint(500, 1500)
        self.target_server_port = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.proto_sock = Protocol(sock)
        self.proto_sock.start(self.server_port)
        self.hellman = DiffieHellman()

    def listening(self):
        first = self.make_header('bib-bib-bib...')
        self.proto_sock.write(first, self.client_port)
        data = self.proto_sock.read()
        self.handshake(data)
        dta, typ = self.check_header(data)
        if typ == 'CLIENT': # True if msg from client, False if msg from server
            self.waiting_for_conn()
        else:
            print('ADDRESS -> ', self.target_server_port)
            self.connected_state()
    
    def handshake(self, data):
        dat = json.loads(data)
        if 'encry' not in dat.keys():
            dat.update({'key': self.hellman.generate_key(self.serv_secret)})
            dat1 = json.dumps(dat)
            self.proto_sock.write(dat1, dat['addr'])
            data = self.proto_sock.read()
            data = json.loads(data)
            self.top_secret_key = self.hellman.get_secret_key(data['key'], self.serv_secret)

    def waiting_for_conn(self):
        print('waiting_for_conn')
        self.proto_sock.write(self.make_header('Enter nunmber(port): '), self.client_port)
        while True:
            data = self.proto_sock.read() # trebuie sa scot data din json (self.check_header(data))
            dte, typ = self.check_header(data)
            dte = self.hellman.decry(dte, self.top_secret_key)
            if dte.isdigit():
                self.target_server_port += dte
                self.proto_sock.write(self.make_header('next digit'), self.client_port)
            else:
                print(self.target_server_port)
                # self.target_server_port = self.target_server_port[::-1]
                # print(self.target_server_port)
                self.proto_sock.write(self.make_header('speak pls'), self.client_port)
                self.connected_state()  

    def encry(self, data):
        return self.hellman.encry(data, self.top_secret_key)

    def connected_state(self):
        print('connected_state')
        self.proto_sock.write(self.make_header('connection successful'), int(self.target_server_port))
        while True:
            data = self.proto_sock.read()
            dta, typ = self.check_header(data)
            print(dta , ' and type ', typ)
            msg = self.make_header(dta)
            if typ == 'CLIENT':
                self.proto_sock.write(msg, int(self.target_server_port))
                print('TREBUIE SA PLECE LA SERVER', self.target_server_port)
            else:
                print('TREBUIE SA PLECE LA CLINET')
                self.proto_sock.write(self.make_header(self.hellman.decry(dta, self.top_secret_key)), self.client_port)


    def make_header(self, data):
        fdata = {"type": "SERVER", "addr" : self.server_port, "data": data}
        return json.dumps(fdata)

    def check_header(self, data):
        fdata = json.loads(data)
        if fdata['type'] == 'SERVER':
            self.target_server_port = fdata['addr']
        return fdata['data'], fdata['type']