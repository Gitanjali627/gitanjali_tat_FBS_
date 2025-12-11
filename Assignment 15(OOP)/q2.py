class Product:
    # Constructor
    def __init__(self, pid=0, pname="NA", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product Object Created")

    # Destructor
    def __del__(self):
        print("Product Object Deleted")

    # Show method
    def showProduct(self):
        print("---- Product Details ----")
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


# Creating objects
p1 = Product()
p1.showProduct()

p2 = Product(201, "Laptop", 45000, 2)
p2.showProduct()