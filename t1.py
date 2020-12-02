from diffie_hellman import DiffieHellman
import json
if __name__ == "__main__":
    string = []
    msg = 'hello'
    for byt in msg.encode('utf-8'):
        string.append(byt + 1)
    print(string)
    str1 = json.dumps(string)
    print(string)
    str1 = json.loads(str1)
    print(string)
    dh = DiffieHellman()
    print(dh.decry(str1, 1))
