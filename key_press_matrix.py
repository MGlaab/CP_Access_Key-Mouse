from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

"""
The format of this keys_pressed2 dictionary is as follows:
    There are as of right now five modes.
    For each mode there are five inputs.
        
        So, 25 possible combinations. You could add more, by adding more lines in the dictionary and more colors to the mode color list.
        Space on the chip is the limit.
        
        ...
        mode: [(input 1), (input 2),(input 3),(input 4),(input 5)]
        ...
        So, its a dictionary, and within the key/value pairs, the values are tuples(what's inside the () braces)
        Each input has a type:
            "MOUSE" for mouse clicks, not movement.
            "KEYBOARD" for keyboard keys.
            "MOUSE MOVE X" for horizontal movement of the mouse. Positive is to the right, negative to the left.
            "MOUSE MOVE Y" for vertical movement of the mouse. Positive is to the down, negative to the up.
                This matches the layout of your computer screen.
                
        mode: [(type of input, key/click/move you want to emulate),...] On through all the rest of the buttons.
        
        THE SYNTAX MATTERS. If you don't follow the format the code will not work. It's not the end of the world.
        Download the code from the github link and try again.

"""
keys_pressed2 = {
    0: [("MOUSE", Mouse.LEFT_BUTTON), ("KEYBOARD", Keycode.A), ("MOUSE MOVE X", 10), ("MOUSE MOVE Y", 10), ("MOUSE", Mouse.LEFT_BUTTON)],
    1: [("MOUSE", Mouse.LEFT_BUTTON), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A)],
    2: [("MOUSE", Mouse.LEFT_BUTTON), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A)],
    3: [("MOUSE", Mouse.LEFT_BUTTON), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A)],
    4: [("MOUSE", Mouse.LEFT_BUTTON), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A), ("KEYBOARD", Keycode.A)]
}