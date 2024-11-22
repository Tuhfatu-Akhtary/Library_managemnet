import save_all_books

def remove_book(all_books):
    isbn_to_remove = int(input("Enter the ISBN of the book you want to remove: "))

    for book in all_books:
        if book['isbn'] == isbn_to_remove:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book removed successfully!")
            return

    print("Book with the given ISBN not found.")
