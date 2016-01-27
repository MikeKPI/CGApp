import sys, math, time
from random import random
from itertools import tee
from PyQt5 import QtCore, QtWidgets, QtGui
from app.transformations import rotate


class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *args):
        QtWidgets.QGraphicsView.__init__(self, *args)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.modifier = lambda x, y: (x, y)

    def clear_scene(self):
        self.scene.clear()

    def draw_figure(self, figure_iter, modifier=lambda x, y: (x, y)):
        self.figure_iter = figure_iter
        self.modifier = modifier

        figure_iter = iter(figure_iter)
        xp, yp = next(figure_iter)
        xp, yp = self._convert_xy(xp, yp)

        flag = True
        for xc, yc in figure_iter:
            xc, yc = self._convert_xy(xc, yc)
            self.scene.addLine(xp, yp, xc, yc)

            # self.scene.addLine(-xp, yp, -xc, yc)

            xp, yp = xc, yc

        self.setScene(self.scene)

    def draw_axis(self, from_x, to_x, a):
        A = 1.5
        B = 5
        self.scene.addLine(A * from_x, 0, A * to_x, 0)
        self.scene.addLine(0, -B * a, 0, B * a)
        self.setScene(self.scene)

    def _convert_xy(self, x, y):
        _x, _y = self.modifier(x, y)
        return (_x, -_y)

    def mousePressEvent(self, event):

        position = self.mapToScene(QtCore.QPoint(event.x(), event.y()))
        x, y = self._convert_xy(position.x(), self.figure_iter.get_y(position.x()))
        if abs(y - position.y()) < 10:
            tangent = self.figure_iter.derivative(x)
            p1x, p1y = self._convert_xy(tangent[0][0], tangent[0][1])
            p2x, p2y = self._convert_xy(tangent[1][0], tangent[1][1])
            self.scene.addLine(p1x, p1y, p2x, p2y,
                               QtGui.QPen(QtCore.Qt.blue))
            self.scene.addEllipse(x, y, 5, 5,
                                  QtGui.QPen(QtCore.Qt.red), QtGui.QBrush(QtCore.Qt.SolidPattern))


            x1, y1 = rotate(90, p1x, p1y, x, y)
            x2, y2 = rotate(90, p2x, p2y, x, y)

            self.scene.addLine(x1, y1, x2, y2,
                               QtGui.QPen(QtCore.Qt.green))

            self.setScene(self.scene)
