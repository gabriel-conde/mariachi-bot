import sys
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import get_sorted_dictionary

# This function reads the contents of a book file and returns it as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# Main function to execute the book analysis.
def main():

    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:

        # If not, print usage instructions and exit
        print("Usage: python3 main.py <path_to_book>")

        # Exit the program with a non-zero status to indicate an error
        sys.exit(1)

    # Get the book path from command line arguments
    book_path = sys.argv[1]

    # Read the book text from the specified path
    text = get_book_text(book_path)

    # Get the number of words in the book text
    num_words = get_number_of_words(text)

    # Get the number of characters in the book text
    num_characters = get_number_of_characters(text)

    # Get the sorted list of characters and their counts
    sorted_characters = get_sorted_dictionary(num_characters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print the sorted character counts
    for char_dict in sorted_characters:

        # Extract character and count from the dictionary
        char = char_dict["char"]
        count = char_dict["num"]

        print(f"{char}: {count}")
    print("============= END ===============")

main()