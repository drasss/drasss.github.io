import time
import mouse
import keyboard
import random
points=0
ct=-1
triche=input("triche ou pas triche ? y/n ")
for i in range(3):
    x=random.randint(100,1300)
    y=random.randint(100,520)
    ct=ct+1
    ko=mouse.get_position()
    while ct==points:
        k=mouse.get_position()
        if abs(k[0]-x)>abs(k[1]-y) :
            if k[0]<(x-25):
                print("a droite")
            if k[0]>(x+25):
                print("a gauche")
        if abs(k[0]-x)<abs(k[1]-y) :
            if k[1]<(y-25):
                print("en bas")
            if k[1]>(y+25):
                print("en haut")
        if (x-25)<k[0]<(x+25)and(y-25)<k[1]<(y+25):
            print("c'est la !")
            if mouse.is_pressed(button="left"):
                points=points+1
        if triche=='y':
            if k[0]==x and k[1]==y:
                mouse.press(button="left")
                time.sleep(1)
            else:
                mouse.move(x,y,duration=0.5)
print(points)
