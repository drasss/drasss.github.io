from tkinter import *
import time,random,os,keyboard,time
fenetre = Tk()
#fonctions
def halp():
      os.system("start halp.bat")
def Repair():
      os.system("start .\ ")
def everything():
      os.system("start E:\\\"kali linux mate\"\\Everything\\Everything.exe")
def Clavier_Visuel():
      os.system("start .\\funct\oskk")
def ControlP():
      os.system("control")
def Perso():
      os.system("start E:\perso")
def calcul():
      os.system("calc")
def Shutdown10():
      os.system("shutdown -s -t 10")
def ShutdownSTOP():
      os.system("shutdown -a")
def SNIPPINGTOOL():
      os.system("start .\\funct\SNIPPINGTOOLL")
def DPyth():
      os.system("start E:\programme\python")
def WINR():
      keyboard.press_and_release("windows+r")
def tskmgr():
      os.system("start .\\funct\\tskmgr")
def accesor():
      os.system("start .\\funct\Accesoires")
def Tcarac():
      os.system("start .\\funct\CHRMAP")
def CMD():
      os.system("start .\\funct\cmd")
def Rdom():
      os.system("start .\\funct\Random")
def JournalW():
      os.system("start E:\\\"Internet Explorer\"\\ADONIS\\\"Journal Adonis.docx\"")
def JournalP():
      os.system("start ..\\\"Journal intime\"\journal.py")
def txtsit():
      os.system("start funct\\Opera.txt")
def opensite():
      lect = open("funct\\Opera.txt", "r", encoding="utf-8")
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
      for i in tab:
            os.system("start "+i)
#------------------------sous menu------------------------
def Lecteur():
      #fonctions
      def oplect():
            os.system("start E:\\perso\\telechargement\\audacity\\proglect\\lecteur.html")
      def fresh():
            os.system("start E:\\perso\\telechargement\\audacity\\proglect\\lecteur.py")
      def CSSch():
            os.system("start funct\CSS.bat")
      def YTMP3():
            os.system("start funct\\YT.bat")

      #boutons
      lectmenu=Tk()
      openit=Button(lectmenu,text="ouvrir le Lecteur MP3",command=oplect).grid(row=0,column=0,padx=5,pady=5)
      refresh=Button(lectmenu,text="renouveler les musiques",command=fresh).grid(row=0,column=1,padx=5,pady=5)
      CSS=Button(lectmenu,text="Changer le style",command=CSSch).grid(row=0,column=2,padx=5,pady=5)
      YT=Button(lectmenu,text="Youtube -> Mp3",command=YTMP3).grid(row=1,column=0,padx=5,pady=5)

def menusite():
      #Fonctions
      #->adresse presse papier:||https://partage.univ-pau.fr/mail#5
      def mailuppa():
            os.system("start https://partage.univ-pau.fr/mail#5")
      def Elearn():
            os.system("start https://elearn.univ-pau.fr/my/")
      def Pscol():
            os.system("start https://www.apogee-pau.u-bordeaux.fr/")
      def rnot():
            os.system("start https://mdw-prod.univ-pau.fr/mondossierweb-1.6.9/#!notesView")
      def resultats():
            os.system("start https://www.apogee-pau.u-bordeaux.fr/resultats/")
      #boutons
      menu=Tk()
      rvnotes=Button(menu, text="Relevé de notes fac", command=rnot).grid(row=0,column=0,padx=5,pady=5)
      resultat=Button(menu, text="Resultats fac", command=resultats).grid(row=0,column=1,padx=5,pady=5)
      portailscol=Button(menu, text="Portail scolarité", command=Pscol).grid(row=1,column=0,padx=5,pady=5)
      elearn=Button(menu, text="Elearn", command=Elearn).grid(row=1,column=1,padx=5,pady=5)
      smtpuppa=Button(menu, text="Mail uppa", command=mailuppa).grid(row=2,column=0,padx=5,pady=5)
      
      menu.mainloop()
def mat():
      #fonctions
      def MAT():
            os.system("start E:\programme\python\maths")
      def fichrl():
            os.system("start E:\programme\python\maths\\reglin\data.txt")
      def recuprl():
            os.system("start funct\\recuperateurrl")
      def rl():
            os.system("start E:\programme\python\maths\\reglin\main.py")
      #Boutons
      matk=Tk()
      MATHS=Button(matk, text="MATHS", command=MAT).grid(row=0,column=0,padx=5,pady=5)
      Fichreglin=Button(matk, text="datas Reglin", command=fichrl).grid(row=0,column=1,padx=5,pady=5)
      recuperateurreglin=Button(matk, text="recuperateur Reglin", command=recuprl).grid(row=0,column=2,padx=5,pady=5)
      reglin=Button(matk, text="Reglin", command=rl).grid(row=0,column=3,padx=5,pady=5)
#---------------------------------------------------------
#premiere ligne (Outils)
OUTILS=Button(fenetre, text="OUTILS", command="", relief=FLAT).grid(row=1,column=0,padx=5,pady=5)

everything=Button(fenetre, text="Everything", command=everything).grid(row=1,column=1,padx=5,pady=5)
Control=Button(fenetre, text="Panneau De Configuration", command=ControlP).grid(row=1,column=2,padx=5,pady=5)
calc=Button(fenetre, text="Calc", command=calcul).grid(row=1,column=3,padx=5,pady=5)
task=Button(fenetre, text="Gest-Taches", command=tskmgr).grid(row=1,column=4,padx=5,pady=5)
Clavisu=Button(fenetre, text="Clavier Visuel", command=Clavier_Visuel).grid(row=1,column=5,padx=5,pady=5)
CaptEcr=Button(fenetre, text="Capture Ecran", command=SNIPPINGTOOL).grid(row=1,column=6,padx=5,pady=5)

#premiere ligne suite(OUTILS2)
CARAC=Button(fenetre, text="Table de Caracteres", command=Tcarac).grid(row=2,column=1,padx=5,pady=5)
Randd=Button(fenetre, text="Nombre Aléatoire", command=Rdom).grid(row=2,column=2,padx=5,pady=5)
Journw=Button(fenetre, text="Journal intime W", command=JournalW).grid(row=2,column=3,padx=5,pady=5)
Journp=Button(fenetre, text="Journal intime P", command=JournalP).grid(row=2,column=4,padx=5,pady=5)
Maths=Button(fenetre, text="Maths", command=mat).grid(row=2,column=5,padx=5,pady=5)
MP3=Button(fenetre, text="Lecteur Mp3", command=Lecteur).grid(row=2,column=6,padx=5,pady=5)
#deuxieme ligne (Dossiers)
DOSSIERS=Button(fenetre, text="DOSSIERS", command="", relief=FLAT).grid(row=3,column=0,padx=5,pady=5)

perso=Button(fenetre, text="Perso", command=Perso).grid(row=3,column=1,padx=5,pady=5)
Pyth=Button(fenetre, text="Dossier Python", command=DPyth).grid(row=3,column=2,padx=5,pady=5)
accesoire=Button(fenetre, text="Accesoires Windows", command=accesor).grid(row=3,column=3,padx=5,pady=5)

#Troisiemme ligne(commandes Windows)
COMWIN=Button(fenetre, text="COMMANDES WINDOWS", command="", relief=FLAT).grid(row=4,column=0,padx=5,pady=5)

CMD=Button(fenetre, text="CMD", command=CMD).grid(row=4,column=1,padx=5,pady=5)
SD=Button(fenetre, text="Shutdown 10s", command=Shutdown10).grid(row=4,column=2,padx=5,pady=5)
SDST=Button(fenetre, text="Shutdown STOP", command=ShutdownSTOP).grid(row=4,column=3,padx=5,pady=5)
Win_R=Button(fenetre, text="Windows + R", command=WINR).grid(row=4,column=4,padx=5,pady=5)


#quatrieme ligne (internet)
COMint=Button(fenetre, text="OPERA", command="", relief=FLAT).grid(row=5,column=0,padx=5,pady=5)

opensites=Button(fenetre, text="Open Sites", command=opensite).grid(row=5,column=1,padx=5,pady=5)
txtsites=Button(fenetre, text="Fichier sites", command=txtsit).grid(row=5,column=2,padx=5,pady=5)
Menusites=Button(fenetre, text="Menus Sites", command=menusite).grid(row=5,column=3,padx=5,pady=5)


#tout en bas (raltif au programme)
Repar=Button(fenetre, text="Repair", command=Repair).grid(row=6,column=1,padx=5,pady=5)
halp=Button(fenetre, text="help", command=halp).grid(row=6,column=2,padx=5,pady=5)
fenetre.mainloop()
