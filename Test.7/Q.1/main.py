
from book import Book

books = {}

while True:
    print("Store Book Details")

    print("\n1. Add Book")
    print("2. Delete Book")
    print("3. Display Books")
    print("4. Search Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        bid = int(input("Enter Book ID: "))
        name = input("Enter Name: ")
        price = float(input("Enter Price: "))
        author = input("Enter Author: ")

        books[bid] = Book(bid, name, price, author)
        print("Book Added Successfully")

    elif ch == 2:
        bid = int(input("Enter Book ID to Deleted: "))
        if bid in books:
            del books[bid]
            print("Book Deleted")
        else:
            print("Book Not Found")

    elif ch == 3:
        if len(books) == 0:
           print('No books available')
        else:
           for book in books.valies():
               book.display()

    elif ch == 4:
        bid = int(input("Enter Book ID to Search Book: "))
        
        if bid in books:
            b = books[bid]
            print(b.bid, b.name, b.price, b.author)
        else:
            print("Book Not Found")


    elif ch == 5:
        break

    else:
        print("Invalid Choice")
