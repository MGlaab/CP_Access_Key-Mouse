def keyboard_config(key_to_be_pressed):
    kbd = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(kbd)
    kbd.send(key_to_be_pressed)     # Keycode.A

def mouse_config(key_to_be_pressed):
    mouse = Mouse(usb_hid.devices)
    mouse.click(key_to_be_pressed)  # Mouse.LEFT_BUTTON

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
