# this is the basic structure of hash tables.
class BasicStructure:
    # Time: O(1)
    def __init__(self):
        # 'words' contains all distinct words.
        self.words = []
        # 'counts' contains frequencies of words.
        self.counts = []

    # return total number of different words
    # Time: O(1)
    def get_number_of_words(self):
        assert(len(self.words) == len(self.counts))
        return len(self.words)

    # return ith word in the hash table
    # Time: O(1)
    def get_ith_word(self, index):
        assert(index < len(self.words))
        return self.words[index]

    # return ith count in the hash table
    # Time: O(1)
    def get_ith_count(self, index):
        assert(index < len(self.counts))
        return self.counts[index]

    # return word with the highest frequency
    # Time: O(number of words)
    def get_word_with_highest_count(self):
        index = self.counts.index(max(self.counts))
        return self.words[index]
