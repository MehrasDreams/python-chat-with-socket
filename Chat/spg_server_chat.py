import socket 
import colorama 
import time 
from socket import * 
from colorama import Fore, init
init()
# ------

# Get a information from user 
name_input =Fore.GREEN+input(Fore.BLUE+"Whats Your Name : ")
#ip_input = input(Fore.YELLOW+"Enter Your IP Addres: ")
port_input = input(Fore.RED+"Enter Your Port: ")





main_chat = socket(2,1)
main_chat.bind(("172.17.0.1", int(port_input)))
main_chat.listen(2)
print(Fore.YELLOW+"Server Runing: ")



client , addr = main_chat.accept()
print(Fore.GREEN+"Connected to server" + str(addr))


while True:
    
    dm = input(Fore.BLUE+"Enter DM : ")
    client.send((name_input+ " : "+ dm).encode())
    pm = client.recv(1234)
    print(pm.decode())
    



main_chat.close()


