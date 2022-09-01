import time,os,os.path
liste=open("Liste.txt","r",encoding="utf-8")
recup=liste.read()+"\n₾"
liste.close()
tab=tuple()
i=0
elt=""
while recup[i]!="₾":
      while recup[i]!="\n":
            elt+=recup[i]
            i+=1
      tab+=(elt,)
      elt=""
      i+=1
print("les éléments de la liste vont apparaitre un par un \n écrire o pour oui, x pour non et - pour peut etre")
endl=tuple()
i=0
while i<=(len(tab)-1):
      rep=input(tab[i]+" ")
      if rep=="o":
            endl+=(tab[i],)
            i+=1
      elif rep=="-":
            endl+=(tab[i]+"~~",)
            i+=1
      elif rep=="x":
            i+=1
date=time.gmtime()
if os.path.exists("listes\\"+str(date[0])+"-"+str(date[1])):
      path=".\\listes\\"+str(date[0])+"-"+str(date[1])
else:
      os.system("mkdir "+".\\listes\\"+str(date[0])+"-"+str(date[1]))
      path="listes\\"+str(date[0])+"-"+str(date[1])
Nlist=open(path+"\\"+str(date[0])+"-"+str(date[1])+"-"+str(date[2])+"-"+str(date[3])+"-"+str(date[4])+".txt","x")
for i in range(len(endl)):
      Nlist.write(endl[i]+"\n")
Nlist.close()
