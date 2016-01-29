import sys, math
from PyQt5 import QtCore, QtWidgets, QtGui

from app.point import Point


class MyGraphicsView(QtWidgets.QGraphicsView):

    clicked = QtCore.pyqtSignal(Point)

    def __init__(self, *args):
        QtWidgets.QGraphicsView.__init__(self, *args)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.modifier = lambda x, y: (x, y)

    def clear_scene(self):
        self.scene.clear()

    def _convert_xy(self, point):
        _x, _y = self.modifier(point.x, point.y)
        return Point(_x, _y)

    def add_line(self, f, t, width=2):
        try:
            f = self._convert_xy(f)
            t = self._convert_xy(t)
            pen = QtGui.QPen(QtCore.Qt.black)
            pen.setWidth(width)
            self.scene.addLine(f.x, f.y, t.x, t.y, pen)
            self.setScene(self.scene)
        except Exception as e:
            print('Ooops {}'.format(e))
            return

    def add_point(self, point, color=QtCore.Qt.red):
        point = self._convert_xy(point)
        self.scene.addEllipse(point.x, point.y, 5, 5, QtGui.QPen(color),
                              QtGui.QBrush(QtCore.Qt.SolidPattern))

    def mousePressEvent(self, event):
        position = self.mapToScene(QtCore.QPoint(event.x(), event.y()))
        self.clicked.emit(Point(position.x(), position.y()))
