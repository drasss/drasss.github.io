import math
k=int(input("on montre les diviseurs des nombres jusqu'ou ? "))
divi=""
for i in range(100000001,k+1):
    for j in range(1,i):
        if i%j==0:
            divi=divi+" "+str(j)
    if divi==" 1":
        divi+=" --p--"
    print(i,":",divi)
    divi=""
