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
    p.direction = Direction.OUTPUT
    pins[pin] = p

# use a dictionary
buttonIDtoKeycode = { 1: Keycode.C,
                      2: Keycode.O,
                      3: Keycode.O,
                      4: Keycode.L,
                      5: Keycode.SPACE,
                      6: Keycode.SHIFT}
