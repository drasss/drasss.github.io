import math
import numpy as np
chx=""
chy=""
i=0
X=tuple()
Y=tuple()
while chx!="stop":
      i+=1
      chx=input("x"+str(i)+" ? (stop) ")
      if chx!="stop":
            chy=input("y"+str(i)+" ? ")
            X+=(int(chx),)
            Y+=(int(chy),)
x=np.array(X)
y=np.array(Y)
Xb=x.mean()
Yb=y.mean()
SXX=0
SXY=0

SCT=0
for i in range(len(x)):
      SXX+=(x[i]-Xb)*(x[i]-Xb)
      SXY+=(x[i]-Xb)*(y[i]-Yb)
      SCT+=(y[i]-Yb)*(y[i]-Yb)
a=SXY/SXX
b=Yb-a*Xb

Yc=tuple()
SCR=0
for i in range(len(x)):
      Yc+=(a*x[i]+b,)
      SCR+=(Yc[i]-Yb)*(Yc[i]-Yb)
print("l'équation est "+str(a)+"X + "+str(b))
print("R²=",SCR/SCT)
