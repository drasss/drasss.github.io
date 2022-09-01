import os, os.path,time
replaced=input("que cherches-tu a remplacer ?: ")
replacing=input("par quoi ?: ")
doss=input("quel est le nom du dossier dans lequel se situe les fichiers ?: ")
os.system("recupmp3 "+doss)
time.sleep(0.5)
lect = open("recup.txt", "r", encoding="utf-8")
noms = lect.read() + "₾"
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
    for z in range(len(tab[i])-len(replaced)):
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
for i in range(len(replacelist)):
    if replacelist[i]!="":
        os.system("REN \"..\\"+doss+"\\"+tab[i]+"\" \""+replacelist[i]+"\"") #syntaxe batch a revoir
        print(replacelist[i])
#chcp 65001
#dir ..\TEST /B>recup.txt
#chcp 1252
#exit



