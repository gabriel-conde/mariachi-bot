import sys
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import get_sorted_dictionary


# This function reads the contents of a song file and returns it as a string.
def get_song_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# Main function to execute the song analysis.
def main():

    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:

        # If not, print usage instructions and exit
        print("Incorrect Usage: Try 'python3 main.py <path_to_song>'")

        # Exit the program with a non-zero status to indicate an error
        sys.exit(1)

    # Get the song path from command line arguments
    song_path = sys.argv[1]

    # Read the song text from the specified path
    text = get_song_text(song_path)

    # Get the number of words in the song text
    num_words = get_number_of_words(text)

    # Get the number of characters in the song text
    num_characters = get_number_of_characters(text)

    # Get the sorted list of characters and their counts
    sorted_characters = get_sorted_dictionary(num_characters)

    print("============ MARIACHI SONG BOT ============")
    print(f"Analyzing song found at {song_path} ...")
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print the sorted character counts
    for char_dict in sorted_characters:

        # Extract character and count from the dictionary
        char = char_dict["char"]
        count = char_dict["num"]

        print(f"{char}: {count}")
    print()
    print("=========== LYRICS ==============")
    print()
    print(text)
    print()
    print("============= END ===============")

main()