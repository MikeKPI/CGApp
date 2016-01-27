import math


class Parabola:
    def __init__(self, delta=0.1, e=1, p=1):
        self._delta = delta
        self.e, self.p = e, p
        self._r = lambda phi: p / (1 - e * cos(phi))

    def __iter__(self):
        new_iter = deepcopy(self)
        new_iter.phi = 0.5 if self.e > 0 else -0.5
        return new_iter

    def __next__(self):
        if self.phi > pi:
            raise StopIteration

        r = self._r(self.phi)
        x, y = r * sin(self.phi), r * cos(self.phi)
        self.phi += self._delta
        return x, y


class Cissoid:
    def __init__(self, from_x=-200, to_x=200, a=30, points=100):
        self._a = a
        self.from_x = min(from_x, to_x)
        self.to_x = max(from_x, to_x)
        self.points = points

    def get_y(self, x):
        a = self._a * x
        return 2 * math.sqrt(a if a > 0 else -a)

    def derivative(self, x):
        x1 = x - 0.001
        x2 = x + 0.001
        y1 = self.get_y(x1)
        y2 = self.get_y(x2)
        ny = lambda x: (x - x1) * (y2 - y1) / (x2 - x1) + y1
        return ((x-50, ny(x-50)), (x+50, ny(x+50)))

    def __iter__(self):
        get_point = lambda x: (x, self.get_y(x))
        delta = (self.to_x - self.from_x) / self.points
        return map(get_point, (self.from_x + i * delta for i in range(self.points + 1)))
