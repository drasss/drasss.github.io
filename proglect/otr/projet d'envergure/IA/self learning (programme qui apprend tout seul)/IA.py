import random,time
#input
taille=input("Combien y'a t il de données dans l'étude\n")
if taille=="":
      taille=3
taille=int(taille)
modifG=(0,)*taille
ver="y"
don=list()
while ver!="n":
      tplinp=tuple()
      for i in range(taille+1):
            cc=i
            if cc==taille:
                  cc="résultat"
            inp=int(input("que mettre en coordonnée "+str(cc)+" : "))
            tplinp+=(inp,)
      don.append((tuple(tplinp)))
      print(don)
      ver=input("voulez vous continuer y/n ? : ")     
#traitement
res=100
while res>10:
      k="le plan la c'est de mettre des valeurs de bases a chaque données, faire une batterie de if, mettre un 1 pour un succes un 0 pour un echec et additionner les 1 et les 0 x modifG par chaque caracteristique et avoir un résultat final qui aura une condition pour etre considéré comme juste"
#output
