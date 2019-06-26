import boardwidgetui
from columnwidget import ColumnWidget
import ahfklib as lib
from PyQt5.QtWidgets import *


class BoardWidget(QWidget, boardwidgetui.Ui_BoardWidget):
    board = ...  # type: lib.Board

    def __init__(self, board: lib.Board, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.board = board

        for column in self.board.sorted_columns:
            self.add_existing_column(column)

        self.newColumnButton.clicked.connect(self.add_new_column)

    def add_existing_column(self, column: lib.Column):
        self.columnsLayout.addWidget(ColumnWidget(column))

    def add_new_column(self):
        column_name = ''
        self.add_existing_column(lib.new_column(column_name, self.board))

    def move_column_to_index_(self, column_widget, index):
        self.columnsLayout.removeWidget(column_widget)
        self.columnsLayout.insertWidget(index, column_widget)

    def move_column_left(self, column_widget):
        self.board.move_column_left(column_widget.column)
        new_index = max(0, self.columnsLayout.indexOf(column_widget) - 1)
        self.move_column_to_index_(column_widget, new_index)

    def move_column_right(self, column_widget):
        self.board.move_column_right(column_widget.column)
        new_index = min(self.columnsLayout.count() - 1, self.columnsLayout.indexOf(column_widget) + 1)
        self.move_column_to_index_(column_widget, new_index)

    def move_note_to_column_index(self, old_column_widget, new_column_index, note_widget):
        old_column_widget.remove_note_widget(note_widget)
        new_column_widget = self.columnsLayout.itemAt(new_column_index).widget()
        new_column_widget.add_existing_note(note_widget.note)

    def move_note_left(self, old_column_widget, note_widget):
        old_column_index = self.columnsLayout.indexOf(old_column_widget)
        new_column_index = max(0, old_column_index - 1)
        if old_column_index != new_column_index:
            self.move_note_to_column_index(old_column_widget, new_column_index, note_widget)

    def move_note_right(self, old_column_widget, note_widget):
        old_column_index = self.columnsLayout.indexOf(old_column_widget)
        new_column_index = min(self.columnsLayout.count() - 1, self.columnsLayout.indexOf(old_column_widget) + 1)
        if old_column_index != new_column_index:
            self.move_note_to_column_index(old_column_widget, new_column_index, note_widget)
