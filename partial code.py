keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

while True:
    event=keys.events.get()
    if event:
        if event.pressed:
            if event.key_number == 1:
                keyboard.send(Keycode.A)
            if event.key_number == 0:
                mouse.press(Mouse.LEFT_BUTTON)
        else:
            pass
            