from app.point import Point


class Curve:
    def __init__(self, fpoint, tpoint, hpoint):
        self.fpoint = fpoint
        self.tpoint = tpoint
        self.hpoint = hpoint

    def __iter__(self):
        return self._curve_iterator()

    def _curve_iterator(self):
        for i in range(0, 101, 5):
            t = i / 100
            A = (1 - t) ** 2
            B = (1 - t) * t
            C = t ** 2
            denominator = A + B + C

            yield Point((A * self.fpoint.x + B * self.hpoint.x + C * self.tpoint.x) / denominator,
                        (A * self.fpoint.y + B * self.hpoint.y + C * self.tpoint.y) / denominator)
