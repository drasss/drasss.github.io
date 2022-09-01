import math,time
prm=(2,3)
lim=int(input("on va jusqu'ou ?"))+1

st=time.time()
##trouver les nombres premiers
def prime(i):
    divi=""
    for j in range(1,i):
        if i%j==0:
            divi=divi+str(j)
    if divi=="1":return(True)
    else:return(False)
    
##voir si ils s'additionnent
final=""
for i in range(4,lim):
    aff="---"
    bol=False
    jref=0
    kref=0
    if i%2==0:
        final+="-"
    for j in prm:
        for k in prm:
            if j+k==i:
                bol=True
                aff=str(j)+"+"+str(k)
    final+=str(i)+")"+aff+"\n"
    if prime(i):
        prm+=(i,)
nd=time.time()
print(final)
#ecriture dans un fichier txt pour des stats

#lim
fichier=open("lim.txt","r")
lect=fichier.read()
fichier.close()
lect+=","+str(lim)
fichier=open("lim.txt","w")
fichier.write(lect)
fichier.close()
#time
fichier=open("time.txt","r")
lect=fichier.read()
fichier.close()
lect+=","+str(nd-st)
fichier=open("time.txt","w")
fichier.write(lect)
fichier.close()
#data
fichier=open("data.txt","w")
fichier.write(final)
fichier.close()
