# coding: utf-8 

import socket
import threading

pp = input("on écoute quel port ?")
if pp == "":
    pp=1111
pp = int(pp)


class ClientThread(threading.Thread):

    def __init__(self, aip, aport, clientsocket):

        threading.Thread.__init__(self)
        self.ip = aip
        self.port = aport
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048)
        r=r.decode()
        print(r)

        print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",pp))

while True:
    tcpsock.listen(10)
    print( " En écoute...")
    (clientsocket, (aip, aport)) = tcpsock.accept()
    newthread = ClientThread(aip, aport, clientsocket)
    newthread.start()
