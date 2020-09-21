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
pins = [sr.get_pin(n) for n in range(8)]
