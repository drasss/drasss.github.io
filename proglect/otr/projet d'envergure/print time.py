import time,math
import numpy as np
k=0
l=int(input("combien d'itérations ? "))
tm=tuple()
start=time.time()
while k<=l:
      print(k)
      if k%2==0:
            tm+=(time.time(),)
      k+=1
data=np.array(tm)
data+=-tm[0]
datam=0
sxx=0
sxy=0
for i in range(len(data)):
      datam+=(data[i])
datam=datam/len(data)
for i in range(len(data)):
      sxx+=(i-(len(data)/2))*(i-(len(data)/2))
      sxy+=(data[i]-datam)*(i-(len(data)/2))
a=sxy/sxx
b=datam-a/2*len(data)

print("a ",a," b ",b)

SCR=0
SCT=0
for i in range(len(data)):
      SCT=(data[i]-datam)*(data[i]-datam)
      SCR=(a*i+b-datam)*(a*i+b-datam)
print("R²= ",SCR/SCT)
