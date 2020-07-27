import pynput.keyboard as k
import pynput.mouse as m
from PIL import ImageGrab, Image
import time

# Used:
# https://pynput.readthedocs.io/en/latest/mouse.html
# https://pynput.readthedocs.io/en/latest/keyboard.html

mouse = m.Controller()
keyboard = k.Controller()

print("BMC Ability Hotkey Script")
ability_amt = int(input("Enter amount of abilities (max 12): "))

print("Please click on the BMC window.")
with m.Listener(on_click=lambda x, y, b, p : False) as l:
	l.join()
	
print("Please click on each ability in order.")
print("NOTE: DO NOT CLICK THE COMMAND WINDOW OR THIS WILL BREAK!")
# see https://github.com/moses-palmer/pynput/issues/32 for a likely cause of this. I don't think I can fix this.

abl_pos = []

def on_click(x, y, button, pressed):
	global ability_amt
	if pressed:
		abl_pos.append((x, y))
		ability_amt -= 1
	return ability_amt > 0
	
with m.Listener(on_click=on_click) as l:
	l.join()

# uncomment below to see ability coordinates.
# key = 1
# for i in abl_pos:
	# print(str(key) + ": " + str(i))
	# key += 1

print("You can now press keys in range 1234567890-= to activate abilities.")
print("Press q to quit.")
	
def on_press(key):
	abl_keys = "1234567890-="
	try:
		if key.char in abl_keys:
			if abl_keys.index(key.char) < len(abl_pos):
				old = mouse.position
				mouse.position = abl_pos[abl_keys.index(key.char)]
				mouse.click(m.Button.left, 1)
				mouse.position = old
			else:
				print("Ability out of range! Coordinates not set!")
		if key.char == 'q':
			return False
	except AttributeError:
		pass  
		#ignore special keys like space, backspace 
		#necessary since those are common in gameplay and will cause this exception
	
	
with k.Listener(on_press=on_press) as l:
	l.join()