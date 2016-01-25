from math import cos, sin
import numpy as np

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x * 10
        self.y = y * 10
        self.z = z * 10

    def to_vector(self=None):
        return np.matrix([self.x, self.y, self.z, 1])

class Line:
    def __init__(self, from_p, to_p):
        self.from_p = from_p
        self.to_p = to_p

    def __iter__(self):
        return (getattr(self, attr) for attr in self.__dict__)

class Figure:
    def __init__(self, figure=None):
        try:
            self.points = figure['points']
            self.lines = [Line(self.points[f], self.points[t])
                          for f, t in figure['lines']]
        except Exception:
            self.points = []
            self.lines = []


figure = Figure({
    "points": [
        # first rectangle
        Point(1, 2, 2),
        Point(1, 2, 9),
        Point(6, 2, 2),
        Point(6, 2, 9),
        Point(1, 4, 2),
        Point(1, 4, 9),
        Point(6, 4, 2),     # line to second rect
        Point(6, 4, 9),     # line to second rect
        # second rectangle (num + 7)
        Point(3, 4, 3),
        Point(3, 4, 6),
        Point(6, 4, 3),     # line to first rect
        Point(6, 4, 6),     # line to first rect
        Point(3, 5, 3),     # line to third rect`
        Point(3, 5, 6),     # line to third rect
        Point(6, 5, 3),
        Point(6, 5, 6),
        # third rectangle (num + 16)
        Point(3, 5, 1),     # line to second rect
        Point(3, 5, 7),     # line to second rect
        Point(11, 5, 1),
        Point(11, 5, 7),
        Point(3, 6, 1),     # line to fourth
        Point(3, 6, 7),     # line to fourth
        Point(11, 6, 1),
        Point(11, 6, 7),    # line to fourth
        # fourth rectangle (num + 24)
        Point(3, 6, 5),     # line to third
        Point(3, 6, 7),     # line to third
        Point(5, 6, 5),
        Point(5, 6, 7),     # line to third
        Point(3, 9, 5),
        Point(3, 9, 7),
        Point(5, 9, 5),
        Point(5, 9, 7),
    ],
    "lines": [
        # first rectangle
        [0, 4], [1, 5], [2, 6], [3, 7], # vertical
        [0, 1], [1, 3], [3, 2], [2, 0], # top horizontal
        [4, 5], [5, 7], [6, 4], # bottom horizontal
        # second rectangle
        [8, 12], [9, 13], [10, 14], [11, 15], # vertical
        [8, 9], [9, 11], [10, 8], # top horizontal
        [13, 15], [15, 14], [14, 12], # bottom horizontal
        # third rectangle
        [16, 20], [17, 21], [18, 22], [19, 23], # vertical
        [17, 19], [19, 18], [18, 16], # top horizontal
        [23, 22], [22, 20], # bottom horizontal
        # fourth rectangle
        [24, 28], [25, 29], [26, 30], [27, 31], # vertical
        [27, 26], [26, 24], # top horizontal
        [28, 29], [29, 31], [31, 30], [30, 28], # bottom horizontal
        # connections
        [6, 10], [11, 7],       # first to second
        [16, 12], [13, 17],     # second to third
        [20, 24], [23, 27]      # third to fourth
    ]
})
