import time
d=time.time()
for i in range(100):
    print(i)
a=time.time()
print("1:",a-d)

d=time.time()
k=""
for i in range(100):
    k+=str(i)+"\n"
print(k)
a=time.time()
print("2:",a-d)

d=time.time()
k=0
r=""
while k!=99:
    r+=str(k)+"\n"
    k+=1
print(r)
a=time.time()
print("3:",a-d)
