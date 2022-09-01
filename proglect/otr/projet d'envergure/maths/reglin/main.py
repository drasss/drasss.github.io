import numpy as np
import math
import matplotlib.pyplot as plt
fichier=open("data.txt","r")
txt=fichier.read()+"₾"
fichier.close()
X=tuple()
Y=tuple()
Yc=tuple()
tr=txt
wrd=""
i=1
while tr[i]!="#":
      if tr[i]!="," and tr[i]!="(" and tr[i]!=")" and tr[i]!="#":
            wrd+=tr[i]
      elif tr[i]!="," or tr[i]!=")":
            X+=(float(wrd),)
            wrd=""
      i+=1
while tr[i]!="(":
      i+=1
i+=1
while tr[i]!="#":
      if tr[i]!="," and tr[i]!="(" and tr[i]!=")" and tr[i]!="#":
            wrd+=tr[i]
      elif tr[i]!="," or tr[i]!=")":
            Y+=(float(wrd),)
            wrd=""
      i+=1
      
x=np.array(X)
y=np.array(Y)
adjust=" "
reps=tuple()
while adjust!="stop" and adjust!="":
      print(" press stop to stop the asjustements")
      print(" 1)sans ajustement / 2) on passe au log (ca a l'air exp) ")
      adjust=input("3)ajustement quadratique (ca a l'air racine) / 4) inverse \n")
      if adjust=="2":
            for i in range(len(y)):
                  y[i]=math.log(float(y[i]))
      if adjust=="3":
            for i in range(len(y)):
                  y[i]=y[i]*y[i]
      if adjust=="4":
            for i in range(len(y)):
                  y[i]=1/y[i]
      reps+=(adjust,)

Xb=x.mean()
Yb=y.mean()

SCT=0
SXX=0
SXY=0
for i in range(len(x)):
      SXX+=(x[i]-Xb)*(x[i]-Xb)
      SXY+=(x[i]-Xb)*(y[i]-Yb)
      SCT+=(y[i]-Yb)*(y[i]-Yb)
a=SXY/SXX
b=Yb-a*Xb

SCR=0
for i in range(len(x)):
      Yc+=(a*x[i]+b,)
      SCR+=(Yc[i]-Yb)*(Yc[i]-Yb)
R2=SCR/SCT

if b<0:
      signe="-"
else:
      signe="+"
print("l'équation est: "+str(a)+"x "+signe+" "+str(abs(b)))
print("R²= "+str(R2))

XX=(x[0],x[len(x)-1])
YY=(Yc[0],Yc[len(x)-1])
plt.plot(x,y,"b.")
plt.plot(XX,YY,"b")
plt.show()
predict=int(input("une valeur a predire peut être ? (entrer la lim)\n"))
yp=a*predict+b
tot=len(reps)
for i in range(tot):
      if reps[tot-i-1]=="2":
            yp=math.exp(yp)
      if reps[tot-i-1]=="3":
            yp=math.sqrt(yp)
      if reps[tot-i-1]=="4":
            yp=1/yp
print(yp)
