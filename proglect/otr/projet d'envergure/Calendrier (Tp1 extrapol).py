import time
aut=time.localtime()
print("donne moi la date d'aujourd'hui et je te donnerai le calendrier de cette année")
adj=input("Voulez vous rentrer le temps manuellement ? (Y/N) ")
cal=int

                        #on prend la date en fonction du choix

if adj=="y" or adj=="Y":
    
    an = input("quelle année sommes-nous ? ")
    jo=1
    mo=1
    cal=9-(aut[7]-aut[6])%7
    print("                            ",cal)
    
else:
    jo=aut[2]
    mo=aut[1]
    an=aut[0]
    cal=int(aut[6]+1)
nom=str
moi=str
an=int(an)

                        #on voit quand est pâques

a=int
b=int
c=int
d=int
e=int
a=an%19
b=an%4
c=an%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7
jap=int
jap=22+e+d
jap = int(jap)

                          #on voit si l'année est bissextile

an10 = int(an)%100
an40 = int(an)%400
an4 = int(an)%4
an = int(an)
if (an10 == 0):
    if (an40 == 0):
        n=1 
    else: n=0
elif (an4 == 0):
    n=1
else:
    n=0
if n==1:
    jap = jap +60
else: jap = jap + 59


                        #on change la valeur du nom du jour pour qu'il soit bon
diff=aut[0]-an
signe=1
if diff<0:
    diff=diff-1
    signe=-1
summ=0
ak=an
print("diff:",diff)
for i in range(diff):
    an=an+signe
    an10 = int(an)%100
    an40 = int(an)%400
    an4 = int(an)%4
    an = int(an)
    if (an10 == 0):
        if (an40 == 0):
            n=1 
        else: n=0
    elif (an4 == 0):
        n=1
    else:
        n=0
    
    summ+=n
print("summ:",summ)
an=ak
cal=(cal+signe*(summ+diff))%7 +1
print("cal:",cal)
    
                       

                        #on affiche jour par jour le calendrier
        

for i in range(0,365+n):
    ct = 2
    if(cal == 2):
        nom="   mardi"
        ct = 3
    if(cal == 3 and ct == 2):
        nom="mercredi"
        ct = 3
    if(cal == 4 and ct == 2):
        nom="   jeudi"
        ct = 3
    if(cal == 5 and ct == 2):
        nom="vendredi"
        ct = 3
    if(cal == 6 and ct == 2):
        nom="  samedi"
        ct = 3
    if(cal == 7 and ct == 2):
        nom="dimanche"
        ct = 3
    if(cal == 1 and ct == 2):
        nom="   lundi"
    ct=0
    if mo==1:
        moi="  Janvier"
    if mo==2:
        moi="  Fevrier"
    if mo==3:
        moi="     Mars"
    if mo==4:
        moi="    Avril"
    if mo==5:
        moi="      Mai"
    if mo==6:
        moi="     Juin"
    if mo==7:
        moi="  Juillet"
    if mo==8:
        moi="     Aout"
    if mo==9:
        moi="Septembre"
    if mo==10:
        moi="  Octobre"
    if mo==11:
        moi=" Novembre"
    if mo==12:
        moi=" Décembre"
    
    if jo <10 and mo<10:
        aff = nom+"  "+str(jo)+" "+moi+" ("+str(mo)+")"+" "+str(an)         
    elif jo<10:
        aff=nom+"  "+str(jo)+" "+moi+"("+str(mo)+")"+" "+str(an)
    elif mo<10:
        aff=nom+" "+str(jo)+" "+moi+" ("+str(mo)+")"+" "+str(an)
    else: aff=nom+" "+str(jo)+" "+moi+"("+str(mo)+")"+" "+str(an)
    if jap ==1:
        aff=str(aff)+"       pâques"
    print(aff)
    if jap>0:jap=jap-1
    
    if(n==1 and mo==2 and jo==28):
        jo=29
        ct=1
    if(n==0 and mo==2 and jo==28):
        jo=1
        mo=3
        ct=1
    if(n==1 and mo==2 and jo==29 and ct==0):
        jo=1
        mo=3
        ct=1    
    if(jo==31 and mo==12):
        an=an+1
        jo=1
        mo=1
        ct=1
    if((mo==1 or mo==3 or mo==5 or mo==7 or mo==8 or mo==10) and (jo==31)):
        mo=mo+1
        jo=1
        ct=1
    if((mo==4 or mo==6 or mo==9 or mo==11) and (jo == 30)):
        mo=mo+1
        jo=1
        ct=1
    if(ct == 0):
        jo=jo+1
    ct = 2
    if(cal == 1):
        cal=2
        ct = 3
    if(cal == 2 and ct == 2):
        cal=3
        ct = 3
    if(cal == 3 and ct == 2):
        cal=4
        ct = 3
    if(cal == 4 and ct == 2):
        cal=5
        ct = 3
    if(cal == 5 and ct == 2):
        cal=6
        ct = 3
    if(cal == 6 and ct == 2):
        cal=7
        ct = 3
    if(cal == 7 and ct == 2):
        cal=1
        ct = 3
    


