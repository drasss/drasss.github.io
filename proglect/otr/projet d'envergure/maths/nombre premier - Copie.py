import math,keyboard
divi=""
i=0
while keyboard.is_pressed("9")==False:
    i+=1
    for j in range(1,i):
        if i%j==0:
            divi=divi+" "+str(j)
    if divi==" 1":
        divi+=" --p--"
    print(i,":",divi)
    divi=""
