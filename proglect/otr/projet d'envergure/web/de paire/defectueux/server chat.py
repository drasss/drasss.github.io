import socket
import time
import keyboard
from threading import Thread

ppc = input(" on communique avec quel port ? ")
if ppc == "":
    ppc=1111
ppc = int(ppc)
pps = input("on écoute quel port ?")
if pps == "":
    pps=1112
pps = int(pps)


class chat(Thread):

    def __init__(self, statut):
        Thread.__init__(self)
        self.statut = statut

    def run(self):
        if self.statut == 's':
            servs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            servs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servs.bind(("", pps))
            servs.listen()
            print("en écoute:")
            (a,(b,c))= servs.accept()
            print(a,b,c)
            d=4
            while True:
                ul = a.recv(1024)
                ul=ul.decode()
                ul=":"+ul+"\n"
                print(ul)
                
        if self.statut == 'c':
            clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            d=True
            while d:
                try:
                     clients.connect(("192.168.1.57", ppc))
                     d=False
                except:
                    print("en attente...")
                    d=True

            while True:
                k = input("envoyer:\n")
                k=str.encode(k)
                clients.send(k)
serrv = chat('s')
cllint = chat('c')
serrv.start()
cllint.start()
serrv.join()
cllint.join()

