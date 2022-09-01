import math
p=input("on prend quel nombre ?: ")
p=int(p)
qte=int(p/4)
i=qte
supp=1
while i<p:
    if abs(p/supp-math.pi)>abs(p/i-math.pi):
        supp=i
    i+=1
print(supp)
print(p,"/",supp,"=",p/supp)
print(math.pi)
