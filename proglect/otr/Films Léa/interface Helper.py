import os
import numpy as np
os.system("dir /B>>recup.txt")
fichier=open("recup.txt","r")
recupa=fichier.read()+"€"
fichier.close()
recup=tuple()
for i in range(len(recupa)):
      recup+=(recupa[i],)
recup=np.array(recup)
i=0
while recup[i]!="€":
      i+=1
      if recup[i]=="\\" and recup[i+1]=="n":
            recup[i+1]=""
            recup[i]="<\li>\n<li>"
recuv=""
for i in range(len(recup)):
      recuv+=recup[i]
print(recup)
