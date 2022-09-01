import os,time
os.system("start .\\recupmp3.bat")
time.sleep(1)
lect = open("list.txt", "r", encoding="utf-8")
noms = lect.read() + "\n₾"
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

#definition des fonctions
def save():
    global tab
    exists=False
    while not(exists):
        exists=True
        name=input("comment voulez-vous l'appeler (ce nom est peut être déja pris)? ")
        for i in tab:
            if i==name:
                exists=False
    fichier=open("data.txt","r")
    recupdt=fichier.read()
    fichier.close()
    fichier=open("recup\\"+name+".txt","w")
    fichier.write(recupdt)
    fichier.close()

def retrive():
    global tab
    print("----------------------------------")
    for i in tab:
        print(i)
    exists=False
    while not(exists):
        exists=False
        rcp=input("----------------------------------\n choisis quel fichier tu veux recuperer (avec le txt)\n")
        for i in tab:
            if i==rcp:
                exists=True
    fichier=open("recup\\"+rcp,"r")
    dat=fichier.read()
    fichier.close()
    fichier=open("data.txt","w")
    fichier.write(dat)
    fichier.close()
    
#choix
choice=""
while choice!="1" and choice!="2":
    print("1) reprendre des données déja sauvegardées")
    choice=input("2) sauvegarder les données entréesé\n")
if choice=="2":
    save()
else:
    retrive()



