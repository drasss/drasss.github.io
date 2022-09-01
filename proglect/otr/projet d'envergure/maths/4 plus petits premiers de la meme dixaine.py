import math
i=int(10)
while i!=-1:
    print(i)
    bo=True
    for j in range(10):
        for k in range(round(math.sqrt(i+j))):
            if (i+j)%(k+1)!=0:
                bo=False
    rem=i
    i+=10
    if not(bo):
        i=-1
    else:
        print(rem,"  ",bo)
