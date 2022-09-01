import math
import numpy as np
import matplotlib.pyplot as plt
a=int(input("bornes: "))
ecart=int(input("nb points "))

k=np.array(range(ecart))
k=k*(2*a/ecart)-a
rep=0*k
esp=rep*0
som=0
for i in range(len(k)):
      esp[i]=1/(math.sqrt(math.pi*2))*math.exp(-k[i]*k[i]/2)
      som+=esp[i]
      rep[i]=som
rep=rep/rep[i]
plt.plot(range(len(k)),rep,range(len(k)),esp)
plt.show()
