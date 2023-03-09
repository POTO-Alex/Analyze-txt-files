####################################################################
#                                                                  #
#  When we append words to this data structure,                    #
#  it keeps all distinct words with frequencies.                   #
#  Define m as the sum of lengths of words in the data structure.  #
#  Define n as the number of appending words.                      #
#  Time complexity for insert one word is O(length of new word).   #
#  So, the total time complexity is O(m).                          #
#  The space complexity is O(m).                                   #
#                                                                  #
####################################################################

from basic_structure import BasicStructure

# use trie data structure to hash words
class HashWord(BasicStructure):
    # Time: O(1)
    def __init__(self):
        super().__init__()
        # number of nodes in trie
        self.number_of_nodes = 0
        # children of node
        self.children = []
        # sign for determining the end points
        # end[i] > -1 means there is 'self.words[end[i]]'
        self.end = []
        # declare root of trie
        self.root = self.new_node()

    # add new node to trie
    # Time: O(1)
    def new_node(self):
        self.children.append({})
        self.end.append(-1)
        self.number_of_nodes += 1
        return self.number_of_nodes - 1

    # insert word to hash table
    # increase the frequency by 1
    # Time: O(length of word)
    def insert(self, word):
        cur = self.root
        for c in word:
            # if there is no child for letter(c),
            # insert new node as a child
            if c not in self.children[cur].keys():
                self.children[cur][c] = self.new_node()
            # traverse
            cur = self.children[cur][c]
        # if this word doesn't exist,
        # add new word and count
        if self.end[cur] == -1:
            self.end[cur] = self.get_number_of_words()
            self.words.append(word)
            self.counts.append(1)
        # else, just increase the count
        else:
            self.counts[self.end[cur]] += 1
