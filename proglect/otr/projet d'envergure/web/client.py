# coding: utf-8

import socket
pp = input(" on communique avec quel port ? ")
if pp == "":
    pp=443
pp = int(pp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("LAPTOP-NF9H0C14",pp))

k=input("dis quelque chose:\n")
k= str.encode(k) 
s.send(k)

