import time
import board
import digitalio

import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)

button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

m = Mouse(usb_hid.devices)

while True:
    if button_A.value:  # button is pushed
        # Type lowercase 'a'. Presses the 'a' key and releases it.
        kbd.send(Keycode.A)
        while button_A.value:
            pass
    if button_B.value:  # button is pushed
        # Click the left mouse button.
        m.click(Mouse.LEFT_BUTTON)
        while button_B.value:
            pass

    time.sleep(0.01)
