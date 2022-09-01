import math
import numpy as np
aff=""
tab=()
sol=()
const=math.e
for p in range(1,10000):
    i=int(p/4+1)
    supp=1
    while i<p:
        if abs(p/supp-const)>abs(p/i-const):
            supp=i
        i+=1
    tab+=(p/supp,)
    sol+=(supp,)
    aff+="-------------\n"+str(p)+" "+str(p)+"/"+str(supp)+"="+str(p/supp)
fichier=open("dat.txt","w")
fichier.write(aff)
fichier.close()
err=np.array(tab)
minn=err[0]
k=1
for i in range(len(err)):
    err[i]=abs(err[i]-const)
    if minn>err[i]:
        minn=err[i]
        k=i+1
print("le best est : ",k," car :")
print(k,"/",sol[k-1],"=",tab[k-1])
