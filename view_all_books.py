def view_all_books(all_books):
    if all_books!=[]:
        for book in all_books:
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"ISBN : {book['isbn']}")
            print(f"Publishing year : {book['publishing_year']}")
            print(f"Price : {book['price']}")
            print(f"Quantity : {book['quantity']}")

    else:
        print("No Book Found")