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

# neopixel library
import neopixel

# define delay to smooth the buttons
debounce_time = 0.2

# neopixel pin
pixel_pin = board.D10
pixel = neopixel.NeoPixel(pixel_pin, 1, brightness=0.3, auto_write=False)

# define counter variable
counter = 0
# define delay to smooth the buttons
debounce_time = 0.2

# variables for the buttons used later in the code
firstmode_first_button = Keycode.SPACE
firstmode_second_button = mouse.LEFT_BUTTON
firstmode_third_button = Keycode.SPACE
firstmode_fourth_button = Keycode.SPACE
firstmode_fifth_button = Keycode.SPACE

secondmode_first_button = Keycode.SPACE
secondmode_second_button = Mouse.LEFT_BUTTON
secondmode_third_button = Keycode.SPACE
secondmode_fourth_button = Keycode.SPACE
secondmode_fifth_button = Keycode.SPACE

thirdmode_first_button = Keycode.SPACE
thirdmode_second_button = Mouse.LEFT_BUTTON
thirdmode_third_button = Keycode.SPACE
thirdmode_fourth_button = Keycode.SPACE
thirdmode_fifth_button = Keycode.SPACE

# MOUSE BUTTONS
fourthmode_first_button = Mouse.LEFT_BUTTON
fourthmode_second_button = Mouse.RIGHT_BUTTON
left  = -5
right =  5
up    = -5
down  =  5

# define buttons

# counter button
D0 = DigitalInOut(board.D0)
D0.direction = Direction.INPUT
D0.pull = Pull.UP

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

# fifth button
D5 = DigitalInOut(board.D5)
D5.direction = Direction.INPUT
D5.pull = Pull.UP

# loop forever
while True:
	# mode button logic
	if not D0.value:
		counter += 1
		print(counter)
		time.sleep(debounce_time)  # debounce delay

		if counter > 3:
			counter = 0

	# first mode button logic
	if not D1.value and counter ==1:
		kbd.send(firstmode_first_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D2.value and counter ==1:
		kbd.send(firstmode_second_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D3.value and counter ==1:
		kbd.send(firstmode_third_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D4.value and counter ==1:
		kbd.send(firstmode_fourth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D5.value and counter ==1:
		kbd.send(firstmode_fifth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay

	# second mode button logic
	if not D1.value and counter ==2:
		kbd.send(secondmode_first_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D2.value and counter ==2:
		kbd.send(secondmode_second_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D3.value and counter ==2:
		kbd.send(secondmode_third_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D4.value and counter ==2:
		kbd.send(secondmode_fourth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D5.value and counter ==2:
		kbd.send(secondmode_fifth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay

	# third mode button logic
	if not D1.value and counter ==3:
		kbd.send(thirdmode_first_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D2.value and counter ==3:
		kbd.send(thirdmode_second_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D3.value and counter ==3:
		kbd.send(thirdmode_third_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D4.value and counter ==3:
		kbd.send(thirdmode_fourth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
	if not D5.value and counter ==3:
		kbd.send(thirdmode_fifth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay

	# fourth mode button logic MOUSE BUTTONS
	if not D1.value and counter ==4:
		mouse.click(fourthmode_first_button) # press the Left MOUSE Button
		time.sleep(debounce_time)  # debounce delay
	if not D2.value and counter ==4:
		mouse.move(x=left) # move the mouse to the left
	if not D3.value and counter ==4:
		mouse.move(x=right) # move the mouse to the right
	if not D4.value and counter ==4:
		mouse.move(y=up) # move the mouse to the up
	if not D5.value and counter ==4:
		mouse.move(y=down) # move the mouse to the down
