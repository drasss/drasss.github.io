import time
d=float
a=float
test=""
print("bonjour, quelle méthode voulez vous utiliser pour ce déchiffrage en césar ?")
choix=input(" 1)vous connaissez un mot  2)vous connaissez rien \n :")
trad="le texte traduit est: "
clé,choix1=0,"      "
texte=input(" quel est le texte a déchiffrer ? \n :")
texte=(" ",)+tuple(texte)
if choix=="1":
    choix1 = input("quel est le mot ? \n :")  
k=len(choix1)
choix1=choix1+" "
for i in range(k+1):
    texte= texte+(" ",)
    choix1=tuple(choix1)
d=time.time()


for i in range(24):
    ct=0
    lol=""
    for j in range(len(texte)-k):
         var=texte[j]
         if not(var==" " or var=="'" or var=="," or var=="."):
             var=ord(var)
             if var<97:
                  var=var+26
             var=var+i+1
             if var>122:
                  var=var-26
             var=chr(var)
         lol=lol+var
         if ct==k:
             clé=i
         #print(lol)
         verif=choix1[ct]
         if var==verif:
             ct=ct+1
         else:
             ct=0
    #print( str(i)+lol)
    if choix=="2":
        print(str(i)+lol)
if choix=="1":
    if clé==0:
        print("on n'a pas réussi")
    else:
        for i in range(len(texte)):
            var=texte[i]
            if var!=" ":
                supp=ord(var)
                supp=supp-clé
                if supp<97:
                    supp+=26
                supp=chr(supp)
            if var==" " or var=="'" or var=="," or var==".":
                supp=var
            trad=trad+supp
    if clé!=0:
        print(trad)
a=time.time()
print("ca a pris:",a-d," secondes")

