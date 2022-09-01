import os, os.path,time
lect = open("recup.txt", "r", encoding="utf-8")
noms = lect.read() + "₾"
tab = tuple()
i, j = 0, 0
st = ""
while noms[i] != "₾":
    while noms[i] != "\n" and noms[i] != "₾":
        st += noms[i]
        i += 1

    tab = tab + (st,)
    st = ""
    i += 1
begin=input("que veux tu mettre au début ?\n")
end=input("que veux tu mettre a la fin ?\n")
resultat=tuple()
for i in range(len(tab)):
    resultat+=(begin+tab[i]+end,)
    print(resultat[i])
fichier=open("resultat.txt","w")
for i in range(len(resultat)):
    fichier.write(resultat[i]+"\n")
fichier.close()

