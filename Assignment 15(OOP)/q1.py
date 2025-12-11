class Book:
    # Constructor (parameterized + parameterless)
    def __init__(self, bid=0, bname="NA", price=0.0, author="NA"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book Object Created")

    # Destructor
    def __del__(self):
        print("Book Object Deleted")

    # Show method
    def showBook(self):
        print("---- Book Details ----")
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)


# Creating objects
b1 = Book()
b1.showBook()

b2 = Book(101, "Python Programming", 550, "Guido Rossum")
b2.showBook()