import notewidgetui
from PyQt5.QtWidgets import *


class NoteWidget(QWidget, notewidgetui.Ui_NoteWidget):
    def __init__(self, note, color='#ffffcc', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.note = note
        self.color = color

        self.headingEdit.setText(self.note.heading)
        self.bodyEdit.setPlainText(self.note.body)

        self.closeButton.clicked.connect(self.delete)
        self.headingEdit.textChanged.connect(lambda: self.note.update_heading(self.headingEdit.text()))
        self.bodyEdit.textChanged.connect(lambda: self.note.update_body(self.bodyEdit.toPlainText()))
        self.moveUpButton.clicked.connect(self.move_up)
        self.moveDownButton.clicked.connect(self.move_down)
        self.moveLeftButton.clicked.connect(self.move_left)
        self.moveRightButton.clicked.connect(self.move_right)

    def delete(self):
        self.note.delete()
        self.setParent(None)

    def move_up(self):
        self.parent().move_note_up(self)

    def move_down(self):
        self.parent().move_note_down(self)

    def move_left(self):
        self.parent().move_note_left(self)

    def move_right(self):
        self.parent().move_note_right(self)


'''
    def color_background(self):
        color_window_background(self, self.color)
        for widget in (self.heading_layout, self.body_layout):
            color_widget_background(widget, self.color)
'''
