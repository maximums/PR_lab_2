import socket
import json
import hashlib

class Protocol:

    BUFF_SIZE = 1024

    def is_valid(self, payload):
        obj = json.loads(payload)
        return obj["hash"] == hashlib.sha256(obj["data"].encode("utf-8")).hexdigest()

    def make_payload(self, val):
        return json.dumps({"hash": hashlib.sha256(val.encode("utf-8")).hexdigest(), "data": val}).encode("utf-8")

    def extract_data(self, payload):
        return json.loads(payload.decode("utf-8"))["data"]
    
    def __init__(self, sockt):
        self.sock = sockt
        self.addr = socket.gethostname()
        
    def write(self, data):

        self.sock.sendto(self.make_payload(data), (self.addr, self.addr_port))
        payload, recv_addr = self.sock.recvfrom(self.BUFF_SIZE)
        if b"nack" in payload:
            self.write(data)

    def read(self):

        data, client_addr = self.sock.recvfrom(self.BUFF_SIZE)
        self.addr_port = client_addr[1]
        payload = self.extract_data(data)
        
        if self.is_valid(data):
            print("Sending ack...")
            self.sock.sendto(b"ack",client_addr)
        else:
            print("Sending nack...")
            self.sock.sendto(b"nack", client_addr)
            self.read()

        return payload
    
    def start(self, server_port):
        self.sock.bind((self.addr, server_port))

    def connect(self, addr_port):
        self.addr_port = addr_port
    