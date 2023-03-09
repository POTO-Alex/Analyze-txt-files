####################################################################
#                                                                  #
#  When we append words to this data structure,                    #
#  it keeps all distinct words with frequencies.                   #
#  Define m as the sum of lengths of words in the data structure.  #
#  Define n as the number of appending words.                      #
#  Time complexity for insert one word is O(m).                    #
#  So, the total time complexity is O(n * m).                      #
#  The space complexity is O(m).                                   #
#                                                                  #
####################################################################

from basic_structure import BasicStructure

class HashWord(BasicStructure):

    def __init__(self):
        super().__init__()

    # insert word to hash table
    # increase the frequency by 1
    # Time: O(sum of lengths of the existing words)
    def insert(self, word):
        if word not in self.words:
            self.words.append(word)
            self.counts.append(0)
        index = self.words.index(word)
        self.counts[index] += 1
