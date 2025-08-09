def get_number_of_words(text):
    # convert text to a list of words
    words = text.split()
    # Count the number of words in the list
    num_words = len(words)
    return num_words

def get_number_of_characters(text):
    """
    Takes text from a song as a string and returns a dictionary with the count
    of each character (including symbols and spaces) in lowercase.
    """
    # Convert text to lowercase for case-insensitive counting
    text_lower = text.lower()
    
    # Initialize empty dictionary to store character counts
    number_of_characters = {}
    
    # Iterate through each character in the text
    for char in text_lower:
        # If character already exists in dictionary, increment count
        if char in number_of_characters:
            number_of_characters[char] += 1
        # If character doesn't exist, add it with count of 1
        else:
            number_of_characters[char] = 1
    
    return number_of_characters

def get_sorted_dictionary(dictionary):
    """
    Takes a dictionary and returns a sorted list of tuples (key, value) in descending order
    based on the values.
    """
    # Sort the dictionary by value in descending order
    sorted_dictionaries = []
    # Iterate through the dictionary items
    for char in dictionary:
        # Get the count of the character from the dictionary
        count = dictionary[char]
        # Create a dictionary with "char" and "num" keys
        char_dict = {"char": char, "num": count}
        # Append the character dictionary to the sorted list
        sorted_dictionaries.append(char_dict)
    
    # A function to sort the dictionaries based on the "num" key
    def sort_on(item):
        return item["num"]
    
    # Sort the list of dictionaries in descending order based on the "num" key
    sorted_dictionaries.sort(reverse=True, key=sort_on)

    return sorted_dictionaries