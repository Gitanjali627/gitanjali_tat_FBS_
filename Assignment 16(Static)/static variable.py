class Book:
    count = 0   # static variable

    def __init__(self, bid=0, bname="NA", price=0.0, author="NA"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        print("Book object destroyed")


# Object creation
b1 = Book(101, "Python", 450, "Guido")
b2 = Book(102, "Java", 500, "James")

b1.showBook()
print()
b2.showBook()
print("\nTotal Books Created:", Book.count)