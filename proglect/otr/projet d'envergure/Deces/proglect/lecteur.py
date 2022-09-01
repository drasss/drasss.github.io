from tkinter import *
import time,random,os,keyboard,time
fenetre = Tk()
#fonctions
def halp():
      os.system("start halp.bat")
def Repair():
      os.system("start .\ ")



OUTILS=Button(fenetre, text="OUTILS", command="", relief=FLAT).grid(row=1,column=0,padx=5,pady=5)

everything=Button(fenetre, text="Everything", command=everything).grid(row=1,column=1,padx=5,pady=5)
