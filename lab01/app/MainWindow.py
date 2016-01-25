import sys
import os
import math

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__name__))+'/app')

from app.main_window_ui import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)

        self.setupUi(self)
        self.set_pixmap()
        self.connect_buttons()
        self.show()

    def connect_buttons(self):
        self.draw_lab0_btn.clicked.connect(self._draw_frame)
        self.transform_lab1_afin_btn.clicked.connect(self.affine_morf_action)
        self.move_evk_btn.clicked.connect(self.move_action)
        self.rotate_evk_btn.clicked.connect(self.rotate_action)
        self.draw_lab1_afin_btn.clicked.connect(self._draw_frame)
        self.draw_lab1_transform_btn.clicked.connect(self._draw_frame)
        self.transform_lab1_transform_btn.clicked.connect(self.transform_action)

    def set_pixmap(self):
        self.label.setPixmap(QtGui.QPixmap("figure.jpg"))

    def _draw_frame(self):
        self.graphicsView.clear_scene()
        self._draw_grid()
        self._draw_figure()

    def _draw_figure(self, modifier=lambda x, y: (x, y)):
        try:
            R = int(self.big_rad_ledit.text() or '20')
            r = int(self.lit_rad_ledit.text() or '10')
            r1 = int(self.ver_rad_ledit.text() or '20')
            r2 = int(self.hor_rad_ledit.text() or '20')
            D = int(self.diag_size_ledit.text() or '100')
            self.graphicsView.draw_figure(D, r1, r2, r, R, modifier=modifier)
        except Exception as e:
            raise

    def _draw_grid(self, modifier=lambda x, y: (x, y)):
        try:
            H = int(self.diag_size_ledit.text() or '100') * 1.2
            self.graphicsView.draw_grid(int(H), modifier=modifier)
        except Exception as e:
            raise

    def affine_morf_action(self):
        try:
            affine_matrix = np.matrix([
                [float(self.rx_0_afin_ledit.text() or '1'),
                 float(self.rx_1_afin_ledit.text() or '0'),
                 0],
                [float(self.ry_0_afin_ledit.text() or '0'),
                 float(self.ry_1_afin_ledit.text() or '1'),
                 0],
                [float(self.r0_0_afin_ledit.text() or '0'),
                float(self.r0_1_afin_ledit.text() or '0'),
                1]
            ])
            self.graphicsView.clear_scene()
            self._draw_grid(modifier=lambda x, y: ((np.matrix([x, y, 1]) * affine_matrix).tolist())[0][:2])
            self._draw_figure(modifier=lambda x, y: ((np.matrix([x, y, 1]) * affine_matrix).tolist())[0][:2])
        except Exception:
            raise


    def move_action(self):
        try:
            move_matrix = np.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [float(self.mv_axis_x_evk_ledit.text() or '0'),
                 float(self.mv_axis_y_evk_ledit.text() or '0'),
                 0]
            ])
            self.graphicsView.clear_scene()
            self._draw_grid()
            self._draw_figure(modifier=lambda x, y: (np.matrix([x, y, 1]) * move_matrix).tolist()[0][:2])
        except Exception:
            raise

    def rotate_action(self):
        try:
            x = float(self.rt_x_center_evk_ledit.text() or '0')
            y = float(self.rt_y_center_evk_ledit.text() or '0')
            angle = math.radians(float(self.rt_angle_evk_ledit.text() or '0'))

            reverse_m = np.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [-x, -y, 1]
            ])
            move_m = np.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [x, y, 1]
            ])
            rotate_m = np.matrix([
                [math.cos(angle), math.sin(angle), 0],
                [-math.sin(angle), math.cos(angle), 0],
                [0, 0, 1]
            ])

            self.graphicsView.clear_scene()
            self._draw_grid()
            self._draw_figure(modifier=lambda x, y: (np.matrix([x, y, 1]) * reverse_m * rotate_m * move_m).tolist()[0][:2])
        except Exception:
            raise

    def transform_action(self):
        try:
            # transform_m = np.matrix([
            #     [float(self.vec_x_0_ledit.text() or '1'),
            #      float(self.vec_x_1_ledit.text() or '0'),
            #      float(self.vec_x_2_ledit.text() or '0')],
            #     [float(self.vec_y_0_ledit.text() or '0'),
            #      float(self.vec_y_1_ledit.text() or '1'),
            #      float(self.vec_y_2_ledit.text() or '0')],
            #     [float(self.vec_r0_0_ledit.text() or '0'),
            #      float(self.vec_r0_1_ledit.text() or '0'),
            #      float(self.vec_r0_2_ledit.text() or '1')]
            # ])
            Xx = float(self.vec_x_0_ledit.text() or '1')
            Yx = float(self.vec_x_1_ledit.text() or '0')
            Wx = float(self.vec_x_2_ledit.text() or '0')
            Xy = float(self.vec_y_0_ledit.text() or '0')
            Yy = float(self.vec_y_1_ledit.text() or '1')
            Wy = float(self.vec_y_2_ledit.text() or '0')
            Rx = float(self.vec_r0_0_ledit.text() or '0')
            Ry = float(self.vec_r0_1_ledit.text() or '0')
            Wr = float(self.vec_r0_2_ledit.text() or '1')

            self.graphicsView.clear_scene()
            # modf =modifier=lambda x, y: (np.matrix([x, y, 1]) * transform_m).tolist()[0][:2]
            def modf(x, y):
                r0 = np.matrix([Rx, Ry])
                rx = np.matrix([Xx, Xy])
                ry = np.matrix([Yx, Yy])
                rez = (r0 * Wr + rx * Wx * x + ry * Wy * y) / (Wr + Wx * x + Wy * y)
                return rez.tolist()[0]
            self._draw_grid(modifier=modf)
            self._draw_figure(modifier=modf)
        except Exception as e:
            raise
