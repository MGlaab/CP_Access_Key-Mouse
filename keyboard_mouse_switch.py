# Import the libraries
import time
import board
from digitalio import DigitalInOut, Direction, Pull

#keyboard and mouse related libraries
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid
from adafruit_hid.mouse import Mouse

# define delay to smooth the buttons
debounce_time = 0.2

# first button
D1 = DigitalInOut(board.D1)
D1.direction = Direction.INPUT
D1.pull = Pull.UP

# second button
D2 = DigitalInOut(board.D2)
D2.direction = Direction.INPUT
D2.pull = Pull.UP

# third button
D3 = DigitalInOut(board.D3)
D3.direction = Direction.INPUT
D3.pull = Pull.UP

# fourth button
D4 = DigitalInOut(board.D4)
D4.direction = Direction.INPUT
D4.pull = Pull.UP

# loop forever
while True:

	if not D1.value:
		# configure device as  keyboard
		kbd = Keyboard(usb_hid.devices)
		layout = KeyboardLayoutUS(kbd)
		kbd.send(Keycode.SPACE) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D2.value:
		# configure device as mouse
		mouse = Mouse(usb_hid.devices)
		mouse.click(Mouse.LEFT_BUTTON) # press the Left MOUSE Button
		time.sleep(debounce_time)  # debounce delay
	if not D3.value:
		# configure device as mouse
		mouse = Mouse(usb_hid.devices)
		mouse.move(-10) # move the mouse right 10
	if not D4.value:
		# configure device as mouse
		mouse = Mouse(usb_hid.devices)
		mouse.move(10) # move the mouse left 10
