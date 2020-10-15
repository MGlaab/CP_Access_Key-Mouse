import board
import digitalio
import gamepad
import time

B_UP = 1 << 0
B_DOWN = 1 << 1


pad = gamepad.GamePad(
    digitalio.DigitalInOut(board.D10),
    digitalio.DigitalInOut(board.D11),
)

y = 0
while True:
    buttons = pad.get_pressed()
    if buttons & B_UP:
        y -= 1
        print(y)
    elif buttons & B_DOWN:
        y += 1
        print(y)
    time.sleep(0.1)
    while buttons:
        # Wait for all buttons to be released.
        buttons = pad.get_pressed()
        time.sleep(0.1)
