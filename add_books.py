import save_all_books

def add_books(all_books):
    title=input("Enter Book title: ")
    author=input("Enter Author Name: ")
    isbn=int(input("Enter ISBN Number: "))
    publishing_year=int(input("Enter Publishing Year of the Book: "))
    price=int(input("Enter price of the Book: "))
    quantity=int(input("Enter quantity: "))

    book={
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "publishing_year": publishing_year,
        "price" : price,
        "quantity" :quantity,
    }

    all_books.append(book)
    save_all_books.save_all_books(all_books)
    print("Book Added Successfully")

    return all_books