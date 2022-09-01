import random
import time
import os
import os.path
sum=float
sum=0
d= float
d = time.time()
for i in range(20):
    random.seed(time.time(),4*i)
    r=random.randint(0,10)
    random.seed(time.time()-1,4*(i+3)-2)
    k=random.randint(0,10)
    n=float
    n=1
    e=k*r
    e=int(e)
    print(i+1,")  Que font",r,"x",k," ? ")
    m=input("")
    m=int(m)
    if m!=e:
        print("faux")
        n=0.5
        print(i+1,"Que font",r,"x",k," ? ")
        m=input("")
        m=int(m)
        if m!=e:
            print("faux")
            n=0.25
            print(i+1,"Que font",r,"x",k," ? ")
            m=input("")
            m=int(m)
            if m!=e:
                print("faux")
                n=0
                print("le resultat était ",k*r)
    sum= float(sum)+n
a = float
a = time.time()
w=float
w=a - d
if w<32.0 and sum==20.0:
    sum=21.0

print(w,"secondes ont étées nécéssaires pour faire le quizz")
memoire=open("record.txt","r")
rec=float(memoire.read())
memoire.close()
print("le record est de "+str(rec)+" secondes")
if w<rec:
    os.remove("record.txt")
    print("et tu l'as battu félicitations !!")
    fichier=open("record.txt","x")
    fichier.write(str(w))
    fichier.close()
print("pour une note de ",sum,"/20")
    
