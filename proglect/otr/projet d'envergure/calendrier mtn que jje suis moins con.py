import time
aut=time.localtime()
an=aut[0]
mo=aut[1]
jo=aut[2]
callnj=("Lundi   ","Mardi   ","Mercredi","Jeudi   ","Vendredi","Samedi  ","Dimanche")
moi=("Janvier  ","Fevrier  ","Mars     ","Avril    ","Mai      ","Juin     ","Juillet  ","Aout     ","Septembre","Octobre  ","Novembre ","Décembre ")
demande=input("De quelle année veux-tu le calendrier ?\n")
demande=int(demande)
#l'année est-elle bissextile
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
b=bissex(an)
#trouver a partir d'aujourd'hui le premier jour de cette année
numjo=7-(aut[7]-2-aut[6])%7
mo=1
jo=1
#remonter jusqu'a l'année demandée
if demande<an:
    while an!=demande:
        an+=-1
        b=bissex(an)
        numjo=(numjo-(b+1))%7
        
if demande>an:
    while an!=demande:
        an+=1
        b=bissex(an)
        numjo=(numjo+b+1)%7
#trouver paques
paq=22+(2*(an%4)+4*(an%7)+6*((19*(an%19))%30)+5)%7+(19*(an%19))%30+59+b
#faire le calendrier
ct=0
for i in range(365+b):
    if i==paq:
        affpaq="  ------pâques------"
    else:
        affpaq=""
    spm=" "
    spj=" "
    if mo>9:
        spm=""
    if jo>9:
        spj=""
    print(str(i)+")  "+callnj[numjo-1]+" "+str(jo)+spj+" "+moi[mo-1]+spm+"("+str(mo)+")"+" "+str(an)+affpaq)
    if mo==2 and jo==28:
        if b==1:
            jo=29
            b=0
        else:
            jo=1
            mo=3
    elif mo==2 and jo==29:
        jo=1
        mo=3
    elif jo==31 and mo==12:
        an+=1
        jo=0
        mo=0
    elif ((mo==1 or mo==3 or mo==5 or mo==7 or mo==8 or mo==10) and (jo==31)):
        mo+=1
        jo=1
    elif ((mo==4 or mo==6 or mo==9 or mo==11) and (jo == 30)):
        mo+=1
        jo=1
    else:
        jo+=1
    numjo=(numjo+1)%7
