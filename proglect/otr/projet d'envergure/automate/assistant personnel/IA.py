import os,os.path
rep=""
#help
def halp():
      print("voici la liste de mes commandes monsieur:")
      print("-help: ce que vous venez de faire")
      print("-")
#jeux
def jeux():
      k=input("1)rqcourcis 2)games 3)jeux 5)tout\n")
      if k=="1" or k=="5":
            os.system("start C:\\Bureau\\rqccourcis")
      if k=="2" or k=="5":
            os.system("start E:\\Games")
      if k=="3" or k=="5":
            os.system("start E:\\perso\\jeux")
      print("voici votre dossier")
      

print("bonjour, que puis-je faire pour vous monsieur ?")
while rep!="exit" and rep!="stop":
      rep=input()
      if rep=="help":
            halp()
      if rep=="calc":
            print("voici votre calculatrice")
            os.system("calc")
      if rep=="jeux":
            jeux()
      if rep=="task":
            print("voici votre gestionnaire de taches")
            os.system("C:\WINDOWS\system32\Taskmgr.exe")
      if rep!="exit" and rep!="stop":
            print("ensuite que puis-je faire ? ")
      else: print(" au revoir et a tres bientot monsieur")      
