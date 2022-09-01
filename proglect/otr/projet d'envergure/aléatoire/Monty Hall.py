import random,time
end=int(input("on va jusqu'ou?\n"))
i=0
win,loose=0,0
while i<=end :
      porte=list()
      random.seed(time.time()+i)
      PV=random.randint(0,2)
      for j in range(0,3):
            if j==PV:
                  porte.append("V")
            else:
                  porte.append("C")
      ChoixPC=random.randint(0,2)
      ChoixPres=ChoixPC
      while ChoixPres==ChoixPC or porte.index("V")==ChoixPres:
            ChoixPres=random.randint(0,2)
      resultat=[0,1,2]
      resultat.remove(ChoixPres)
      resultat.remove(ChoixPC)
      if porte[resultat[0]]=="V":
            win+=1
      else:
            loose+=1
      i+=1
tauxR=win*100/(end+1)
tauxD=loose*100/(end+1)
print("Pourcentage de chance de réusseite en changeant d'avis: "+str(tauxR)+"\nPourcentage de Chance d'échec en changeant d'avis: "+str(tauxD))
print("pour verifier que l'étude est juste, si c'est différent de 100 y'a une érreur: "+str(tauxR+tauxD))
