import sys, math
from random import random
from itertools import tee
from PyQt5 import QtCore, QtWidgets, QtGui

class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *args):
        QtWidgets.QGraphicsView.__init__(self, *args)

        self.scene = QtWidgets.QGraphicsScene(self)

    def clear_scene(self):
        self.scene.clear()

    def draw_frame(self, h, r_vert, r_hor, r_in, r_out, modifier=lambda x: x):
        self.h2 = h / 2
        if h > 0 and r_vert > 0 and r_hor > 0 and r_in > 0 and r_out > 0 and \
                math.sqrt((self.h2-r_vert) ** 2 / (self.h2 ** 2 + (self.h2-r_vert) ** 2)) * self.h2 >= r_out and \
                self.h2-r_vert > 0 and self.h2 - r_hor > 0 and r_in < r_out:
            self.scene.clear()
            self.draw_grid(grid_size=int(1.2*h), modifier=modifier)
            self.draw_figure(h, r_vert, r_hor, r_in, r_out, modifier=modifier)

    def draw_grid(self, grid_size=100, modifier=lambda x, y: (x, y)):
        X = self._convert_x(grid_size)
        _X = self._convert_x(-grid_size)
        Y = self._convert_y(grid_size)
        _Y = self._convert_y(-grid_size)
        for x in range(-grid_size, grid_size + 1, 30):
            _x = self._convert_x(x)
            _xt1, _Yt = modifier(_x, _Y)
            _xt2, Yt = modifier(_x, Y)
            text = QtWidgets.QGraphicsTextItem()
            text.setPos(*(modifier(_x - 25, Y - 30)))
            text.setPlainText('{:>5}'.format(x))
            self.scene.addLine(_xt1, _Yt, _xt2 , Yt)
            self.scene.addItem(text)
        for y in range(-grid_size, grid_size + 1, 30):
            _y = self._convert_y(y)
            _Xt, _yt1 = modifier(_X, _y)
            Xt, _yt2 = modifier(X, _y)
            text = QtWidgets.QGraphicsTextItem()
            text.setPos(*(modifier(_X - 50, _y - 10)))
            text.setPlainText('{:>5}'.format(-y))
            self.scene.addLine(_Xt, _yt1, Xt, _yt2)
            self.scene.addItem(text)

    def draw_figure(self, h, r_vert, r_hor, r_in, r_out,
            modifier=lambda x, y: (x, y)):
        pen = QtGui.QPen(QtCore.Qt.red)
        for x1, y1, x2, y2 in self._create_item(h, r_vert, r_hor, r_in, r_out):
            x1, y1 = modifier(x1, y1)
            x2, y2 = modifier(x2, y2)
            self.scene.addLine(x1, y1, x2, y2, pen)
        self.setScene(self.scene)

    def _create_item(self, h, r_vert, r_hor, r_in, r_out):
        from app.drawer import draw_bow, default_figure
        prec = 100
        for polygon_t in default_figure(h, r_vert, r_hor, r_in, r_out):
            polygon = ((self._convert_x(x), self._convert_y(y))
                       for x, y in polygon_t)
            x, y = next(polygon)
            for xt, yt in polygon:
                yield (x, y, xt, yt)
                x, y = xt, yt

    def _convert_x(self, x):
        return x

    def _convert_y(self, y):
        return -y
