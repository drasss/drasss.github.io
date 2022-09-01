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

diviseur=tuple()
for i in range(2,len(x)-1):
      if len(x)%i==0 and len(x)/i!=2:
            diviseur+=(i,)
print(diviseur)

Rs=tuple()

ptperiod=tuple()
for i in diviseur:
      Rp=tuple()
      nbperiod=int(len(X)/i)
      for k in range(i):
      
            SregX=tuple()
            SregY=tuple()
            for j in range(nbperiod):
                  SregX+=(X[i*j+k],)
                  SregY+=(Y[j*i+k],)
            SX=np.array(SregX)
            SY=np.array(SregY)
            #reglin
            Xb=SX.mean()
            Yb=SY.mean()
            SCT=0
            SXX=0
            SXY=0
            for m in range(len(SX)):
                  SXX+=(SX[m]-Xb)*(SX[m]-Xb)
                  SXY+=(SX[m]-Xb)*(SY[m]-Yb)
                  SCT+=(SY[m]-Yb)*(SY[m]-Yb)
            a=SXY/SXX
            b=Yb-a*Xb
            SCR=0
            Yc=tuple()
            for m in range(len(SX)):
                  Yc+=(a*SX[m]+b,)
                  SCR+=(Yc[m]-Yb)*(Yc[m]-Yb)
            Rp+=(SCR/SCT,)
      Rp=np.array(Rp)
      Rs+=(Rp.mean(),)
print(Rs)
mxx=Rs[0]
argmxx=0
for i in range(len(Rs)):
      if mxx<Rs[i]:
            mxx=Rs[i]
            argmxx=i
print(" la periode est de ",diviseur[argmxx])
