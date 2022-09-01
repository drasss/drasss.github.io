import keyboard
import time
import mouse
cpt=0
total=""
t=time.time()
print("7 pour arreter")
while not(keyboard.is_pressed("7")):
    if keyboard.is_pressed("shift"):
        cpt+=1
        total=total+"shift "
        print("shift ")
    if keyboard.is_pressed("w"):
        cpt+=1
        total=total+"w "
        print("w ")
    if keyboard.is_pressed("a"):
        cpt+=1
        total=total+"a "
        print("a ")
    if keyboard.is_pressed("s"):
        cpt+=1
        total=total+"s "
        print("s ")
    if keyboard.is_pressed("d"):
        cpt+=1
        total=total+"d "
        print("d ")
    if keyboard.is_pressed("e"):
        cpt+=1
        total=total+"tir "
        print("tir ")
    if keyboard.is_pressed("space"):
        cpt+=1
        total=total+"saut "
        print("saut ")
    if mouse.is_pressed(button='left'):
        cpt+=1
        total=total+"attaque "
        print("attaque ")
    if mouse.is_pressed(button='right'):
        cpt+=1
        total=total+"smash "
        print("smash ")
    time.sleep(0.025)
k=time.time()-t
print(cpt/k ,"actions par secondes")
print("end")
print(total)
