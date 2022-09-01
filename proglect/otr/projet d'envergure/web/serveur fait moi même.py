import socket
servs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
pp = input("on écoute quel port ?")
if pp == "":
    pp=1111
pp = int(pp)
servs.bind(("", pp))


servs.listen()
print("en écoute:")
(a,(b,c))= servs.accept()
while True:
    ul = a.recv(1024)
    u2=ul.decode()
    print(u2)


    
        

