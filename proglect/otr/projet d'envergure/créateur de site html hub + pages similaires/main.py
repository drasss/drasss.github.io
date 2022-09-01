import numpy as np
import os
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *

tab=("#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF")

os.system("start docu.txt")
print("entres les données dans ce fichier texte, de la forme:")
print("(Titre;lien d'une image;petit texte)\n")
input("et ce pour chaque page que tu souhaites (ne pas mettre de poitn virgule ;)\n")


#choix des couleurs

root = Tk()
root.title('Tkinter Color Chooser')

##----------------couleur du bouton  bt
bt=tab[2]
canvas = Canvas(root, width=15, height=15, background=bt)
canvas.grid(row=2,column=0,padx=5,pady=5)
def change_color_button():
      global bt
      colors = askcolor(title="Tkinter Color Chooser")
      bt=colors[1]
      canvas = Canvas(root, width=15, height=15, background=bt)
      canvas.grid(row=2,column=0,padx=5,pady=5)
buton=Button(
    root,
    text='choisis une couleur pour le bouton',
    command=change_color_button).grid(row=1,column=0,padx=5,pady=5)
##----------------couleur du texte   color_text
color_text=tab[0]
canvas = Canvas(root, width=15, height=15, background=color_text)
canvas.grid(row=2,column=1,padx=5,pady=5)
def change_color_text():
      global color_text
      colors = askcolor(title="Tkinter Color Chooser")
      color_text=colors[1]
      canvas = Canvas(root, width=15, height=15, background=color_text)
      canvas.grid(row=2,column=1,padx=5,pady=5)
text=Button(
    root,
    text='Choisis une couleur pour le texte',
    command=change_color_text).grid(row=1,column=1,padx=5,pady=5)
##----------------couleur de la bande   color_band
color_band=tab[1]
canvas = Canvas(root, width=15, height=15, background=color_band)
canvas.grid(row=2,column=2,padx=5,pady=5)
def change_color_band():
      global color_band
      colors = askcolor(title="Tkinter Color Chooser")
      color_band=colors[1]
      canvas = Canvas(root, width=15, height=15, background=color_band)
      canvas.grid(row=2,column=2,padx=5,pady=5)
band=Button(
    root,
    text='Choisis une couleur pour la bande',
    command=change_color_band).grid(row=1,column=2,padx=5,pady=5)

##----------------Fond d'écran    Background
Background=tab[3]
def change_bck():
      global Background
      Background = askopenfilename(title="Ouvrir un fond d'écran",filetypes=[('Jpeg files','.jpg'),('png files','.png'),('all files','.*')])
bck=Button(
    root,
    text='Choisis un fond d\'écran',
    command=change_bck).grid(row=1,column=3,padx=5,pady=5)
root.mainloop()

fichier=open("docu.txt","r")
txt=fichier.read()+"₾₾"
fichier.close()
finaltab=tuple()
X=tuple()
tr=txt
wrd=""
i=1
while tr[i]!="₾":
    while tr[i]!="#" and tr[i]!="₾":
          if tr[i]!=";" and tr[i]!="(" and tr[i]!=")" and tr[i]!="#" and tr[i]!="₾":
                wrd+=tr[i]
          elif tr[i]!=";" or tr[i]!=")":
                X+=(wrd,)
                wrd=""
          i+=1
    while tr[i]!="(" and tr[i]!="₾":
          i+=1
    i+=1
    finaltab+=(X,)
    X=tuple()
HUB=input("quel titre veux-tu a ton hub ?\n")
