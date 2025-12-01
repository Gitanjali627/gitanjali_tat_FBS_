# Program to calculate selling price of a book based on cost price and discount

# Input cost price and discount
cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))

# Calculate discount amount
discount_amount = (cost_price * discount) / 100

# Calculate selling price
selling_price = cost_price - discount_amount

# Display the result
print("Discount Amount =", discount_amount)
print("Selling Price of the book =", selling_price)
