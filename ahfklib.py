import json
import pathlib
import uuid
from collections import OrderedDict
from sqlalchemy import Column as SQLColumn, String, Integer, ForeignKey, Table
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


ahfk = None  # reference to the ahfk table row, of which there must be exactly one
AHFK_VERSION = '0.1'  # will be arbitrary before 1.0
AHFK_HOME = pathlib.Path.home().joinpath('.ahfk')
AHFK_HOME.mkdir(exist_ok=True)

Base_ = declarative_base()
engine_ = create_engine('sqlite:///{}/default.db'.format(AHFK_HOME))
db_session_ = scoped_session(sessionmaker(bind=engine_))
Base_.query = db_session_.query_property()


def list_coalesce(seq_or_none):
    return [] if seq_or_none is None else seq_or_none


# TODO: Consider moving the following table declarations to a models.py module
notes_to_tags = Table('notes_to_tags', Base_.metadata,
                      SQLColumn('notes_id', Integer, ForeignKey('notes.id')),
                      SQLColumn('tags_id', Integer, ForeignKey('tags.id')))


class Note(Base_):
    __tablename__ = 'notes'

    id = SQLColumn(Integer, primary_key=True)
    heading = SQLColumn(String, default='')
    body = SQLColumn(String, default='')
    sort_order = SQLColumn(Integer)  # key for sorting notes within their column
    column_id = SQLColumn(Integer, ForeignKey('columns.id'))
    column = relationship('Column', back_populates='notes')
    tags = relationship('Tag',
                        secondary=notes_to_tags,
                        back_populates='notes')

    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Note):
                return {'ahfknote': OrderedDict((('tags', o.tags),
                                                 ('title', o.heading),
                                                 ('body', o.body)))}
            return json.JSONEncoder.default(self, o)

    @staticmethod
    def to_json(o):
        """Dump to JSON an object that may contain Note instances."""
        return json.dumps(o, cls=Note.JSONEncoder, indent=4)

    @property
    def json(self):
        return Note.to_json(self)

    def update_heading(self, new_text):
        self.heading = new_text
        db_session_.add(self)
        db_session_.commit()

    def update_body(self, new_text):
        self.body = new_text
        db_session_.add(self)
        db_session_.commit()

    def update_column(self, new_column):
        if self.column == new_column:
            return
        self.column = new_column
        if self.column is not None:
            self.sort_order = None
            self.sort_order = self.column.next_sort_order()
        db_session_.add(self)
        db_session_.commit()

    def delete(self):
        db_session_.delete(self)
        db_session_.commit()

    def __str__(self):
        return self.json

    def title_contains_all(self, title_substrings):
        return all(substring in self.heading for substring in title_substrings)

    def body_contains_all(self, body_substrings):
        return all(substring in self.body for substring in body_substrings)

    def tags_contains_all(self, tag_substrings):
        return all(any(substring in tag.name for tag in self.tags) for substring in tag_substrings)


class Tag(Base_):
    __tablename__ = 'tags'

    id = SQLColumn(Integer, primary_key=True)
    name = SQLColumn(String)
    notes = relationship('Note',
                         secondary=notes_to_tags,
                         back_populates='tags')


class Column(Base_):
    __tablename__ = 'columns'

    id = SQLColumn(Integer, primary_key=True)
    name = SQLColumn(String)
    sort_order = SQLColumn(Integer)
    board_id = SQLColumn(Integer, ForeignKey('boards.id'))
    board = relationship('Board', back_populates='columns')
    notes = relationship('Note', back_populates='column')

    @property
    def sorted_notes(self):
        return sorted(self.notes, key=lambda n: n.sort_order)

    def update_name(self, new_text):
        self.name = new_text
        db_session_.add(self)
        db_session_.commit()

    def delete(self):
        db_session_.delete(self)
        db_session_.commit()

    def next_sort_order(self):
        if self.notes is None or len(self.notes) == 0:
            max_sort_order = 0
        else:
            max_sort_order = max(note.sort_order for note in self.notes if note.sort_order is not None)
        return max_sort_order + 1

    def swap_notes(self, note_a, note_b):
        note_a.sort_order, note_b.sort_order = note_b.sort_order, note_a.sort_order
        db_session_.add_all((note_a, note_b))
        db_session_.commit()

    def move_note_up(self, note):
        if note not in self.notes:
            raise Exception('Note {} not in column {}'.format(note, self))
        already_at_top = self.sorted_notes[0].id == note.id
        if already_at_top:
            return
        other_note = self.sorted_notes[self.sorted_notes.index(note) - 1]
        self.swap_notes(note, other_note)

    def move_note_down(self, note):
        if note not in self.notes:
            raise Exception('Note {} not in column {}'.format(note, self))
        already_at_bottom = self.sorted_notes[-1].id == note.id
        if already_at_bottom:
            return
        other_note = self.sorted_notes[self.sorted_notes.index(note) + 1]
        self.swap_notes(note, other_note)


class Board(Base_):
    __tablename__ = 'boards'

    id = SQLColumn(Integer, primary_key=True)
    name = SQLColumn(String)
    columns = relationship('Column', back_populates='board')

    @property
    def sorted_columns(self):
        return sorted(self.columns, key=lambda c: c.sort_order)

    def swap_columns(self, column_a, column_b):
        column_a.sort_order, column_b.sort_order = column_b.sort_order, column_a.sort_order
        db_session_.add_all((column_a, column_b))
        db_session_.commit()

    def move_column_left(self, column):
        if column not in self.columns:
            raise Exception('column {} not in board {}'.format(column, self))
        already_at_start = self.sorted_columns[0].id == column.id
        if already_at_start:
            return
        other_column = self.sorted_columns[self.sorted_columns.index(column) - 1]
        self.swap_columns(column, other_column)

    def move_column_right(self, column):
        if column not in self.columns:
            raise Exception('column {} not in board {}'.format(column, self))
        already_at_end = self.sorted_columns[-1].id == column.id
        if already_at_end:
            return
        other_column = self.sorted_columns[self.sorted_columns.index(column) + 1]
        self.swap_columns(column, other_column)

    def next_sort_order(self):
        if self.columns is None or len(self.columns) == 0:
            max_sort_order = 0
        else:
            max_sort_order = max(column.sort_order for column in self.columns)
        return max_sort_order + 1


class AHFK(Base_):
    __tablename__ = 'ahfk'

    uuid = SQLColumn(String, primary_key=True)
    app_version = SQLColumn(String, default=AHFK_VERSION)
    last_board_id = SQLColumn(Integer, ForeignKey('boards.id'))
    last_board = relationship('Board')


def init():
    if AHFK.query.first() is None:
        db_session_.add(AHFK(uuid=str(uuid.uuid4())))
        db_session_.commit()
    global ahfk
    ahfk = AHFK.query.first()


def new_note(column):
    note = Note(column=column, sort_order=column.next_sort_order())
    db_session_.add(note)
    db_session_.commit()
    return note


def new_column(name, board):
    column = Column(name=name, board=board, sort_order=board.next_sort_order())
    column.notes = [Note(column=column, sort_order=column.next_sort_order())]
    db_session_.add_all((column, column.notes[0]))
    db_session_.commit()
    return column


def new_board(name, column_names=None):
    global ahfk
    board = Board(name=name)
    column_names = list_coalesce(column_names) or ['default column']
    columns = [Column(name=column_name, board=board, sort_order=board.next_sort_order()) for column_name in column_names]
    for column in columns:
        column.notes = [Note(column=column, sort_order=1)]
        db_session_.add(column.notes[0])
    board.columns = columns
    ahfk.last_board = board
    db_session_.add_all((ahfk, board, *columns))
    db_session_.commit()
    return board


Base_.metadata.create_all(engine_)
init()
