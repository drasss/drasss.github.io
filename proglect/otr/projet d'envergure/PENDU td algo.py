mot=input("quel mot doit etre deviné\n")
mot=tuple(mot)
prop=tuple()
for i in range(len(mot)):
      prop=prop+("-",)
pd=0
while (prop!=mot)and(pd<11):
      print(str(prop))
      prop=(tuple(prop))
      n=input("quelle lettre ?")
      k=False
      cpt=("",)
      for i in range(len(mot)):
            if n==mot[i]:
                  cpt=cpt+(i,)
                  k=True
      prop1=tuple(prop)
      if k:
            for j in range(len(cpt)):
                  for i in range(len(mot)):
                        if cpt[j]==i:
                              prop1=prop1+(mot[i],)
                        else:
                              prop1=prop[i]
            prop=prop1
            print("bravo, il y a la lettre",n)
      else:
            pd=pd+1
            print("Eh non, il te reste ",11-pd," essais")
if pd >=11:
      print("le mot correct etait: ",mot)
else:
      print("félicitations, le mot a été deviné avec seulement",pd,"erreursé")
