import time
aut=time.localtime()
Jmois=(00,31,28,31,30,31,30,31,31,30,31,30,31)
print("toutes les réponses devront se faire numériquement\n")
Ynaiss=int(input("quelle est ton année de naissance ?\n"))
Mnaiss=int(input("quelle est ton mois de naissance ?\n"))
Jnaiss=int(input("quelle est ton jour de naissance ?\n"))
Hnaiss=int(input("quelle est ton Heure (juste l'heure) de naissance ?\n"))
Minnaiss=int(input("quelle est tes minutes de naissance ?\n"))

##fonction is_bissextile
def bissex (an):
    if (an%100 == 0):
        if (an%400 == 0):
            biss=1 
        else: biss=0
    elif (an%4 == 0):
        biss=1
    else:
        biss=0
    return(biss)
#si l'année est bissextile et si il est né avant février, on rajoute un jour au compteur
bissn=bissex(Ynaiss)
j=0
if Mnaiss<3 and bissn==1:
    j=1

#on rajoute les jours des mois aprés sa naissance dans l'année de sa naissance
for i in range(Mnaiss+1,len(Jmois)):
    j+=Jmois[i]

#on rajoute les jours restant du mois ou il est né 
j+=(Jmois[Mnaiss]-Jnaiss)-1

#on rajoute les jours des années entre sa naissance et maintenant
for i in range(Ynaiss+1,aut[0]):
    biss=bissex(i)
    j+=365+biss
#on rajoute les jours des mois entre le debut de cette année et aujourd'hui
for i in range(1,aut[1]-1):
    j+=Jmois[i]
#on rajoute les jours entre le début du mois et aujourd'hui
j+=aut[2]-1

#-------------------------------------comptage des minutes------------------------------------------
minn=1440-Minnaiss-60*Hnaiss
minn+=aut[3]*60+aut[4]
minn+=j*1440
#-------------------------------------comptage des secondes------------------------------------------
sec=60*minn+aut[5]
#Traitement des secondes pour afficher des données
print("tu as vécu ",sec," secondes")
print("ca fait ",sec/60," minutes")
H=sec/(60*60)
print(H," Heures")
print(H/24," Jours")
print(H/(24*30.417)," Mois")
print(H/(24*365)," Ans")
Mois=int(H/(24*30.417))
j=int(j)

diviseur=tuple()
for i in range(1,Mois):
      if Mois%i==0 and Mois/i!=Mois:
            diviseur+=(i,)
x=diviseur[int(len(diviseur)/2)]

y=int(Mois/x)
ligne=""
for i in range(min(x,y)):
    ligne+="O"
print("chaque O represente un Mois vécu")
for i in range(max(x,y)):
    print(ligne)

