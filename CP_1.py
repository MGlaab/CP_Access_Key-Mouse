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
