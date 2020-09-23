# import main libraries
import time
import board
from digitialio import DigitalInOut, Direction, Pull
import usb_hid

# import keyboard and mouse libraries
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

# functions
def keyboard_config(key_to_be_pressed):
    kbd = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(kbd)
    kbd.send(key_to_be_pressed)

def mouse_config(key_to_be_pressed):
    mouse = Mouse(usb_hid.devices)
    mouse.click(key_to_be_pressed)

# negative is left
# positive is right
# negative is up
# positive is down
# format: mouse.move(x=50, y=-20)

def mouse_config_move_x(x_distance):
    mouse = Mouse(usb_hid.devices)
    mouse.move(x = x_distance, y = 0)

def mouse_config_move_y(y_distance):
    mouse = Mouse(usb_hid.devices)
    mouse.move(x = 0, y = y_distance)

# variables
mode_counter = 0
debounce_time = 0.2

# variables for keyboard buttons, so mode 1: first key, second key, third key, ...
# this is the only area that would need to be changed if the keys needed to be changed.

a_mode = [keyboard_config(Keycode.SPACE),  # SPACE
          mouse_config(mouse.LEFT_BUTTON), # LEFT MOUSE BUTTON
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE)]  # SPACE

b_mode = [keyboard_config(Keycode.SPACE),  # SPACE
          mouse_config(mouse.LEFT_BUTTON), # LEFT MOUSE BUTTON
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE)]  # SPACE

c_mode = [keyboard_config(Keycode.SPACE),  # SPACE
          mouse_config(mouse.LEFT_BUTTON), # LEFT MOUSE BUTTON
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE)]  # SPACE

d_mode = [keyboard_config(Keycode.SPACE),  # SPACE
          mouse_config(mouse.LEFT_BUTTON), # LEFT MOUSE BUTTON
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE),  # SPACE
          keyboard_config(Keycode.SPACE)]  # SPACE

# list comprehension https://learn.adafruit.com/74hc595/usage
in_pins  = [board.D0,   # Mode Input
            board.D1,   # 1st Input
            board.D2,   # 2nd Input
            board.D3,   # 3rd Input
            board.D4,   # 4th Input
            board.D5]   # 5th Input

out_pins = [board.D8,   # Red LED
            board.D9,   # Green LED
            board.D10]] # Blue LED

# use this notation to initialize the inputs
for pin in ["D0", "D1", "D2", "D3", "D4", "D5"]:
    p = DigitalInOut(getattr(board, pin))
    p.direction = Direction.INPUT
    p.pull = Pull.UP
    pins[pin] = p

# use this notation to initialize the outputs
for pin in ["D8", "D9", "D10"]:
    p = DigitalInOut(getattr(board, pin))
    p.direction = Direction.OUTPUT
    p.pull = Pull.UP
    pins[pin] = p

# use a dictionary
buttonIDtoKeycode = { 1: Keycode.C,
                      2: Keycode.O,
                      3: Keycode.O,
                      4: Keycode.L,
                      5: Keycode.SPACE,
                      6: Keycode.SHIFT}

https://learn.adafruit.com/vote-keyboard/software
import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = (0, 0, 0)

kbd = Keyboard()
kbdLayout = KeyboardLayoutUS(kbd)
state = []
pins = {}
buttonMap = [
    dict(row="D4", col="D0", id=1),
    dict(row="D4", col="D1", id=2),
    dict(row="D4", col="D2", id=3),
    dict(row="D3", col="D2", id=4),
    dict(row="D3", col="D0", id=5),
    dict(row="D3", col="D1", id=6)]

# Set up row pins
for pin in ["D4", "D3"]:
    p = DigitalInOut(getattr(board, pin))
    p.direction = Direction.OUTPUT
    pins[pin] = p

# Set up column pins
for pin in ["D0", "D1", "D2"]:
    p = DigitalInOut(getattr(board, pin))
    p.direction = Direction.INPUT
    p.pull = Pull.DOWN
    pins[pin] = p

buttonIDtoKeycode = {
    1: Keycode.V,
    2: Keycode.O,
    3: Keycode.T,
    4: Keycode.E,
    5: Keycode.SPACE,
    6: Keycode.ENTER}

while True:
	# Compare old and new state
    oldState = state
    newState = []
    newBtn = None
    for button in buttonMap:
        r = pins[button["row"]]
        r.value = True
        if pins[button["col"]].value:
            newState += [button["id"]]
            if not button["id"] in oldState:
                newBtn = button["id"]
        r.value = False
    # Press & release keys
    for oldID in oldState:
        if not oldID in newState:
            kbd.release(buttonIDtoKeycode[oldID])
            dot[0] = (0, 0, 0)
    if newBtn:
        kbd.press(buttonIDtoKeycode[newBtn])
        dot[0] = (255, 0, 0)
    state = newState

#new stuff
counter_array = ['mode 1','mode 2']
keys_pressed = {
    'mode 1': ['A', 'B', 'C', 'D', 'E'],
    'mode 2': ['F', 'G', 'H', 'I', 'J']}

print(keys_pressed[counter_array[0]][0])

# CircuitPython demo - Keyboard emulator

import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import neopixel

# A simple neat keyboard demo in CircuitPython

# RGB led(neopixel, WS28b12) related code
pixels = neopixel.NeoPixel(board.D10, 1, brightness=0.3, auto_write=False)

# color table for the neopixel (red, green, blue) 0-255
RED    = (255,   0,   0)
YELLOW = (255, 150,   0)
GREEN  = (  0, 255,   0)
CYAN   = (  0, 255, 255)
BLUE   = (  0,   0, 255)
PURPLE = (180,   0, 255)

# The pins we'll use, each will have an internal pullup
keypress_pins = [board.D1, board.D2, board.D3, board.D4, board.D5]
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
#keys_pressed = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E], # mode 1

keys_pressed = {
    'mode 1': [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E],
    'mode 2': [Keycode.F, Keycode.G, Keycode.H, Keycode.I, Keycode.J]}
control_key = Keycode.SHIFT

mode_counter = 0
counter_array = ['mode 1','mode 2']
# define delay to smooth the buttons
debounce_time = 0.2

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Setup the mode pin
D0 = digitalio.DigitalInOut(board.D0)
D0.direction = digitalio.Direction.INPUT
D0.pull = digitalio.Pull.UP

# Make all pin objects inputs with pullups
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    key_pin_array.append(key_pin)

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("Waiting for key pin...")

while True:
    # Check the mode button
    if not D0.value:
        mode_counter += 1
        print(mode_counter)
        time.sleep(debounce_time)  # debounce delay

        if mode_counter > 3:
            mode_counter = 0

    # Check each pin
    for key_pin in key_pin_array:
        if not key_pin.value:  # Is it grounded?
            i = key_pin_array.index(key_pin)
            print("Pin #%d is grounded." % i)

            # Turn on the red LED
            led.value = True

            while not key_pin.value:
                pass  # Wait for it to be ungrounded!
            # "Type" the Keycode or string
            key = keys_pressed[keys_pressed[counter_array[mode_counter]][i]]  # Get the corresponding Keycode or string
            keyboard.press(control_key, key)  # "Press"...
            keyboard.release_all()  # ..."Release"!

            # Turn off the red LED
            led.value = False

    time.sleep(0.01)

# CircuitPython demo - NeoPixel
import time
import board

import usb_hid
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import neopixel

# functions
def keyboard_config(key_to_be_pressed):
    kbd = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(kbd)
    kbd.send(key_to_be_pressed)

def mouse_config(key_to_be_pressed):
    mouse = Mouse(usb_hid.devices)
    mouse.click(key_to_be_pressed)

# negative is left
# positive is right
# negative is up
# positive is down
# format: mouse.move(x=50, y=-20)

def mouse_config_move_x(x_distance):
    mouse = Mouse(usb_hid.devices)
    mouse.move(x = x_distance, y = 0)

def mouse_config_move_y(y_distance):
    mouse = Mouse(usb_hid.devices)
    mouse.move(x = 0, y = y_distance)

# RGB led(neopixel, WS28b12) related code
pixels = neopixel.NeoPixel(board.D10, 1, brightness=0.3, auto_write=False)

# color table for the neopixel (red, green, blue) 0-255
RED    = (255,   0,   0)
YELLOW = (255, 150,   0)
GREEN  = (  0, 255,   0)
CYAN   = (  0, 255, 255)
BLUE   = (  0,   0, 255)
PURPLE = (180,   0, 255)

# variables
mode_counter = 0
debounce_time = 0.2


while True:
    pixels.fill(RED)
    pixels.show()
