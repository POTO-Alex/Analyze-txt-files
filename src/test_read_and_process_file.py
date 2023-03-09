import unittest
from unittest.mock import patch

from read_and_process_file import get_words_from_line
import read_and_process_file


class GetWordsFromLineTestCase(unittest.TestCase):

    def test_empty_line(self):
        self.assertEqual(get_words_from_line(''), [])

    def test_one_punctuation(self):
        self.assertEqual(get_words_from_line('\n'), [])
        self.assertEqual(get_words_from_line('\t'), [])
        self.assertEqual(get_words_from_line('?'), [])
        self.assertEqual(get_words_from_line('.'), [])
        self.assertEqual(get_words_from_line(','), [])
        self.assertEqual(get_words_from_line('-'), [])
        self.assertEqual(get_words_from_line(';'), [])
        self.assertEqual(get_words_from_line('"'), [])
        self.assertEqual(get_words_from_line('\''), [])

    def test_only_punctuations(self):
        self.assertEqual(get_words_from_line(' \t?? . \''), [])

    def test_one_word(self):
        self.assertEqual(get_words_from_line('apple'), ['apple'])

    def test_two_words(self):
        self.assertEqual(get_words_from_line('apple banana'), ['apple', 'banana'])
        self.assertEqual(get_words_from_line('apple,banana'), ['apple', 'banana'])
        self.assertEqual(get_words_from_line('apple. ??:banana'), ['apple', 'banana'])

    def test_several_words(self):
        self.assertEqual(get_words_from_line('apple, banana. pe:ar ... yellow??'), ['apple', 'banana', 'pe', 'ar', 'yellow'])


class GetWordsFromFileTestCase(unittest.TestCase):

    def test(self):
        with patch('read_and_process_file.readlines_from_txt_file') as mock_readlines_from_txt_file, \
             patch('read_and_process_file.get_words_from_line') as mock_get_words_from_line:
            file_path = 'abc'
            word = 'xyz'
            mock_readlines_from_txt_file.return_value = [word]
            read_and_process_file.get_words_from_file(file_path)
            read_and_process_file.readlines_from_txt_file.assert_called_once()
            read_and_process_file.get_words_from_line.assert_called_once()
            self.assertEqual(read_and_process_file.readlines_from_txt_file.call_args[0][0], file_path)
            self.assertEqual(read_and_process_file.get_words_from_line.call_args[0][0], word)


if __name__ == '__main__':
    unittest.main()
