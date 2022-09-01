import random
B=""
for i in range(10):
    for i in range(16):
        B=B+chr(random.randint(97,122))
    B=B+"\n"
print(B)
