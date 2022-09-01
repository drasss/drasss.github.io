import random
B=""
for i in range(100):
    A=random.randint(90,122)
    if 89<A<=96:
        A=32
    B=B+chr(A)
print(B)
