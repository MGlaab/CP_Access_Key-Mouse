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
    0: [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E],
    2: [Keycode.F, Keycode.G, Keycode.H, Keycode.I, Keycode.J],
    3: [Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O],
    4: [Keycode.P, Keycode.Q, Keycode.R, Keycode.S, Keycode.T],
    4: [Keycode.U, Keycode.V, Keycode.W, Keycode.X, Keycode.Y],
}
control_key = Keycode.SHIFT

mode_counter = 0
# define delay to smooth the buttons
debounce_time = 0.2
mode_color = [RED, YELLOW, GREEN, BLUE]

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
            print(i)
            key = keys_pressed[mode_counter][i]
            print(key)
            #key = keys_pressed[keys_pressed[counter_array[mode_counter]][i]]  # Get the corresponding Keycode or string
            keyboard.press(key)  # "Press"...
            #keyboard.release_all()  # ..."Release"!

            # Turn off the red LED
            led.value = False
    
    pixels.fill(mode_color[mode_counter])
    pixels.show()

    time.sleep(0.01)
