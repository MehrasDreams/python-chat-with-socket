import socket
from socket import *
from colorama import Fore 

name_input = Fore.GREEN+input(Fore.BLUE+"Whats Your Name : ")
port_input = input(Fore.RED+"Enter Your Port: ")



server = socket(2,1)
server.connect(("172.17.0.1", int(port_input)))

data =  server.recv(222)

print(data.decode())






while True:
    
    dm = input(Fore.BLUE+"Enter DM : ")
    server.send((name_input+ " : "+ dm).encode())
    pm = server.recv(1234)
    print(pm.decode())
    



