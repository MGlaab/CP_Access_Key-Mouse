import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import neopixel
import key_functions
import file_to_change

pixels = neopixel.NeoPixel(board.D10, 1, brightness=0.3, auto_write=False)

# The pins we'll use, each will have an internal pullup
keypress_pins = [board.D1, board.D2, board.D3, board.D4, board.D5]
# Our array of key objects
key_pin_array = []

mode_counter = 0 # define delay to smooth the buttons
debounce_time = 0.2
# you must add colors to this array if you add more modes
mode_color = [RED, YELLOW, GREEN, BLUE, CYAN]

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

print("Waiting for key pin...")
while True:
    # Check the mode button
    if not D0.value:
        mode_counter += 1
        print(mode_counter)
        time.sleep(debounce_time)  # debounce delay

        if mode_counter > (len(keys_pressed)-1):
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
            print(i)
            key = keys_pressed2[mode_counter][i]
            print(key)

            if "MOUSE" in key:
                mouse_config(key[1])

            if "KEYBOARD" in key:
                keyboard_config(key[1])

            if "MOUSE MOVE X" in key:
                mouse_config_move_x(key[1])

            if "MOUSE MOVE Y" in key:
                mouse_config_move_y(key[1])

            # Turn off the red LED
            led.value = False

    pixels.fill(mode_color[mode_counter])
    pixels.show()

    time.sleep(0.01)
