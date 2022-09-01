import os
import os.path
import time
infoa = input("info 1)  ")
infob = input("info 2)  ")
infoc = input("info 3)  ")
infod = input("info 4)  ")
infoe = input("info 5)  ")
p = input("quelle région ?  ")
tim=time.time()
g=1
if os.path.exists("listes enregistrées"+"\\alla.txt"):
    while os.path.exists("listes enregistrées"+"\\alla"+str(g)+".txt"):
        g+=1
        print("ok")
name = "alla"+str(g)+".txt"
print(name)
fichier = open("listes enregistrées"+"\\"+name, "x")
ch = (infoa,infob,infoc,infod,infoe,"")
for ziz in range(6):
    a=ch[ziz]
    for aia in range(6):
        b=ch[aia]
        for bib in range(6):
            c=ch[bib]
            for cic in range(6):
                d=ch[cic]
                for did in range(6):
                    e=ch[did]
                    for eie in range(6):
                        f=ch[eie]
                        ziz=str(ziz)
                        aia=str(aia)
                        bib=str(bib)
                        cic=str(cic)
                        did=str(did)
                        eie=str(eie)
                        fichier.write("\n"+ziz+aia+bib+cic+did+eie)
                        fichier.write("\n"+a+b+c+d+e+f)
                        fichier.write("\n"+a+b+c+d+e+f+p)
                        fichier.write("\n"+a+b+c+d+e+f+p+"0")
                        fichier.write("\n"+a+b+c+d+e+f+p+"000")
                        fichier.write("\n"+a+b+c+d+e+f+p+"0001")
                        ziz=int(ziz)
                        aia=str(aia)
                        bib=str(bib)
                        cic=str(cic)
                        did=str(did)
                        eie=str(eie)
fichier.write("\n"+"1234567")
fichier.write("\n"+"password")
fichier.write("\n"+"Mot_de_Passe")
fichier.close()
print("fait en",time.time()-tim)
