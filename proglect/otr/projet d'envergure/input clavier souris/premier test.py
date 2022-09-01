import keyboard
import time
import mouse
mouse.drag(-1000, -1000, 100, 225, absolute=False, duration=0.1)
mouse.click(button='left')
mouse.drag(0, 0, 400, 545, absolute=False, duration=0.1)
mouse.click(button='left')
keyboard.write("hey")
keyboard.send("backspace")
