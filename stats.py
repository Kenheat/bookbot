# Returns total number of words in the text file
def number_of_words(text):
    words = text.split()
    return len(words)

# Returns a dictionary where the keys are a single character and
# the values are the total number of times the single character appears in the text
def number_of_characters(text):
    char_count_dict = {}

    for char in text:
        lc_char = char.lower()
        if lc_char not in char_count_dict:
            char_count_dict[lc_char] = 1
        else:
            char_count_dict[lc_char] += 1
    
    return char_count_dict

# A function that takes a dictionary and returns the value of the "num" key.
# This is how the '.sort()' method knows how to sort the list of dictionaries.
def sort_on(dict):
    return dict["num"]

# Returns a list with dictionaries. Each dictionary have two key-value pairs:
# One for the character itself and one for that character's count.
# e.g. {"char": "b", "num": 4868}
# The list is sorted in descending character count order.
def sorted_character_list(dictionary):
    list_of_dicts = []

    for character in dictionary:
        temporary_dict = {"char": character, "num": dictionary[character]}
        list_of_dicts.append(temporary_dict)
    
    list_of_dicts.sort(reverse=True, key=sort_on)
            
    return list_of_dicts

def print_report(book_path, word_count, list_of_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in list_of_dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
