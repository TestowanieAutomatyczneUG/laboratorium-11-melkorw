import unittest
from unittest.mock import MagicMock
from src.note.note import Note


class TestNote(unittest.TestCase):
    def test_note_type_error1(self):
        note_class = MagicMock(side_effect=TypeError)
        name = 123
        note = 4.0
        self.assertRaises(TypeError, note_class, name, note)

    def test_note_type_error2(self):
        note_class = MagicMock(side_effect=TypeError)
        name = None
        note = 4.0
        self.assertRaises(TypeError, note_class, name, note)

    def test_note_type_error3(self):
        note_class = MagicMock(side_effect=TypeError)
        name = 'Name'
        note = 'note'
        self.assertRaises(TypeError, note_class, name, note)

    def test_note_value_error1(self):
        note_class = MagicMock(side_effect=ValueError)
        name = ''
        note = 3
        self.assertRaises(ValueError, note_class, name, note)

    def test_note_value_error2(self):
        note_class = MagicMock(side_effect=ValueError)
        name = 'Abc'
        note = 0.3
        self.assertRaises(ValueError, note_class, name, note)

    def test_note_get_name(self):
        name = 'Abc'
        note = 3.5
        test_object = Note(name, note)
        test_object.get_name = MagicMock(return_value=name)
        self.assertEqual(test_object.get_name(), name)

    def test_note_get_note(self):
        name = 'Abc'
        note = 3.5
        test_object = Note(name, note)
        test_object.get_note = MagicMock(return_value=note)
        self.assertEqual(test_object.get_note(), note)
