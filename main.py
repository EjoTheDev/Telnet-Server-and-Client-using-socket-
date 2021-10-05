import getpass
import socket
import sys
import time
import codecs

Hostname = "192.168.1.175"
Port = 5000
ADDR = (Hostname, Port)
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    Client.connect(ADDR)
    Node = Client.recv(2048).decode('utf-8')
    print("Connected to", Node)
    print(Client.recv(2048).decode('utf-8'))
except:
    sys.exit()


def Send(msg):
    Message = msg.encode('utf-8')
    Client.send(Message)
    if msg == "end":
        Client.close()
        sys.exit()
    print(Client.recv(2048).decode('utf-8'))
    return 1

while True:
    Send(input(Node + ": $ "))


