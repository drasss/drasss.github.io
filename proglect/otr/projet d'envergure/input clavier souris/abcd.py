import keyboard
import time
time.sleep(1)
for i in range(26):
    keyboard.send(chr(i+97))
