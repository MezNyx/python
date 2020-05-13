#!/usr/bin/env python3

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

sense = SenseHat()

R = [255, 0, 0]
G = [0, 255, 0]
W = [255, 255, 255]
X = [
    W, R, R, R, R, R, R, W,
    R, W, R, R, R, R, W, R,
    R, R, W, R, R, W, R, R,
    R, R, R, W, W, R, R, R,
    R, R, R, W, W, R, R, R,
    R, R, W, R, R, W, R, R,
    R, W, R, R, R, R, W, R,
    W, R, R, R, R, R, R, W
]
O = [
    G, G, W, W, W, W, G, G,
    G, W, W, G, G, W, W, G,
    W, W, G, G, G, G, W, W,
    W, G, G, G, G, G, G, W,
    W, G, G, G, G, G, G, W,
    W, W, G, G, G, G, W, W,
    G, W, W, G, G, W, W, G,
    G, G, W, W, W, W, G, G
]
STATE = ""

while True:
    for event in sense.stick.get_events():
        if event.action == 'released' and event.direction == 'middle':
            if STATE == "":
                sense.set_pixels(X)
                STATE = "X"
            elif STATE == "X":
                sense.set_pixels(O)
                STATE = "O"
            elif STATE == "O":
                sense.clear()
                STATE = ""
