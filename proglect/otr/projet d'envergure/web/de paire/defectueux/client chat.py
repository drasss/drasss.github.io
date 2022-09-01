import socket
import threading
import keyboard
ppc = input(" on communique avec quel port ? ")
if ppc == "":
    ppc=1112
ppc = int(ppc)
pps = input("on écoute quel port ?")
if pps == "":
    pps=1111
pps = int(pps)
d=0

class chat(threading.Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, statut):
        threading.Thread.__init__(self)
        self.statut = statut

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        if self.statut == 's':
            servs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            servs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servs.bind(("", pps))
            servs.listen()
            print("en écoute:")
            (a,(b,c))= servs.accept()
            while True:
                ul = a.recv(1024)
                ul=ul.decode()
                ul=":"+ul+"\n"
                print(ul)
                d=4
        if self.statut == 'c':
            clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        
            clients.connect(("192.168.1.57", ppc))

            while True:
                k = input("envoyer:\n")
                if k == "/help":
                    print("c'est un chat")
                else:
                    k=str.encode(k)
                    clients.send(k)
serrv = chat('s')
cllint = chat('c')
cllint.start()
serrv.start()
serrv.join()
cllint.join()

