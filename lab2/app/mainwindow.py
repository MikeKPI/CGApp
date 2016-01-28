import sys
import os
import math

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__name__))+'/app')

from PyQt5 import QtCore, QtWidgets, QtGui

from app.main_window_ui import Ui_Form
from app.graphic_object import Cissoid
from app.transformations import rotate, move


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)

        self.setupUi(self)

        self.connect_buttons()

        self.show()
        self.draw()

    def draw(self):
        self.graphicsView.clear_scene()
        self.__draw_axis()
        self.graphicsView.draw_figure(Cissoid())

    def connect_buttons(self):
        self.build_pb.clicked.connect(self.build_action)
        self.rotate_pb.clicked.connect(self.rotate_action)
        self.move_pb.clicked.connect(self.move_action)

    def build_action(self):
        fig = self.__create_gobject()
        modf = lambda x, y: (x, y)

        self.graphicsView.clear_scene()
        self.__draw_axis()
        self.graphicsView.draw_figure(fig, modf)

    def rotate_action(self):
        fig = self.__create_gobject()
        modf = self.__rotate_hndlr()

        self.graphicsView.clear_scene()
        self.__draw_axis()
        self.graphicsView.draw_figure(fig, modf)

    def move_action(self):
        fig = self.__create_gobject()
        modf = self.__move_hndlr()

        self.graphicsView.clear_scene()
        self.__draw_axis()
        self.graphicsView.draw_figure(fig, modf)

    def __create_gobject(self):
        self.a = int(self.a_ledit.text() or '30')
        self.fx = int(self.from_x_ledit.text() or '-200')
        self.tx = int(self.to_x_ledit.text() or '200')
        self.num_i = int(self.num_ledit.text() or '100')

        return Cissoid(self.fx, self.tx, self.a, self.num_i)

    def __rotate_hndlr(self):
        self.angle = float(self.rotate_angle_ledit.text() or '0')
        self.rpx = float(self.rotate_x_ledit.text() or '0')
        self.rpy = float(self.rotate_y_ledit.text() or '0')

        return lambda x, y: rotate(self.angle, x, y, self.rpx, self.rpy)

    def __move_hndlr(self):
        self.dx = float(self.move_x_ledit.text() or '0')
        self.dy = float(self.move_y_ledit.text() or '0')

        return lambda x, y: move(x, y, self.dx, self.dy)

    def __draw_axis(self):
        self.__create_gobject()
        self.graphicsView.draw_axis(self.fx, self.tx, self.a)
