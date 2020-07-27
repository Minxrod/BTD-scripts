import pynput.keyboard as k
import pynput.mouse as m
from PIL import ImageGrab, Image
import time

mouse = m.Controller()
keyboard = k.Controller()

max_click = int(input("Enter number of rounds: "))

print("Please click on the BTD window.")
with m.Listener(on_click=lambda x, y, b, p : False) as l:
	l.join()

print("Please hover over the round start button while no round is playing.")
print("Please do not move the mouse until the program has finished preparing.")

time.sleep(3)

p = mouse.position
mouse.move(-32, -32)
time.sleep(0.5) #included for btd6 compat, even though that's useless

print("You can now move the mouse normally.")

# This scaling works when Windows is set to scale everything by 125%. 
# See https://github.com/moses-palmer/pynput/issues/32
# I don't think I can fix this, so if this program doesn't work, 
# you can try switching which "t=" is enabled below.

# t = (p[0]/1535*1920, p[1]/863*1080, p[0]/1535*1920+16, p[1]/863*1080+16)
t = (p[0], p[1], p[0]+16, p[1]+16)

img = ImageGrab.grab(t)

clicks = 0
while clicks < max_click:
	img2 = None

	while img != img2:
		img2 = ImageGrab.grab(t)
		time.sleep(1)

	keyboard.type(" ")
	time.sleep(1)
	clicks += 1

print("Done.")