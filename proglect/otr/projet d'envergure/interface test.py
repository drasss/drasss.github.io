from tkinter import *
import time,random
x1=0
x2=4
y1=0
def write():
      label = Label(fenetre, text="Hello World")
      label.pack()
def drawline():
      global x1, x2,y1
      y2=random.randint(0,1000)
      can1.create_line(x1,y1,x2,y2,width=2,fill='red')
      x1+=4
      x2+=4
      y1=y2
fenetre = Tk()
can1 = Canvas(fenetre,bg='dark grey',height=1000,width=500)
can1.pack(side=LEFT)

bou1=Button(fenetre,text='ecrire un truc',command=write)
bou1.pack()
bou2=Button(fenetre,text='draw a line',command=drawline)
bou2.pack()
fenetre.mainloop()


