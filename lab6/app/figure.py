import math
import numpy as np

STEPS = 30
ALPHA = math.pi / 6
MAX_R = 10
MIN_Z = -MAX_R
MAX_Z = MAX_R / math.sin(ALPHA)
dZ = (MAX_Z -MIN_Z) / STEPS
CHANGE_LINE = MAX_R * math.sin(ALPHA)


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x * 10
        self.y = y * 10
        self.z = z * 10

    def to_vector(self=None):
        return np.matrix([self.x, self.y, self.z, 1])

    def __repr__(self):
        return "<Point({x} {y} {z})>".format(x=self.x, y=self.y, z=self.z)

class Line:
    def __init__(self, from_p, to_p):
        self.from_p = from_p
        self.to_p = to_p

    def __iter__(self):
        return (getattr(self, attr) for attr in self.__dict__)

    def __repr__(self):
        return "<Line({f} {t})>".format(f=self.from_p, t=self.to_p)

class Figure:
    def __init__(self, figure=None):
        try:
            self.points = figure['points']
            self.lines = figure['lines']
        except Exception:
            self.points = []
            self.lines = []

def rsf(z):
    if z < CHANGE_LINE:
        return math.sqrt(MAX_R**2 - z**2)
    else:
        return (MAX_Z - z) * math.tan(ALPHA)

zs = [MIN_Z + dZ * i for i in range(STEPS + 1)]
rs = list(map(rsf, zs))
dphi = math.pi / STEPS * 2
xs = [[r * math.cos(dphi * i) for i in range(STEPS + 1)] for r in rs]
ys = [[r * math.sin(dphi * i) for i in range(STEPS + 1)] for r in rs]
zs = [[z for _ in range(STEPS + 1)] for z in zs]

xyzs = list(map(lambda *t: list(zip(*t)), xs, ys, zs))

figure = Figure({
    "points": [Point(x, y, z) for xyz in map(zip, xs, ys, zs) for x, y, z in xyz],
    "lines": [Line(Point(*xyz[i-1]), Point(*xyz[i]))
              for xyz in map(lambda *t: list(zip(*t)), xs, ys, zs)
              for i in range(1, STEPS+1)] + \
             [Line(Point(*xyzs[i-1][j]), Point(*xyzs[i][j]))
               for i in range(1, STEPS+1)
               for j in range(STEPS+1)]
})
