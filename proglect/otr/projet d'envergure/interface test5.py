from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

#grid(row=1,column=0,padx=5,pady=5)
root = Tk()
root.title('Tkinter Color Chooser')
k="yellow"
kt="blue"

canvas = Canvas(root, width=15, height=15, background=k)
canvas.grid(row=2,column=0,padx=5,pady=5)
canvas = Canvas(root, width=15, height=15, background=kt)
canvas.grid(row=2,column=1,padx=5,pady=5)
def change_color():
      global k
      colors = askcolor(title="Tkinter Color Chooser")
      k=colors[1]
      canvas = Canvas(root, width=15, height=15, background=k)
      canvas.grid(row=2,column=0,padx=5,pady=5)
def change_colort():
      global kt
      colors = askcolor(title="Tkinter Color Chooser")
      kt=colors[1]
      canvas = Canvas(root, width=15, height=15, background=kt)
      canvas.grid(row=2,column=1,padx=5,pady=5)


base=Button(
    root,
    text='Select a Color',
    command=change_color).grid(row=1,column=0,padx=5,pady=5)
text=Button(
    root,
    text='Select a Color for the text',
    command=change_colort).grid(row=1,column=1,padx=5,pady=5)


root.mainloop()
