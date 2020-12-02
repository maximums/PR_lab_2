import random

class DiffieHellman:
    
    def __init__(self):
        self.modulus = 9973
        self.base = 2351
        minPrime = 0
        maxPrime = 1000

    def generate_key(self, secret):
        key = int(pow(self.base, secret, self.modulus))
        return key
    
    def get_secret_key(self, key, secret):
        secr_key = int(pow(key, secret, self.modulus))
        return secr_key

    def encry(self, msg, key):
        ency_bytes = []
        data = msg.encode('utf-8')
        for byt in data:
            ency_bytes.append(byt + key)
        return ency_bytes
    
    def decry(self, data, key):
        print(data)
        msg = ''
        for byt in data:
            msg += chr(byt - key)
        return msg

# if __name__ == "__main__":
#     DiffieHellman()        
