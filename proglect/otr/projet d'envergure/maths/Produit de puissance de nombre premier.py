nb=int(input("quel est ton  nombre ?:"))
i=2
div=tuple()
while nb>=i:
    if nb%i==0:
        nb=nb/i
        div+=(i,)
    else:i+=1
verif=1
for i in div:
    verif=verif*i
print(verif)
print(div)
