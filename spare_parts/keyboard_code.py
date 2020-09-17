import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

# variables for the buttons used later in the code
first_button = Keycode.SPACE
second_button = Keycode.SPACE
third_button = Keycode.SPACE
fourth_button = Keycode.SPACE


debounce_time = 0.5

# define output LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# flash the LED when booting
for x in range(0, 5):

	led.value = False
	time.sleep(0.2)
	led.value = True
	time.sleep(0.2)

# configure device as keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# define buttons
D0 = DigitalInOut(board.D0)
D0.direction = Direction.INPUT
D0.pull = Pull.UP

D1 = DigitalInOut(board.D1)
D1.direction = Direction.INPUT
D1.pull = Pull.UP

D2 = DigitalInOut(board.D2)
D2.direction = Direction.INPUT
D2.pull = Pull.UP

D3 = DigitalInOut(board.D3)
D3.direction = Direction.INPUT
D3.pull = Pull.UP

D4 = DigitalInOut(board.D4)
D4.direction = Direction.INPUT
D4.pull = Pull.UP

D5 = DigitalInOut(board.D5)
D5.direction = Direction.INPUT
D5.pull = Pull.UP

D6 = DigitalInOut(board.D6)
D6.direction = Direction.INPUT
D6.pull = Pull.UP

D7 = DigitalInOut(board.D7)
D7.direction = Direction.INPUT
D7.pull = Pull.UP


# loop forever
while True:

	if not D0.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(first_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D1.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(second_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D3.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(third_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D4.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(fourth_button) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D5.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(Keycode.SPACE) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D6.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(Keycode.SPACE) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off

	if not D7.value:

		# press the SPACEBAR
		led.value = False # led on
		kbd.send(Keycode.SPACE) # press the SPACEBAR
		time.sleep(debounce_time)  # debounce delay
		led.value = True # led off
