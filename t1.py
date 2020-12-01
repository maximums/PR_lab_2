# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 

print_lock = threading.Lock() 

# # thread function 
# def threaded(c): 
# 	while True: 

# 		# data received from client 
# 		data, addr = c.recvfrom(1024) 
# 		if not data: 
# 			print('Bye') 
			
# 			# lock released on exit 
# 			print_lock.release() 
# 			break

# 		# reverse the given string from client 
# 		data = data[::-1] 

# 		# send back reversed string to client 
# 		c.sendto(data, ('localhost', addr)) 

host = "localhost" 
port = 12345

def lisen():
    sok = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sok.bind((host, port))
    print('socket binded on', host, ' ', port)
    while True:
        data, addr = sok.recvfrom(1024)
        print('From : ', addr, ' ', data.decode())

def speak():
    sok = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sok.bind((host, 12346))
    print('socket binded on', host, ' ', 12346)
    while True:
        dt = input()
        sok.sendto(dt.encode(), (host,12345))

# def Main(): 
# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# 	s.bind((host, port)) 
# 	print("socket binded to port", port) 
# 	while True: 

# 		data, addr = s.recvfrom(1024)

# 		# lock acquired by client 
# 		print_lock.acquire() 
# 		print('Connected to :', addr[0], ':', addr[1], ' \ndata =', data) 

# 		# Start a new thread and return its identifier 
# 		start_new_thread(threaded, (c,)) 
# 	s.close() 


if __name__ == '__main__': 
	# Main() 
    print('start')
    start_new_thread(lisen, ())
    # start_new_thread(speak, ())
    speak()
