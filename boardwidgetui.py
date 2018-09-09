# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boardwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BoardWidget(object):
    def setupUi(self, BoardWidget):
        BoardWidget.setObjectName("BoardWidget")
        BoardWidget.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(BoardWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.containerLayout = QtWidgets.QHBoxLayout()
        self.containerLayout.setSpacing(10)
        self.containerLayout.setObjectName("containerLayout")
        self.newColumnButton = QtWidgets.QPushButton(BoardWidget)
        self.newColumnButton.setObjectName("newColumnButton")
        self.containerLayout.addWidget(self.newColumnButton)
        self.columnsLayout = QtWidgets.QHBoxLayout()
        self.columnsLayout.setSpacing(10)
        self.columnsLayout.setObjectName("columnsLayout")
        self.containerLayout.addLayout(self.columnsLayout)
        self.horizontalLayout_2.addLayout(self.containerLayout)

        self.retranslateUi(BoardWidget)
        QtCore.QMetaObject.connectSlotsByName(BoardWidget)

    def retranslateUi(self, BoardWidget):
        _translate = QtCore.QCoreApplication.translate
        BoardWidget.setWindowTitle(_translate("BoardWidget", "Form"))
        self.newColumnButton.setText(_translate("BoardWidget", "New Column"))

