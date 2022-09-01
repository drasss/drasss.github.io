import random
import keyboard
import time
import os.path
import mouse
ct=0
i=0
k="3"
print(" c'est un simalteur de bourse, mets la souris en haut a droite \n ou appuyes sur 9 pour mettre en pause et faire quelque chose\n")
while k=="3":
    k=input("1)charger ou 2)nouvelle partie 3)précisions ")
    if k=="3":
        print("tu as 200 € pour commencer et as sous les yeux le cours d'un bien, son prix varie chaque jour, et chaque jour \n tu peux acheter vendre ou ne rien faire, acheter  ou vendre diminue les prix")
        print("un bien vendu ne rapporte que 90% de son prix puisqu'il est \"d'occasion\"")
        print("chaque jour, ton épargne te rapportes 0,2% de ton argent (ton argent augment de 0,2% chaque jour) même si tu es en négatif !")
        print("tout les mois (31 jours) tu dois payer ton loyer et les taxes, ce qui te coute 2% de ton agent + 50 €\n")

if os.path.exists("./save.txt") and k=="1":
    save=open("save.txt","r")
    val=save.read()+" \n"
    save.close()
    while ct<5:
        conc=""
        while val[i]!="\n":
            conc+=val[i]
            i+=1
        i+=1
        if ct==0:
            prix=int(str(conc))/100000
        if ct==1:
            mon=int(str(conc))/100000
        if ct==2:
            bien=int(str(conc))/100000
        if ct==3:
            to=int(str(conc))/100000
        if ct==4:
            ct=int(str(conc))/100000
        ct+=1
if (os.path.exists("./save.txt")==False) or k=="2":
      prix=100
      mon=200
      bien=0
      to=1
      ct=0
      print("hey")
choix=1
boo=False
while choix!="0" :
      time.sleep(0.5)
      while not(keyboard.is_pressed("9")or (mouse.get_position()[1]<100 and mouse.get_position()[0]<100) and boo==False):
            ct+=1
            to=(random.random()+0.1)*1.8
            prix=to*prix+10*to
            mon=mon*1.002
            print(int(mon)," ",bien," ",prix)
            time.sleep(0.5)
            if(keyboard.is_pressed("9")):
                  boo=True
            time.sleep(0.5)
            if ct%31==0:
                mon=0.98*mon-50
      boo=False
      print("\nt'as : ",mon," de monnaie et ",bien," de bien\n")
      choix=input("tu veux 1)acheter ou 2)vendre ou 0)sauvegarder et partir ")
      if choix=="1":
            print("voici combien tu peux en acheter au maximum : ",int(mon/prix))
            choixbis=int(input("combien de bien on achete ?"))
            mon=mon-choixbis*prix
            bien+=choixbis
            prix=prix-0.01*choixbis
      if choix=="2":
                 
            choixbis=int(input("combien de bien on vend ?"))
            if bien-choixbis>=0:
                mon=mon+choixbis*prix*0.9
                prix=prix-0.01*choixbis
                bien=bien-choixbis
            else:
                print("\nt'as pas assez\n")
            
if os.path.exists("save.txt"):
    save=open("save.txt","w")
else:
    save=open("save.txt","x")
save.write(str(int(prix*100000))+"\n"+str(int(mon*100000))+"\n"+str(int(bien*100000))+"\n"+str(int(to*100000))+"\n"+str(int(ct*100000)))
save.close()

                              
            
