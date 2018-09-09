# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'columnwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ColumnWidget(object):
    def setupUi(self, ColumnWidget):
        ColumnWidget.setObjectName("ColumnWidget")
        ColumnWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ColumnWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.containerLayout = QtWidgets.QVBoxLayout()
        self.containerLayout.setObjectName("containerLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameEdit = QtWidgets.QLineEdit(ColumnWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.deleteButton = QtWidgets.QPushButton(ColumnWidget)
        self.deleteButton.setMinimumSize(QtCore.QSize(20, 20))
        self.deleteButton.setMaximumSize(QtCore.QSize(20, 20))
        self.deleteButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.containerLayout.addLayout(self.horizontalLayout)
        self.moveButtonsLayout = QtWidgets.QHBoxLayout()
        self.moveButtonsLayout.setObjectName("moveButtonsLayout")
        self.moveLeftButton = QtWidgets.QPushButton(ColumnWidget)
        self.moveLeftButton.setObjectName("moveLeftButton")
        self.moveButtonsLayout.addWidget(self.moveLeftButton)
        self.moveRightButton = QtWidgets.QPushButton(ColumnWidget)
        self.moveRightButton.setObjectName("moveRightButton")
        self.moveButtonsLayout.addWidget(self.moveRightButton)
        self.containerLayout.addLayout(self.moveButtonsLayout)
        self.newNoteButton = QtWidgets.QPushButton(ColumnWidget)
        self.newNoteButton.setObjectName("newNoteButton")
        self.containerLayout.addWidget(self.newNoteButton)
        self.notesLayout = QtWidgets.QVBoxLayout()
        self.notesLayout.setSpacing(10)
        self.notesLayout.setObjectName("notesLayout")
        self.containerLayout.addLayout(self.notesLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.containerLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.containerLayout)

        self.retranslateUi(ColumnWidget)
        QtCore.QMetaObject.connectSlotsByName(ColumnWidget)

    def retranslateUi(self, ColumnWidget):
        _translate = QtCore.QCoreApplication.translate
        ColumnWidget.setWindowTitle(_translate("ColumnWidget", "Form"))
        self.deleteButton.setText(_translate("ColumnWidget", "X"))
        self.moveLeftButton.setText(_translate("ColumnWidget", "←"))
        self.moveRightButton.setText(_translate("ColumnWidget", "→"))
        self.newNoteButton.setText(_translate("ColumnWidget", "New Note"))

