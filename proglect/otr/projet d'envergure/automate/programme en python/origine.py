import os
import os.path
g="1"
prr=input("quel nom au programme ?")
while os.path.exists(prr+g+".py"):
    g=int(g)+1
    g=str(g)
name = prr+g+".py"
print("voici les choix possibles")
fichier = open(name, "x")

        
                    
fichier.close()
