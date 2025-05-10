from stats import number_of_words, number_of_characters, sorted_character_list, report_character_count
import sys

cl_args = sys.argv

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = cl_args[1]
    text = get_book_text(book_path)

    # Send text and get number of words in the text file.
    word_count = number_of_words(text)

    # Send text and get dictionary where characters are counted.
    character_count_dictionary = number_of_characters(text)

    # Send dictionary and get list with dictonaries that are sorted in descending character count order.
    list_of_sorted_dictionaries = sorted_character_list(character_count_dictionary)

    # Send list of dictionaries and get an ordered string of character count.
    refined_character_count = report_character_count(list_of_sorted_dictionaries)

    print(
    "============ BOOKBOT ============\n"
    f"Analyzing book found at {book_path}...\n"
    "----------- Word Count ----------\n"
    f"Found {word_count} total words\n"
    "--------- Character Count -------\n"
    f"{refined_character_count}\n"
    "============= END ==============="
    )

if len(cl_args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
