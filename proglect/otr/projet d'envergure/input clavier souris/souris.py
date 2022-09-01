import time
import mouse
import keyboard
tout=mouse.get_position()
ct=False
CTG=False
x=0
y=0
i=1
while keyboard.is_pressed("o")==False:
    k=mouse.get_position()
    tout=tout+k
    print(k)
    time.sleep(0.03)
print(tout)
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
time.sleep(1)
while keyboard.is_pressed("o")==False:
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
