import time,os

#ce qu'il reste a faire

#il faut que je regle le probleme du delete ou y'a une valeur qui s'affiche +eurs fois

#et il faut que je re-regarde la manière dont je stocke les valeur dans les txt (time-fois etc...)




#fonctions
def choix():
      global options,choix
      print("voici les données déja disponibles:\n")
      for i in range(len(options)):
            print(options[i],"\n")
      print("----------------------------------------------")
      print("veux tu: \n1)créer une nouvelle liste de données")
      print("2)remplir une déja existante")
      print("3)quitter")
      choix="0"
      while choix!='1' and choix!='2' and choix!='3':
            choix=input("")
      if choix=="1":
            create()
      if choix=="2":
            amodif=input("quel fichier doit être changé (avec le .txt ) ?\n")
            fill(amodif)
      if choix=="3":
            rien="rien"

def create():
      global amodif
      new=input("quel nom on lui donne ? (sans le .txt) \n")
      creation=open("data\\"+new+".txt","w")
      amodif=new+".txt"
      creation.close()
      fill(amodif)
      
def fill(amodif):
      values=tuple()
      fichier=open("data\\"+amodif,"r")
      modified=fichier.read()
      fichier.close()
      mots=""
      for i in range(len(modified)):
            if modified[i]!="\n":
                  mots+=modified[i]
            else:
                  values+=(mots,)
                  mots=""
      print("tapes quitt pour prendre fin ")
      print("data pour voir les données")
      print("delete pour supprimer une valeur")
      include=""
      while include!="quitt":
            include=input(":")
            if include=="quitt":
                  rien="rien"
            elif include=="data":
                  for i in range(len(values)):
                        print(values[i])
            elif include=="delete":
                  for i in range(len(values)):
                        print(i," ",values[i])
                  dell=int(input("quelle numéro supprimer ?"))
                  values2=tuple()
                  for i in range(len(values)):
                        if i!=dell:
                             values2+=(values[i],)
                        elif i==len(values):
                              1==1
                  values=values2
            else:
                  values+=(include,)
      fichier=open("data\\"+amodif,"w")
      for i in range(len(values)):
            fichier.write(values[i]+"\n")
      fichier.close()
                        
                  
#recupérations des differentes options

os.system("start recuptxt.bat")
time.sleep(0.5)
noms=open("recup.txt","r")
don=noms.read()
noms.close()
options=tuple()
mot=""
for i in range(len(don)):
      if don[i]!="\n":
            mot+=don[i]
      else:
            options+=(mot,)
            mot=""
#choix
choix()
