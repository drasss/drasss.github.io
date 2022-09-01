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
        time.sleep(0.01)
    if keyboard.is_pressed("w"):
        cpt+=1
        total=total+"w "
        print("w ")
        time.sleep(0.01)
    if keyboard.is_pressed("a"):
        cpt+=1
        total=total+"a "
        print("a ")
        time.sleep(0.01)
    if keyboard.is_pressed("s"):
        cpt+=1
        total=total+"s "
        print("s ")
        time.sleep(0.01)
    if keyboard.is_pressed("d"):
        cpt+=1
        total=total+"d "
        print("d ")
        time.sleep(0.01)
    if keyboard.is_pressed("e"):
        cpt+=1
        total=total+"tir "
        print("tir ")
        time.sleep(0.01)
    if keyboard.is_pressed("space"):
        cpt+=1
        total=total+"saut "
        print("saut ")
    if mouse.is_pressed(button='left'):
        cpt+=1
        total=total+"attaque "
        print("attaque ")
        time.sleep(0.01)
    if mouse.is_pressed(button='right'):
        cpt+=1
        total=total+"smash "
        print("smash ")
        time.sleep(0.01)
k=time.time()-t
print(cpt/k ,"actions par secondes")
print("end")
print(total)
