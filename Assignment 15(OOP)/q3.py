class Shirt:
    # Constructor
    def __init__(self, sid=0, sname="NA", type="Formal", price=0.0, size="M"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Shirt Object Created")

    # Destructor
    def __del__(self):
        print("Shirt Object Deleted")

    # Show method
    def showShirt(self):
        print("---- Shirt Details ----")
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)


# Creating objects
s1 = Shirt()
s1.showShirt()

s2 = Shirt(301, "Cotton Shirt", "Casual", 799, "L")
s2.showShirt()