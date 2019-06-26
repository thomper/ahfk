import columnwidgetui
from notewidget import NoteWidget
import ahfklib as lib
from PyQt5.QtWidgets import *


class ColumnWidget(QWidget, columnwidgetui.Ui_ColumnWidget):
    column = ...  # type: lib.Column

    def __init__(self, column: lib.Column, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.column = column

        self.nameEdit.setText(column.name)
        for note in self.column.sorted_notes:
            self.add_existing_note(note)

        self.nameEdit.textChanged.connect(lambda: self.column.update_name(self.nameEdit.text()))
        self.deleteButton.clicked.connect(self.delete)
        self.newNoteButton.clicked.connect(self.add_new_note)
        self.moveLeftButton.clicked.connect(self.move_left)
        self.moveRightButton.clicked.connect(self.move_right)

    def add_existing_note(self, note: lib.Note):
        self.notesLayout.addWidget(NoteWidget(note))
        if note.column != self.column:
            note.update_column(self.column)

    def add_new_note(self):
        self.add_existing_note(lib.new_note(self.column))

    def remove_note_widget(self, note_widget):
        self.notesLayout.removeWidget(note_widget)
        note_widget.hide()
        note_widget.note.update_column(None)

    def delete(self):
        for note in self.column.notes:
            note.delete()
        self.column.delete()
        self.setParent(None)

    def move_left(self):
        self.parent_board_widget.move_column_left(self)

    def move_right(self):
        self.parent_board_widget.move_column_right(self)

    def move_note_to_index_(self, note_widget, index):
        self.notesLayout.removeWidget(note_widget)
        self.notesLayout.insertWidget(index, note_widget)

    def move_note_up(self, note_widget):
        self.column.move_note_up(note_widget.note)
        new_index = max(0, self.notesLayout.indexOf(note_widget) - 1)
        self.move_note_to_index_(note_widget, new_index)

    def move_note_down(self, note_widget):
        self.column.move_note_down(note_widget.note)
        new_index = min(self.notesLayout.count() - 1, self.notesLayout.indexOf(note_widget) + 1)
        self.move_note_to_index_(note_widget, new_index)

    def move_note_left(self, note_widget):
        self.parent_board_widget.move_note_left(self, note_widget)

    def move_note_right(self, note_widget):
        self.parent_board_widget.move_note_right(self, note_widget)

    def __repr__(self):
        return '<ColumnWidget>'

    def __str__(self):
        return self.__repr__()

    @property
    def parent_board_widget(self):
        return self.parent().parent().parent().parent()
