import add_books
import view_all_books
import update_book
import remove_book

all_books=[]

while True:
    print("Welcome to Library Management System!")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Book")
    print("3. Update Book")
    print("4. Remove Book")


    option=input("Select option")

    if option == "0":
        print("Thanks for using Library Management System")
        break

    elif option == "1":
        add_books.add_books(all_books)

    elif option == "2":
        view_all_books.view_all_books(all_books)

    elif option == "3":
        update_book.update_book(all_books)

    elif option == "4":
        remove_book.remove_book(all_books)

    else:
        print("Choose a valid option")
