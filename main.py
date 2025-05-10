from stats import *
import sys

cl_args = sys.argv

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(cl_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = cl_args[1]
    text = get_book_text(book_path)

    # Send text and get number of words in the text file.
    word_count = number_of_words(text)

    # Send text and get dictionary where characters are counted.
    character_count_dictionary = number_of_characters(text)

    # Send dictionary and get list with dictonaries that are sorted in descending character count order.
    list_of_sorted_dictionaries = sorted_character_list(character_count_dictionary)

    # Send bookpath, wordcount and list of sorted dictionaries and get report printed.
    print_report(book_path, word_count, list_of_sorted_dictionaries)

main()
