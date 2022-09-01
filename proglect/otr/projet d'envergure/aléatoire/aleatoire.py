import random
while True:
    v=0
    for j in range(10000):
        k,i=0,0
        for i in range(1000):
            k=k+random.randint(0,100)
        u=k/(i+1)
        v=v+u
    v=v/(j+1)
    print("en tout la moyenne est de : ",v)
