# Returns total number of words in the text file
def number_of_words(text):
    words = text.split()
    return len(words)

# Returns a dictionary where the keys are a single character and
# the values are the total number of times the single character appears in the text
def number_of_characters(text):
    lowercase_text = text.lower()

    unique_characters = []

    for i in lowercase_text:
        if i not in unique_characters:
            unique_characters.append(i)

    character_count_dict = {}
    
    for i in unique_characters:
        character_count_dict[i] = lowercase_text.count(i)
    
    return character_count_dict

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

# Returns an ordered string of character count.
def report_character_count(list_of_dicts):
    new_list = []

    for dict in list_of_dicts:
        if dict["char"].isalpha():
            new_list.append(f"{dict["char"]}: {dict["num"]}")
    
    new_string = ""

    for string in new_list:
        new_string = new_string + string + "\n"

    refined_string = new_string.strip()

    return refined_string
