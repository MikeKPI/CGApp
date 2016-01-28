import sys
import os
import math

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__name__))+'/app')

from PyQt5 import QtCore, QtWidgets, QtGui

from app.lab6_mainwindow_ui import Ui_Form
from app.figure import figure, Point


class L6MainWindow(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)

        self.setupUi(self)

        self.set_default_matrixes()
        self.set_default_values()
        self.refresh_all()
        self._connect_all()

        self.show()

    def _set_casting_matrixes(self):
        self.xy_matrix = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ])
        self.xz_matrix = np.matrix([
            [1, 0, 0, 0],
            [0, 0, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.yz_matrix = np.matrix([
            [0, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def _set_rotation_matrixs(self):
        self.x_rot_m = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.y_rot_m = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.z_rot_m = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def _set_move_matrix(self):
        self.move_m = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0 ,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def set_default_matrixes(self):
        self._set_move_matrix()
        self._set_casting_matrixes()
        self._set_rotation_matrixs()

    def draw(self, mtr, view, i1, i2):
        for line in figure.lines:
            points = [(point * self.x_rot_m * self.y_rot_m * self.z_rot_m * self.move_m * mtr).tolist()[0]
                for point in map(Point.to_vector, line)]
            view.add_line(
                [points[0][i1], points[0][i2]],
                [points[1][i1], points[1][i2]]
            )

    def refresh_all(self):
        self.graphicsView.clear_scene()
        self.draw(self.xz_matrix, self.graphicsView, 0, 2)

    def on_rotate_click(self):
        rx_mtr = self.x_rot_m.tolist()
        ry_mtr = self.y_rot_m.tolist()
        rz_mtr = self.z_rot_m.tolist()

        try:
            self.xr += math.radians(float(self.x_angle_ledit.text()))
            rx_mtr[1][1] = math.cos(self.xr)
            rx_mtr[2][1] = math.sin(self.xr)
            rx_mtr[1][2] = -math.sin(self.xr)
            rx_mtr[2][2] = math.cos(self.xr)

            self.x_rot_m = np.matrix(rx_mtr)
        except Exception:
            raise

        try:
            self.yr += math.radians(float(self.y_angle_ledit.text()))
            ry_mtr[0][0] = math.cos(self.yr)
            ry_mtr[2][0] = math.sin(self.yr)
            ry_mtr[0][2] = -math.sin(self.yr)
            ry_mtr[2][2] = math.cos(self.yr)

            self.y_rot_m = np.matrix(ry_mtr)
        except Exception:
            raise

        try:
            self.zr += math.radians(float(self.z_angle_ledit.text()))
            rz_mtr[0][0] = math.cos(self.zr)
            rz_mtr[1][0] = math.sin(self.zr)
            rz_mtr[0][1] = -math.sin(self.zr)
            rz_mtr[1][1] = math.cos(self.zr)

            self.z_rot_m = np.matrix(rz_mtr)
        except Exception:
            raise

        self.refresh_all()

    def set_default_values(self):
        self.xr = self.yr = self.zr = 0

    def _connect_all(self):
        self.rotate_pb.clicked.connect(self.on_rotate_click)
