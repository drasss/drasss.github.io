import numpy as np
import random
choix=input("1)proposer un mot  2)en prendre un au hasard?\n")
mots=input("quel mot doit etre deviné\n")
mot=tuple(mots)
echec=()
#création du jeu
props=""
prop=tuple()
for i in mot:
      prop+=("-",)
      props+="-"
prop=np.array(prop)

# le jeu
vies=10
while props!=mots and vies!=0:

      print(prop)
      print(echec)
      act=input("1)une lettre ou 2)un mot ?\n")
      if act=="1":
            lettre="  "
            while len(lettre)!=1:
                  lettre=input("quelle lettre ?\n")
            reussite=False
            for i in range(len(mot)):
                  if mot[i]==lettre:
                        prop[i]=lettre
                        reussite=True
            if not(reussite):
                  vies-=1
                  print("raté ! vous avez "+str(vies)+" vies")
                  echec+=(lettre,)
            else:
                  print("il y a un "+lettre)
      if act=="2":
            lettre=""
            while len(lettre)!=len(mot):
                  lettre=input("a quel mot pensez vous ?\n")
            if lettre!=mots:
                  print("bien éssayé mais c'est raté")
                  vies-=2
      props=""
      for i in range(len(prop)):
            props+=prop[i]

print(prop)
print("c'est gagné")
                  
                  
