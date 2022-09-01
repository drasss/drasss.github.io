import random,time
import matplotlib.pyplot as plt
import numpy as np
#l'idée c'est de faire une sorte de jeu ou une suite d'actions a faire
#ensuite le robot part de 0 et se développera pour réussir a faire ces actions

#le jeu/action: retrouver la fonction random
#sous la forme random.randint(a,b)=[(x*y+z)%(b-a+1)]+a
#avec x y ou z la seed
#on va devoir tester avec x la seed uniquement (si c'est y ca va se permuter, si c'est z on aura z*1+(x*y))

#definition de notre propre fonction de nombres aléatoires
def rd(x):
      y=(((x)*384400+(x*time.time()%100))%100001)/10000 -5
      return(y)
#input
essai=int(input("on essaye combien de fois ?\n"))

sid=500
apros=100

random.seed(sid)
appr=tuple()
data=tuple()
for i in range(apros):
      appr+=(0,)
      data+=((1.0,1.0,1.0),) #dans l'ordre x , y , z
appr=np.array(appr)*0 #vecteur de 10 approximations avec un x un y et un z associé
verif=1*appr
data=0*np.array(data)

#initialisation de quoi visualiser
soluce=(0,)
trouve=(0,)

#traitement
x=float(sid)
y=float(50)
z=float(19)
a=0
b=1000
for i in range(essai):
      sol=random.randint(a,b)
      soluce+=(sol,)
      best=b
      argbest=0
      data[0]=data[argbest]
      for j in range(apros):
            if j!=0:
                  data[j,0]=x
                  data[j,1]=y+rd(j+x)*3
                  data[j,2]=z+rd(apros-j+x)*3

            appr[j]=((data[j,0]*data[j,1]+data[j,2])%(b-a+1))+a
            
            verif[j]=abs(sol-appr[j])
            if best>verif[j]:
                  argbest=j
                  best=verif[j]
      (x,y,z)=data[argbest]
      print(i," ",x," ",y," ",z)
      x=appr[argbest]
      trouve+=(appr[argbest],)

#output
trouve=np.array(trouve)
soluce=np.array(soluce)
print(trouve)
print(soluce)
print(abs(trouve-soluce))
plt.plot(range(len(trouve)),trouve,range(len(soluce)),soluce)
plt.plot(range(len(trouve)),abs(trouve-soluce))
plt.show()
