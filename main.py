from stats import get_word_amount, get_character_amounts, sort_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def main():

    book = get_book_text(filepath)

    words = get_word_amount(book)

    characters = get_character_amounts(book)

    sorted_list = sort_characters(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["num"]}")


main()

