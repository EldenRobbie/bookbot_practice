def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content

def main():
    print(get_book_text("books/frankenstein.txt"))


main()