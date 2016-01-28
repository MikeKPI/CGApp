import sys, math
from random import random
from itertools import tee
from PyQt5 import QtCore, QtWidgets, QtGui

class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *args):
        QtWidgets.QGraphicsView.__init__(self, *args)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.modifier = lambda x, y: (x, y)

    def clear_scene(self):
        self.scene.clear()

    def draw_asisses(self, x_lbl, y_lbl):
        self.scene.clear()

        axis_pen = QtGui.QPen(QtCore.Qt.black)

        self.scene.addLine(0, 0, 100, 0, axis_pen)    # X axis
        self.scene.addLine(0, 0, 0, 100, axis_pen)    # Y axis

        x_lbl_text = QtWidgets.QGraphicsTextItem()
        x_lbl_text.setPos(70, -20)
        x_lbl_text.setPlainText('{:>5}'.format(x_lbl))
        self.scene.addItem(x_lbl_text)
        y_lbl_text = QtWidgets.QGraphicsTextItem()
        y_lbl_text.setPos(-30, 80)
        y_lbl_text.setPlainText('{:>5}'.format(y_lbl))
        self.scene.addItem(y_lbl_text)
        o_point_text = QtWidgets.QGraphicsTextItem()
        o_point_text.setPos(-30, -20)
        o_point_text.setPlainText('{:>5}'.format("0"))
        self.scene.addItem(o_point_text)

        self.setScene(self.scene)

    def _convert_xy(self, x, y):
        _x, _y = self.modifier(x, y)
        return (_x, -_y)

    def add_line(self, f, t):
        try:
            f = self._convert_xy(*f)
            t = self._convert_xy(*t)
            self.scene.addLine(*(f + t))
            self.setScene(self.scene)
        except Exception:
            return
