from stats import get_word_amount

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

def main():
    words = get_word_amount(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()

