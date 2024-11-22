import save_all_books

def update_book(all_books):
    isbn_to_update = int(input("Enter the ISBN of the book you want to update: "))

    for book in all_books:
        if book['isbn'] == isbn_to_update:
            print("Book found!")
            print("Enter new details. Press Enter to keep the current value.")

            book['title'] = input(f"Title ({book['title']}): ") or book['title']
            book['author'] = input(f"Author ({book['author']}): ") or book['author']
            book['publishing_year'] = int(
                input(f"Publishing Year ({book['publishing_year']}): ") or book['publishing_year'])
            book['price'] = int(input(f"Price ({book['price']}): ") or book['price'])
            book['quantity'] = int(input(f"Quantity ({book['quantity']}): ") or book['quantity'])

            save_all_books.save_all_books(all_books)
            print("Book updated successfully!")
            return

    print("Book with the given ISBN not found.")
