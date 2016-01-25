import sys
import os

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

    def set_pixmap(self):
        self.label.setPixmap(QtGui.QPixmap("figure.jpg"))

    def _draw_frame(self):
        self._draw_grid()
        self._draw_figure()

    def _draw_figure(self):
        try:
            R = int(self.big_rad_ledit.text() or '20')
            r = int(self.lit_rad_ledit.text() or '10')
            r1 = int(self.ver_rad_ledit.text() or '20')
            r2 = int(self.hor_rad_ledit.text() or '20')
            D = int(self.diag_size_ledit.text() or '100')
            self.graphicsView.draw_figure(D, r1, r2, r, R)
        except Exception as e:
            self.label_7.setText(self._translate("Form", str(e)))

    def _draw_grid(self):
        try:
            H = int(self.diag_size_ledit.text() or '100') * 1.2
            self.graphicsView.draw_grid(int(H))
        except Exception as e:
            self.label_7.setText(self._translate("Form", str(e)))
