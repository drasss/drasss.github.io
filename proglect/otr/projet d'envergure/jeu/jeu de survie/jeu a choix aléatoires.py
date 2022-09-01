import random
import time
print("vous vous reveillez, aucune personne aux alentours, vous êtes dans une jungle, mais ou ?\n Comment vous êtes arrivés la ? Qui sait ? l'important maintenant c'est de survivre et vite, vous recuperez ce que vous pouvez de vos afffaires éparpillées \n et vous partez")
choix=1
choixbis=1
#variables de besoin
nourriture = 10
sommeil = 10
soif = 8
froid = 5
folie = 20
#variables qui comblent le besoin
cabane=0
feu=0
puis=0
atelier=0
#matieres premieres
metal=2
bois=0
brindilles=0
corde=2
#ouitls (en durabilité)
pelle=0
couteau=15
pioche=0
machette=0

#procedure pour construire 

#on definit les fonctions realtives aux évenements


#on definit la fonction d'appel de l'evenement aléatoire qui prend en compte les differentes avancées



#on fait la boucle de jeu
while choix!=0:
      
      print("nourriture: ",nourriture," sommeil: ",sommeil," soif: ",soif," froid: ",froid," folie: ",folie,"\n")
      print("atelier niveau: ",atelier," cabane niveau: ",cabane," feu niveau: ",feu," puis niveau: ",puis,"\n")
      if 0<couteau<5:
            print("le couteau va bientot se casser")
      elif 5<couteau<10:
            print("le couteau commence a s'user")
      if 0<machette<5:
            print("la machette va bientot se casser")
      elif 5<machette<10:
            print("la machette commence a s'user")
      if 0<pelle<5:
            print("la pelle va bientot se casser")
      elif 5<pelle<10:
            print("la pelle commence a s'user")
      if 0<pioche<5:
            print("la pioche va bientot se casser")
      elif 5<pioche<10:
            print("la pioche commence a s'user")

    
      while 0<int(choix)<5:
            
            print("que voulez vous faire ?")
            choix=input("1)action, 2)construction, 3)réparation/transformation, 4)besoin vital, 0)sauvegarder et quitter\n")
            # ACTION
            if choix==1:
                  print("quelle action ?")
                  choixbis=input("1)explorer, 2)récolter, 3)détruire")

# Construction
            if choix=="2":
                  while choixbis!=0:
                        print("que voulez vous construire?")
                        choixbis=input("1)cabane, 2)feu, 3)puis, 4)atelier 0)exit\n")
                        if choixbis=="1":
                              if cabane==0:
                                    sur=input("ca va couter 2 bois, 8 brindilles et 1 corde, êtes vous sur ? Y/N")
                                    if sur=="Y" or "y":
                                          if(bois>=2 and brindilles>=8 and corde>=1):
                                                bois=bois-2
                                                brindilles=brindilles-8
                                                corde=corde-1
                                                cabane=1
                                                sommeil=sommeil-1
                                                print("c'est fait ! \n")
                                                choixbis=0
                                          else:print("y'a pas assez pour construire ca :/")
                              elif cabane=="1":
                                    sur=input("ca va couter 6 bois, 8 brindilles et 3 corde, êtes vous sur ? Y/N")
                                    if sur=="Y" or "y":
                                          if(bois>=4 and brindilles>=4 and corde>=3):
                                                bois=bois-4
                                                brindilles=brindilles-4
                                                corde=corde-3
                                                cabane=2
                                                sommeil=sommeil-1
                                                print("c'est fait ! \n")
                                                choixbis=0
                                          else:print("y'a pas assez pour construire ca :/")
                              elif cabane=="2":
                                    sur=input("ca va couter 8 bois, 12 brindilles et 8 corde, êtes vous sur ? Y/N")
                                    if sur=="Y" or "y":
                                          if(bois>=8 and brindilles>=12 and corde>=8):
                                                bois=bois-8
                                                brindilles=brindilles-8
                                                corde=corde-8
                                                cabane=3
                                                sommeil=sommeil-1
                                                print("c'est fait ! \n")
                                                choixbis=0
                                          else:print("y'a pas assez pour construire ca :/")













