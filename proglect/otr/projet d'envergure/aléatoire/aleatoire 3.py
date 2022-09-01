import random
B=''
for i in range(100):
    A=random.randint(0,2)
    if 0==A:
        B=B+"o"
    if 1==A:
        B=B+"-"
    if 2==A:
        B=B+" "
print(B)
