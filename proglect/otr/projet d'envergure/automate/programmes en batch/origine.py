import os
import os.path
g="1"
while os.path.exists("programme "+g+" .bat"):
    g=int(g)+1
    g=str(g)
name = "programme "+g+" .bat"
print("voici les choix possibles")
fichier = open(name, "x")
fichier.write("@echo off")
fichier.write("\n:start")
ch = int
var = str
val = str
txt = str
got = str
suite = ""
suite = str(suite)
while ch!=0:
    print("0)fin 1)set /p 2)if var = nb goto 3)echo -4)set /a")
    ch = input("5):lbl 6)goto 7) if general 8)cmd 9)ou j'en suis 10)pause ")
    ch = int(ch)
    if ch==1:
        var = input("quelle variable ?  ")
        txt = input("quel texte ?  \n")
        com=("\nset /p "+var+"=\""+txt+"\"  ")
        
    if ch==2:
        var = input("quelle variable ?  ")
        val = input("quelle valeur ? ")
        got = input("goto quoi ? ")
        com=("\nif \"%"+var+"%\"==\""+val+"\" goto "+got)
        
    if ch==3:
        txt = input("quel texte mettre ? \n")
        com=("\necho "+txt)
        
    if ch==4: print("pas encore fini")

    if ch==5:
        txt = input("quel nom d'etiquette mettre ? \n")
        com=("\n:"+txt)
        
    if ch==6:
        got = input("a quelle étiquette se référer ? ")
        com=("\ngoto "+got)
        
    if ch==7:
        cnd = input("quelle est la condition ? ")
        cns = input("quelle est la conséquence ? ")
        com=("\nif "+cnd+" "+cns)
   
    if ch==8:
        txt=input("quelle est la commande cmd ? \n")
        com=("\n"+txt)
        
    if ch==10: com=("\npause")
    if ch==0 or ch==9: print(suite)
    else:
        fichier.write(com)
        suite= str(suite)+com
        
                    
fichier.close()
