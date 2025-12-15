class Shirt:
    base_price = 1000   # static base price

    def __init__(self, sid=0, sname="NA", stype="Formal", size="Small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size
        self.price = self.calculate_price()

    @staticmethod
    def calculate_price_by_size(size):
        if size == "Small":
            return Shirt.base_price
        elif size == "Medium":
            return Shirt.base_price * 1.1
        elif size == "Large":
            return Shirt.base_price * 1.2
        elif size == "XLarge":
            return Shirt.base_price * 1.3

    def calculate_price(self):
        return Shirt.calculate_price_by_size(self.size)

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.stype)
        print("Size:", self.size)
        print("Price:", self.price)

    def __del__(self):
        print("Shirt object destroyed")


# Object creation
s1 = Shirt(301, "Raymond", "Formal", "Small")
s2 = Shirt(302, "Arrow", "Casual", "Medium")
s3 = Shirt(303, "Peter England", "Formal", "Large")

s1.showShirt()
print()
s2.showShirt()
print()
s3.showShirt()