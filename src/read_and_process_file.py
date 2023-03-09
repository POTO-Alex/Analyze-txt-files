import os
import re
import string
import settings


# This function is for reading a txt file from file_path.
# This returns a list of all lines in the file.
# Time: O(n), Space: O(n)
# Here, n is the size of a txt file.
def readlines_from_txt_file(file_path):
    if os.path.exists(file_path) == False:
        raise FileNotFoundError(f'FILE NOT FOUND IN INPUT FILE: {file_path}')
    # Open the txt file for reading. (read only)
    file = open(file_path, 'r')
    # return all lines in the file
    return file.readlines()

# We can use this function to get all words in each line.
# This function returns a list of words in a line.
# Time: O(n), Space: O(n)
# Here, n is the length of a line.
def get_words_from_line(line):
    # First, remove all remove_punctuations
    line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    # Then, replace all uppercase letters with lowercase ones.
    line = line.lower()
    # We can get all word by splitting the line by ' '.
    # Additionally, in the 'string.punctuation', there isn't '\n' and '\t'.
    list_of_words_in_line = re.split(' |\n|\t', line)
    # Remove all empty words.
    list_of_words_in_line = [line for line in list_of_words_in_line if len(line) > 0]

    return list_of_words_in_line

# We can use this function to get all words in a txt file.
# This returns a list of words - strings.
# Time: O(n), Space: O(n)
# Here, n is the size of a txt file.
def get_words_from_file(file_path = None):
    # If user doesn't define the file_path,
    # it will automatically load the txt file in data directory.
    if file_path is None:
        file_path = settings.settings['file_path']

    # Get all lines as a list.
    lines = readlines_from_txt_file(file_path)
    # Get all words in the lines.
    # Declare list_of_words as a empty list.
    list_of_words_in_file = []
    for line in lines:
        # 'get_words_from_line' returns a list of words in a line.
        # We can merge the list with the existing list - 'get_words_from_line'.
        list_of_words_in_file += get_words_from_line(line)

    return list_of_words_in_file


if __name__ == "__main__":
    print(get_words_from_file())
