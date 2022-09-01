import random,time
import numpy as np
#l'idée c'est de faire une sorte de jeu ou une suite d'actions a faire
#ensuite le robot part de 0 et se développera pour réussir a faire ces actions

#le jeu/action: créer des mots qui sonnent français

#objectif premier: retrouver le nom aurélien depuis un mot aléatoire

#input
solution="aurelien"
solution_Fract=()
solnb=()
for i in range(len(solution)):
      solution_Fract+=tuple(solution[i])
      solnb+=(ord(solution[i]),)
print(solution_Fract)
sol=np.array(solution_Fract)
a=()
b=()
begg=()
nbb=()
verif=np.array(range(len(sol)))
for i in range(len(sol)):
      a+=(1,)
      b+=(0,)
      begg+=("a",)
      nbb+=(0,)
a=np.array(a)
b=np.array(b)
zeros=np.array(b)
verif=np.array(a)
#traitement (random.random()*52-26,)
essaia=np.array((a,a,a,a,a,a,a,a,a,a))
essaib=np.array((b,b,b,b,b,b,b,b,b,b))
after=np.array((begg,begg,begg,begg,begg,begg,begg,begg,begg,begg))
afterint=np.array((nbb,nbb,nbb,nbb,nbb,nbb,nbb,nbb,nbb,nbb))
iterr=0
while verif.any()!=0:
      sauvegarde=np.array(after)
      for i in range(9):
            for j in range(len(sol)):
                  essaia[i,j]=essaia[i,j]*(random.random()*2-1)
                  essaib[i,j]=abs(essaib[i,j]+round((random.random()*verif[j]/3-verif[j]/6)))
      for i in range(10):
            for j in range(len(sol)):
                  afterint[i,j]=(abs(int(essaia[i,j])*ord(begg[j])+int(essaib[i,j])))
                  after[i,j]=chr(afterint[i,j])
      argmin=0
      minimum=1000000
      
      for i in range(len(verif)):
            verif[i]=sum(abs(solnb-afterint[i]))
            if verif[i]<minimum:
                  minimum=verif[i]
                  argmin=i
      print(verif)
      a=()
      b=()
      for i in range(10):
            a+=(tuple(essaia[argmin]),)
            b+=(tuple(essaib[argmin]),)
      essaia=np.array(a)
      essaib=np.array(b)
      
      
      iterr+=1
      
#on a appr l'approximation // sol la solution // verif la comparaison entre les deux

