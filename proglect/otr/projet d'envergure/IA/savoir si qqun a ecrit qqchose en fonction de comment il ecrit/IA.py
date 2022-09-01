import numpy as np
import os, os.path,time
lect = open("base.txt", "r", encoding="utf-8")
noms = lect.read() + " ₾"
lect.close()
tab = tuple()
i, j = 0, 0
st = ""
while noms[i] != "₾":
    while noms[i] != " " and noms[i] != "₾":
        st += noms[i]
        i += 1

    tab = tab + (st,)
    st = ""
    i += 1
motest=list()
nbtest=list()
for i in range(len(tab)):
    if tab[i]!="":
        if motest.count(tab[i])!=0:
            j=motest.index(tab[i])
            nbtest[j]+=1
        else:
            motest.append(tab[i])
            nbtest.append(1)
fractest=list(nbtest)
for i in range(len(motest)):
    fractest[i]=fractest[i]*100/len(tab)
    #print(nbtest[i]," : ",motest[i],"\n",fractest[i])
#---------------------------------test
lect = open("testerdessus.txt", "r", encoding="utf-8")
ph = lect.read() + " ₾"
lect.close()
phra = tuple()
i, j = 0, 0

while ph[i] != "₾":
    while ph[i] != " " and ph[i] != "₾":
        st += ph[i]
        i += 1

    phra = phra + (st,)
    st = ""
    i += 1
motph=list()
nbph=list()
for i in range(len(phra)):
    if tab[i]!="":
        if motph.count(phra[i])!=0:
            j=motph.index(phra[i])
            nbph[j]+=1
        else:
            motph.append(phra[i])
            nbph.append(1)
fracph=list(nbph)
for i in range(len(motph)):
    fracph[i]=fracph[i]*100/len(phra)
#chi deux
chid=0
for i in range(len(motph)):
    if motest.count(motph[i])==0:
        chid+=fracph[i]
    else:
        chid+=(fractest[i]-fracph[i])*(fractest[i]-fracph[i])/(fractest[i])
print(chid)
print(len(phra))
