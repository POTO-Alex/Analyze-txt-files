from read_and_process_file import get_words_from_file
import settings
if settings.settings['mode'] == 'brute_force':
    from brute_force_hash_table import HashWord
elif settings.settings['mode'] == 'trie':
    from trie_hash_table import HashWord
else:
    exit(0)

# Time & Space complexity of this function depends on
# trie_hash_table data structure.
def count_all_words():
    # get all words in a txt file.
    words = get_words_from_file()
    # iterate all words and insert to the hash table
    hash_word = HashWord()
    for word in words:
        hash_word.insert(word)
    # print the result
    number_of_words = hash_word.get_number_of_words()
    with open(settings.settings['save_path'], 'w') as file:
        for i in range(number_of_words):
            word = hash_word.get_ith_word(i)
            count = hash_word.get_ith_count(i)
            if count == 1:
                file.write(f'{word} appears once in the text file.\n')
            else:
                file.write(f'{word} appears {count} times in the text file.\n')
        file.write('\n')
        file.write(f'{hash_word.get_word_with_highest_count()} is the word with the highest count.\n')


if __name__ == "__main__":
    count_all_words()
