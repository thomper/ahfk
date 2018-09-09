# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notewidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoteWidget(object):
    def setupUi(self, NoteWidget):
        NoteWidget.setObjectName("NoteWidget")
        NoteWidget.resize(300, 300)
        NoteWidget.setMinimumSize(QtCore.QSize(300, 300))
        NoteWidget.setMaximumSize(QtCore.QSize(300, 300))
        NoteWidget.setBaseSize(QtCore.QSize(2, 0))
        NoteWidget.setAutoFillBackground(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NoteWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headingAndDeleteButtonLayout = QtWidgets.QHBoxLayout()
        self.headingAndDeleteButtonLayout.setObjectName("headingAndDeleteButtonLayout")
        self.headingEdit = QtWidgets.QLineEdit(NoteWidget)
        self.headingEdit.setObjectName("headingEdit")
        self.headingAndDeleteButtonLayout.addWidget(self.headingEdit)
        self.closeButton = QtWidgets.QPushButton(NoteWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(20, 20))
        self.closeButton.setMaximumSize(QtCore.QSize(20, 20))
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.headingAndDeleteButtonLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.headingAndDeleteButtonLayout)
        self.verticalMoveButtonsAndBodyLayout = QtWidgets.QHBoxLayout()
        self.verticalMoveButtonsAndBodyLayout.setObjectName("verticalMoveButtonsAndBodyLayout")
        self.verticalMoveButtonsLayout = QtWidgets.QVBoxLayout()
        self.verticalMoveButtonsLayout.setObjectName("verticalMoveButtonsLayout")
        self.moveUpButton = QtWidgets.QPushButton(NoteWidget)
        self.moveUpButton.setMinimumSize(QtCore.QSize(28, 100))
        self.moveUpButton.setMaximumSize(QtCore.QSize(28, 16777215))
        self.moveUpButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moveUpButton.setObjectName("moveUpButton")
        self.verticalMoveButtonsLayout.addWidget(self.moveUpButton)
        self.moveDownButton = QtWidgets.QPushButton(NoteWidget)
        self.moveDownButton.setMinimumSize(QtCore.QSize(28, 100))
        self.moveDownButton.setMaximumSize(QtCore.QSize(28, 16777215))
        self.moveDownButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moveDownButton.setObjectName("moveDownButton")
        self.verticalMoveButtonsLayout.addWidget(self.moveDownButton)
        self.verticalMoveButtonsAndBodyLayout.addLayout(self.verticalMoveButtonsLayout)
        self.bodyEdit = QtWidgets.QPlainTextEdit(NoteWidget)
        self.bodyEdit.setObjectName("bodyEdit")
        self.verticalMoveButtonsAndBodyLayout.addWidget(self.bodyEdit)
        self.verticalLayout.addLayout(self.verticalMoveButtonsAndBodyLayout)
        self.horizontalMoveButtonsLayout = QtWidgets.QHBoxLayout()
        self.horizontalMoveButtonsLayout.setObjectName("horizontalMoveButtonsLayout")
        self.moveLeftButton = QtWidgets.QPushButton(NoteWidget)
        self.moveLeftButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moveLeftButton.setObjectName("moveLeftButton")
        self.horizontalMoveButtonsLayout.addWidget(self.moveLeftButton)
        self.moveRightButton = QtWidgets.QPushButton(NoteWidget)
        self.moveRightButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moveRightButton.setObjectName("moveRightButton")
        self.horizontalMoveButtonsLayout.addWidget(self.moveRightButton)
        self.verticalLayout.addLayout(self.horizontalMoveButtonsLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(NoteWidget)
        QtCore.QMetaObject.connectSlotsByName(NoteWidget)
        NoteWidget.setTabOrder(self.headingEdit, self.closeButton)
        NoteWidget.setTabOrder(self.closeButton, self.bodyEdit)

    def retranslateUi(self, NoteWidget):
        _translate = QtCore.QCoreApplication.translate
        NoteWidget.setWindowTitle(_translate("NoteWidget", "Form"))
        self.closeButton.setText(_translate("NoteWidget", "X"))
        self.moveUpButton.setText(_translate("NoteWidget", "↑"))
        self.moveDownButton.setText(_translate("NoteWidget", "↓"))
        self.moveLeftButton.setText(_translate("NoteWidget", "←"))
        self.moveRightButton.setText(_translate("NoteWidget", "→"))

