from PyQt5 import QtWidgets


class Figure(QtWidgets.QGraphicsItem):
    def __init__(self, curves):
        super(Figure, self).__init__()

        self.curves = curves
        self.points = []
        for curve in self.curves:
            self.points += [curve.fpoint, curve.tpoint, curve.hpoint]

    def add_curve(self, curve):
        self.curves += [curve]
        self.points += [curve.fpoint, curve.tpoint, curve.hpoint]

    def get_same(self, point):
        return next(filter(point.__eq__, self.points))
