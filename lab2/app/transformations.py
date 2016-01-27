import math
import numpy as np


def rotate(angle, x, y, x0, y0):
    angle = math.radians(angle)
    _x = x0 + (x - x0) * math.cos(angle) - (y - y0) * math.sin(angle)
    _y = y0 + (x - x0) * math.sin(angle) + (y - y0) * math.cos(angle)
    return _x, _y

def move(x, y, dx, dy):
    move_matrix = np.matrix([
        [1, 0, 0],
        [0, 1, 0],
        [dx, dy, 0]
    ])
    return (np.matrix([x, y, 1]) * move_matrix).tolist()[0][:2]
