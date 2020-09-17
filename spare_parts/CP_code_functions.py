# pins for outputs
out_pins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7]

# array for pins
pins = []

# setup for pins to be outputs
for p in out_pins:
    pin = DigitalInOut(p)
    pin.direction = Direction.OUTPUT
    pins.append(pin)
# arrays for the different modes
# each has five items, which correspond to the five buttons
first_mode_keys = [Keycode.SPACE, Keycode.SPACE, Keycode.SPACE, Keycode.SPACE, Keycode.SPACE]
second_mode_keys = []
third_mode_keys = []
fourth_mode_keys = [Mouse.LEFT_BUTTON, -10, 10, -10, 10] # click, move left, move right, move up, move down

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
