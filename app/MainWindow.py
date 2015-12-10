# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/templates/main_form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 800)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 12, 4, 1, 1)
        self.draw_btn = QtWidgets.QPushButton(Form)
        self.draw_btn.setObjectName("draw_btn")
        self.gridLayout_2.addWidget(self.draw_btn, 13, 4, 1, 1)
        self.hor_rad_ledit = QtWidgets.QLineEdit(Form)
        self.hor_rad_ledit.setObjectName("hor_rad_ledit")
        self.gridLayout_2.addWidget(self.hor_rad_ledit, 5, 3, 1, 2)
        self.ver_rad_ledit = QtWidgets.QLineEdit(Form)
        self.ver_rad_ledit.setObjectName("ver_rad_ledit")
        self.gridLayout_2.addWidget(self.ver_rad_ledit, 3, 3, 1, 2)
        self.ver_rad_lbl = QtWidgets.QLabel(Form)
        self.ver_rad_lbl.setObjectName("ver_rad_lbl")
        self.gridLayout_2.addWidget(self.ver_rad_lbl, 2, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 13, 3, 1, 1)
        self.big_rad_lbl = QtWidgets.QLabel(Form)
        self.big_rad_lbl.setObjectName("big_rad_lbl")
        self.gridLayout_2.addWidget(self.big_rad_lbl, 8, 3, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("figure.jpg"))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 10, 3, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 12, 1, 2, 1)
        self.diag_size_lbl = QtWidgets.QLabel(Form)
        self.diag_size_lbl.setObjectName("diag_size_lbl")
        self.gridLayout_2.addWidget(self.diag_size_lbl, 0, 3, 1, 2)
        self.big_rad_ledit = QtWidgets.QLineEdit(Form)
        self.big_rad_ledit.setObjectName("big_rad_ledit")
        self.gridLayout_2.addWidget(self.big_rad_ledit, 9, 3, 1, 2)
        self.diag_size_ledit = QtWidgets.QLineEdit(Form)
        self.diag_size_ledit.setObjectName("diag_size_ledit")
        self.gridLayout_2.addWidget(self.diag_size_ledit, 1, 3, 1, 2)
        self.lit_rad_ledit = QtWidgets.QLineEdit(Form)
        self.lit_rad_ledit.setObjectName("lit_rad_ledit")
        self.gridLayout_2.addWidget(self.lit_rad_ledit, 7, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 12, 0, 2, 1)
        self.hor_rad_lbl = QtWidgets.QLabel(Form)
        self.hor_rad_lbl.setObjectName("hor_rad_lbl")
        self.gridLayout_2.addWidget(self.hor_rad_lbl, 4, 3, 1, 2)
        self.lit_rad_lbl = QtWidgets.QLabel(Form)
        self.lit_rad_lbl.setObjectName("lit_rad_lbl")
        self.gridLayout_2.addWidget(self.lit_rad_lbl, 6, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 12, 2, 2, 1)
        self.graphicsView = MyGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 12, 3)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.draw_btn.clicked.connect(self._draw_figure)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.draw_btn.setText(_translate("Form", "Draw"))
        self.ver_rad_lbl.setText(_translate("Form", "Введите радиус r2"))
        self.big_rad_lbl.setText(_translate("Form", "Введите радиус R"))
        self.diag_size_lbl.setText(_translate("Form", "Введите размер диагонали D"))
        self.hor_rad_lbl.setText(_translate("Form", "Введите радиус r1"))
        self.lit_rad_lbl.setText(_translate("Form", "Введите радиус r"))

    def _draw_figure(self):
        try:
            R = int(self.big_rad_ledit.text() or '20')
            r = int(self.lit_rad_ledit.text() or '10')
            r1 = int(self.ver_rad_ledit.text() or '20')
            r2 = int(self.hor_rad_ledit.text() or '20')
            D = int(self.diag_size_ledit.text() or '100')
            self.graphicsView.draw_frame(D, r1, r2, r, R)
        except Exception as e:
            print(e)

    def _draw_grid(self):
        pass

from .mygraphicsview import MyGraphicsView
