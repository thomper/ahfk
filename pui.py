import ahfklib as lib
from boardwidget import BoardWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


def color_window_background(window, color):
        window.setAutoFillBackground(True)
        palette = window.palette()
        palette.setColor(QPalette.Window, QColor(color))
        window.setPalette(palette)


def color_widget_background(widget, color):
        palette = widget.palette()
        palette.setColor(QPalette.Active, QPalette.Base, QColor(color))
        palette.setColor(QPalette.Inactive, QPalette.Base, QColor(color))
        widget.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, board=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if board is not None:
            self.board = board
        else:
            if lib.ahfk.last_board is not None:
                self.board = lib.ahfk.last_board
            else:
                self.board = lib.new_board('default board')

        self.setWindowTitle('ahfkanban')

        widget = BoardWidget(self.board)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
