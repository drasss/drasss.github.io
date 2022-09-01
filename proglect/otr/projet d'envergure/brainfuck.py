k=input("nombre ou caractere ? nb/ca ")
txt=tyt=""
if k=="ca":
    k=input("quel charactere ? ")
    for i in range(ord(k)):
        txt=txt+"+"
        tyt=tyt+"-"
    print(ord(k),tyt+"\n  ",txt)
if k=="nb":
    k=int(input("quel nombre ? "))
    for i in range(k):
        txt=txt+"+"
        tyt=tyt+"-"
    print(chr(k),tyt+"\n ",txt)

