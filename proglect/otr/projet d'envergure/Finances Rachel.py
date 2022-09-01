from tkinter import *
fenetre = Tk()
val=tuple()
i=0
def write():
      global val,entree,i
      k = entree.get()
      label = Label(fenetre, text=k)
      label.pack()
      print(k)
      val = val + (k,)
      print(val)
      i+=1
value = StringVar()
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()


label = Label(fenetre, text="Hello World")
label.pack()

bou1=Button(fenetre,text='send',command=write)
bou1.pack()
fenetre.mainloop()

