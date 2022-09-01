import os, os.path,time
replaced=input("que cherches-tu a remplacer ?: ")
replacing=input("par quoi ?: ")
lect = open("recup.txt", "r", encoding="utf-8")
noms = lect.read() + "₾"
time.sleep(0.5)
lect.close()
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
replacelist=tuple()
k=0
for i in range(len(tab)):
    bol = 0
    k=0
    bole=False
    rpcer=""
    for z in range(len(tab[i])-len(replaced)+1):
        bol=0
        for j in range(len(replaced)):
            if tab[i][z + j] != replaced[j]:
                bol =0
            else:
                bol+=1
            if bol==len(replaced):
                k = z
                bole=True
    if bole:
        j=0
        while j<k:
            rpcer+=tab[i][j]
            j+=1
        rpcer+=replacing
        j+=len(replaced)
        for u in range(j,len(tab[i])):
            rpcer+=tab[i][u]
    replacelist+=(rpcer,)
fichier=open("resultat.txt","w")
for i in range(len(replacelist)):
    if replacelist[i]!="":
        print(replacelist[i])
        fichier.write(replacelist[i]+"\n")
fichier.close()

