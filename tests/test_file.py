from unittest import mock
import unittest
from unittest.mock import patch, mock_open

from file.file import File


class TestFile(unittest.TestCase):
    def test_read(self):
        content_mock = 'Hello World!'
        file_path = '/fake/file/path.txt'
        with patch('file.file.open'.format(__name__),
                   new=mock_open(read_data=content_mock)) as _file:
            actual = File().read(file_path)
            _file.assert_called_once_with(file_path, 'r')
            self.assertEqual(content_mock + '\n', actual)

    def test_write(self):
        fake_file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('file.file.open', mock_open()) as f:
            File().write(fake_file_path, content)
            # assert if opened file on write mode 'w'
            f.assert_called_once_with(fake_file_path, 'w')

            # assert if the specific content was written in file
            f().write.assert_called_once_with(content)

    @mock.patch('file.file.os.path')
    @mock.patch('file.file.os')
    def test_delete_not_existing_file(self, mock_os, mock_path):
        mock_path.exists.return_value = False

        File().delete("path")

        self.assertFalse(mock_os.remove.called,
                         "Failed to not remove the file if not present.")

    @mock.patch('file.file.os.path')
    @mock.patch('file.file.os')
    def test_delete_existing_file(self, mock_os, mock_path):
        mock_path.exists.return_value = True

        File().delete("path")

        mock_os.remove.assert_called_with("path")

