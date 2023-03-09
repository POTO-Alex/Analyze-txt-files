import unittest
import brute_force_hash_table
import trie_hash_table


class BruteForseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_word = brute_force_hash_table.HashWord()

    def test_add_one_word(self):
        self.hash_word.__init__()
        self.hash_word.insert('apple')
        self.assertEqual(self.hash_word.words, ['apple'])

    def test_add_same_words_twice(self):
        self.hash_word.__init__()
        self.hash_word.insert('apple')
        self.hash_word.insert('apple')
        self.assertEqual(self.hash_word.words, ['apple'])

    def test_add_same_words_several_times(self):
        self.hash_word.__init__()
        self.hash_word.insert('apple')
        self.hash_word.insert('apple')
        self.hash_word.insert('apple')
        self.assertEqual(self.hash_word.words, ['apple'])

    def test_add_same_words(self):
        self.hash_word.__init__()
        self.hash_word.insert('apple')
        self.hash_word.insert('banana')
        self.hash_word.insert('apple')
        self.hash_word.insert('banana')
        self.assertEqual(self.hash_word.words, ['apple', 'banana'])

    def test_different_words(self):
        self.hash_word.__init__()
        self.hash_word.insert('apple')
        self.hash_word.insert('banana')
        self.hash_word.insert('tomato')
        self.assertEqual(self.hash_word.words, ['apple', 'banana', 'tomato'])


class TrieTestCase(BruteForseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.hash_word = trie_hash_table.HashWord()


if __name__ == '__main__':
    unittest.main()
