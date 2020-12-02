# Laborator 2
<br>

### Author:Dodi Cristian-Dumitru
#### Group:FAF-181
### Description
<br>

Base and main module is __transport.py__, it is abstraction for _BSD Sockets_ with error correction, used algorithm is _Hamming_, its implementation can be found in __hamming.py__. For security I used _Diffie Hellman_ its implementation can be found in __diffie_hellman.py__,
the key exchange is performed in func `def handshake(self, data):` from __server_abstr.py__ and __client_abstr.py__ .
For application lvl I tried to make a protocol based on the workings (state machine) of a __stationary telephone__, it is composed of
__client - server --- server2 - client2__, client abstraction can be found in __client_abstr.py__ and server abstraction in __server_abstr.py__. __client.py__, __client2.py__, __server.py__ and __server2.py__ are just instance of their abstraction in which I define ports for sockets.
<br>

__Order of running:__ _client.py_ or _client2.py_ and _server.py_ or _server2.py_

### Demonstration
![Output](https://github.com/maximums/PR_lab_2/blob/master/img/demo.gif)
