# SPDX-FileCopyrightText: 2024 Bill Binko
# SPDX-FileCopyrightText: 2024 Matthew Glaab
# SPDX-License-Identifier: MIT

#############################################################
# 3D printable case files can be found here:
# https://github.com/MGlaab/CP_Access_Key-Mouse/tree/master/TRRS%20Trinkey%20case%20STL's
#############################################################

import digitalio
import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# ONLY CHANGE THESE TWO VARIABLES
# SEE HERE FOR KEYBOARD KEY NAMES:
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
# SEE HERE FOR MOUSE BUTTON NAMES/FUNCTIONS:
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-mouse-mouse
#############################################################
# key/click you want to press
KEYBOARD_INPUT = Keycode.SPACEBAR
MOUSE_INPUT = Mouse.LEFT_BUTTON
#############################################################


# DO NOT TOUCH/CHANGE CODE FROM HERE DOWN, SERIOUSLY.
#############################################################

# functions
def keyboard_config(key_to_be_pressed):
    keyboard = Keyboard(usb_hid.devices)
    #layout = KeyboardLayoutUS(keyboard)
    keyboard.send(key_to_be_pressed)

def mouse_config(key_to_be_pressed):
    mouse = Mouse(usb_hid.devices)
    mouse.click(key_to_be_pressed)

#We are only using Ring1 and Tip as input - set Ring2 & sleeve to GND
ground = digitalio.DigitalInOut(board.RING_2)
ground.direction=digitalio.Direction.OUTPUT
ground.value = False

ground2 = digitalio.DigitalInOut(board.SLEEVE)
ground2.direction=digitalio.Direction.OUTPUT
ground2.value = False


#Use Keypad library to read buttons wired between ground and Tip/Ring1
keys = keypad.Keys((board.TIP,board.RING_1), value_when_pressed=False, pull=True)

#Main loop for events
while True:
    event=keys.events.get()
    if event:
        if event.pressed:
            if event.key_number == 1:
                print("keyboard")
                keyboard_config(KEYBOARD_INPUT)
            if event.key_number == 0:
                print("mouse")
                mouse_config(MOUSE_INPUT)
        else:
            pass
