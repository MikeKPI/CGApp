# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/templates/lab3_form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 621, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_pb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_pb.setObjectName("open_pb")
        self.horizontalLayout_2.addWidget(self.open_pb)
        self.save_pb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_pb.setObjectName("save_pb")
        self.horizontalLayout_2.addWidget(self.save_pb)
        self.add_pb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_pb.setObjectName("add_pb")
        self.horizontalLayout_2.addWidget(self.add_pb)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.graphicsView = MyGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_pb.setText(_translate("Form", "Open"))
        self.save_pb.setText(_translate("Form", "Save"))
        self.add_pb.setText(_translate("Form", "Add"))

from mygraphicsview import MyGraphicsView
