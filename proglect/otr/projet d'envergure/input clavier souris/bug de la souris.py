import keyboard
import time
import mouse
import random
c = input("1)petite pute ou 2)gros bourin")
x=0
y=0
if c=="1":
    while keyboard.is_pressed('9')==False :
        mouse.move(5, 5, absolute=False, duration=0.01)
        mouse.move(-5, 5, absolute=False, duration=0.01)
        mouse.move(-5, -5, absolute=False, duration=0.01)
        mouse.move(5, -5, absolute=False, duration=0.01)
if c=="2":
    tout=mouse.get_position()
    while keyboard.is_pressed('9')==False :
        mouse.move(random.randint(100,3000),random.randint(100,620),duration=0.01)
        tout=tout+mouse.get_position()
    for i in range(len(tout)):
        if i%2==0:
            x=x+tout[i]
        if i%2==1:
            y=y+tout[i]
    i=(i+1)/2
    x=float(x/i)
    y=float(y/i)
    print("moyenne x = ",x)
    print("moyenne y = ",y)

