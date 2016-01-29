import sys
import os
import math
import pickle

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__name__))+'/app')

from PyQt5 import QtCore, QtWidgets, QtGui

from app.main_window_ui import Ui_Form
from app.figure import Figure
from app.point import Point
from app.curve import Curve


class MainWindow(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)

        self.picked = None
        self.mflag = False

        self.figure = Figure([])

        self.setupUi(self)
        self._connect_all()

        self.show()

    def _connect_all(self):
        self.open_pb.clicked.connect(self.choose_open_file_action)
        self.save_pb.clicked.connect(self.choose_save_file_action)
        self.add_pb.clicked.connect(self.add_curve_action)
        self.graphicsView.clicked.connect(self.gview_clicked_action)

    def choose_open_file_action(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()[0]
        # TODO: opening and reading from pickled file
        with open(filename, 'rb') as ifile:
            self.figure = pickle.Unpickler(ifile).load()
        self.draw()

    def choose_save_file_action(self):
        filename = QtWidgets.QFileDialog.getSaveFileName()[0]
        # TODO: seriliazation object with pickle and writing it to file
        with open(filename, 'wb') as ofile:
            pickle.Pickler(ofile).dump(self.figure)

    def add_curve_action(self):
        curve = Curve(Point(100, 100), Point(200, -40), Point(-100, 100))
        self.figure.add_curve(curve)
        self.draw()

    def draw(self):
        self.graphicsView.clear_scene()
        for curve in self.figure.curves:
            self.draw_curve(curve)

    def gview_clicked_action(self, point):
        print(self.picked)
        if self.picked is not None:
            for picked_point in filter(self.picked.__eq__, self.figure.points):
                picked_point.x = point.x
                picked_point.y = point.y
            self.picked = None
            self.draw()
        else:
            try:
                self.picked = next(filter(point.__eq__, self.figure.points))
                self.graphicsView.add_point(point, QtCore.Qt.green)
            except Exception:
                pass

    def draw_curve(self, curve):
        icurve = iter(curve)
        prev = next(icurve)
        for curr in icurve:
            self.graphicsView.add_line(prev, curr)
            prev = curr
        # self.graphicsView.add_point(curve.fpoint)
        # self.graphicsView.add_point(curve.hpoint)
        # self.graphicsView.add_point(curve.tpoint)
        # self.graphicsView.add_line(curve.fpoint, curve.hpoint, 1)
        # self.graphicsView.add_line(curve.tpoint, curve.hpoint, 1)
