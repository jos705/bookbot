from stats import count_words, count_characters, sort_output
import sys

def check_args(args):
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookfile = args[1]
    return bookfile

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    bookfile = check_args(sys.argv)
    file_contents = get_book_text(bookfile)
    num_words = count_words(file_contents)
    counted_characters_sorted = sort_output(count_characters(file_contents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for p in counted_characters_sorted:
        print(f"{p["char"]}: {p["num"]}")
    print("============= END ===============")


main()