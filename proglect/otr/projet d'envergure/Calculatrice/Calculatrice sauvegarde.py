from tkinter import *
import time,random,os,keyboard,time
import numpy as np
fenetre = Tk()
#fonctions

opera=""

#---------------opérations possibles----------------------
def clir():
      global opera
      opera=""
      print(opera)
def clire():
      global opera
      oper=""
      for i in range(len(opera)-1):
            oper+=opera[i]
      opera=oper
      print(opera)
def zer(kit):
      global opera
      opera+="0"
      print(opera)
def zera():
      global opera
      opera+="1"
      print(opera)
def zerb():
      global opera
      opera+="2"
      print(opera)
def zerc():
      global opera
      opera+="3"
      print(opera)
def zerd():
      global opera
      opera+="4"
      print(opera)
def zere():
      global opera
      opera+="5"
      print(opera)
def zerf():
      global opera
      opera+="6"
      print(opera)
def zerg():
      global opera
      opera+="7"
      print(opera)
def zerh():
      global opera
      opera+="8"
      print(opera)
def zeri():
      global opera
      opera+="9"
      print(opera)
def mult():
      global opera
      opera+="*"
      print(opera)
def div():
      global opera
      print(opera)
      opera+="/"
def add():
      global opera
      opera+="+"
      print(opera)
def dell():
      global opera
      opera+="-"
      print(opera)
def bo():
      global opera
      opera+="("
      print(opera)
def bc():
      global opera
      opera+=")"
      print(opera)
#---------------Calcul de l'opération----------------------


#--------------isoles les parties avec des parentheses et demandes a calcul() de calculer ce qu'il y a dedans
def parentheses(opera):
      stropera=opera
      opera=np.array(tuple(str(opera)),dtype='<U9')
      i=0
      while opera[i-1]!="(":
            if opera[i]=="(":
                  cpt=0
                  st=""
                  j=1
                  while cpt!=0 or opera[i+j]!=")":
                        if opera[i+j]=="(":
                              cpt+=1
                        elif opera[i+j]==")":
                              cpt+=-1
                        st+=opera[i+j]
                        j+=1
            i+=1
      res=calcul(st)
      opera=np.array(tuple(opera),dtype='<U9')
      opera[i-1]=res[0]
##      print(opera)
      for k in range(j):
            opera=np.delete(opera,i)
##      print("apres parentheses ",opera)
      operation=""
      for i in range(len(opera)):
            operation+=opera[i]
##      print("operation ",operation)
      return(operation)



#---------------calcules ce qu'on lui donne et si il y a des parentheses, renvoies le calcul a parentheses()
def calcul(opera):
      st=""
      tab=()
      opera=opera
##      print("opera ",opera)
      boll=False
      while not(boll) or i!=len(opera)-1:
            st=""
            tab=()
            boll=False
##            print("opera ",opera)
            for i in range(len(opera)):
##                  print("i ",opera[i])
                  if 47<ord(opera[i])<58 or opera[i]==".":
                        st+=opera[i]

                  else:
                        if opera[i]=="(":
                              boll=True
                        else:
                              if opera[i]==")":
                                    tab+=(str(st),)
                              else:
                                    tab+=(str(st),opera[i])
                              st=""
            if boll:
                  apres=parentheses(opera)
                  tab+=(apres,)
                  opera=apres
            else: boll=True
      tab+=(str(st),)
##      print(tab)
      tab=np.array(tab,dtype='<U9')
      #---------multiplications ou divisions----------
##      print("tab ",tab)
      i=0
      while i<len(tab):
            
            if tab[i]=="*":
                  tab[i-1]=str(float(tab[i+1])*float(tab[i-1]))
                  tab=np.delete(tab,i+1)
                  tab=np.delete(tab,i)
                  i=i-1
            if tab[i]=="/":
                  tab[i-1]=str(float(tab[i-1])/float(tab[i+1]))
                  tab=np.delete(tab,i+1)
                  tab=np.delete(tab,i)
                  i=i-1
##            print(i,"tab m-d ",tab)
            i+=1
      #---------additions ou soustractions----------
      i=0
      while i<len(tab):
            if tab[i]=="+":
                  tab[i-1]=str(float(tab[i+1])+float(tab[i-1]))
                  tab=np.delete(tab,i+1)
                  tab=np.delete(tab,i)
                  i=i-1
            if tab[i]=="-":
                  tab[i-1]=str(float(tab[i-1])-float(tab[i+1]))
                  tab=np.delete(tab,i+1)
                  tab=np.delete(tab,i)
                  i=i-1
##            print(i,"tab a-s",tab)
            i+=1
##      print(tab)
      return(tab)      
def egal():
      global opera,tab
##      print(opera)
      st=""
      tab=()
      i=0
      bol=False
      for i in range(len(opera)):
            if opera[i]=="(":
                  bol=True
      if bol:opera=parentheses(opera)
      
      reponse=calcul(opera)
      print("----------la réponse est: ",round(float(reponse[0]),2))
      clir()
#---------------------------------------------------------
equal=Button(fenetre, text="=", command=egal).grid(row=0,column=0,padx=5,pady=5)
clear=Button(fenetre, text="C", command=clir).grid(row=0,column=1,padx=5,pady=5)
clearE=Button(fenetre, text="CE", command=clire).grid(row=0,column=2,padx=5,pady=5)

paro=Button(fenetre, text="   (   ", command=bo).grid(row=4,column=2,padx=5,pady=5)
parc=Button(fenetre, text="   )   ", command=bc).grid(row=4,column=3,padx=5,pady=5)

zero=Button(fenetre, text="   0   ", command=zer).grid(row=4,column=1,padx=5,pady=5)
fenetre.bind("0",zer)

zeroa=Button(fenetre, text="   1   ", command=zera).grid(row=1,column=1,padx=5,pady=5)
zerob=Button(fenetre, text="   2   ", command=zerb).grid(row=1,column=2,padx=5,pady=5)
zeroc=Button(fenetre, text="   3   ", command=zerc).grid(row=1,column=3,padx=5,pady=5)
zerod=Button(fenetre, text="   4   ", command=zerd).grid(row=2,column=1,padx=5,pady=5)
zeroe=Button(fenetre, text="   5   ", command=zere).grid(row=2,column=2,padx=5,pady=5)
zerof=Button(fenetre, text="   6   ", command=zerf).grid(row=2,column=3,padx=5,pady=5)
zerog=Button(fenetre, text="   7   ", command=zerg).grid(row=3,column=1,padx=5,pady=5)
zeroh=Button(fenetre, text="   8   ", command=zerh).grid(row=3,column=2,padx=5,pady=5)
zeroi=Button(fenetre, text="   9   ", command=zeri).grid(row=3,column=3,padx=5,pady=5)
fois=Button(fenetre, text="   x   ", command=mult).grid(row=1,column=4,padx=5,pady=5)
divv=Button(fenetre, text="   /   ", command=div).grid(row=2,column=4,padx=5,pady=5)
plus=Button(fenetre, text="   +   ", command=add).grid(row=3,column=4,padx=5,pady=5)
moins=Button(fenetre, text="   -   ", command=dell).grid(row=4,column=4,padx=5,pady=5)
fenetre.mainloop()
