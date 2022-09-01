import keyboard,time
k="e"
while not(keyboard.is_pressed("+")):
      time.sleep(0.05)
      keyboard.send(k)
