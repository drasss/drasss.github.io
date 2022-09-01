import os, os.path,time
lect = open("recup.txt", "r", encoding="utf-8")
noms = lect.read() + "₾"
lect.close()
tab = tuple()
i, j = 0, 0
st = ""
while noms[i] != "₾":
    while noms[i] != "\n" and noms[i] != "₾":
        st += noms[i]
        i += 1

    tab = tab + (st,)
    st = ""
    i += 1
print(tab)


