# Program to calculate electricity bill

# Input units from user
units = int(input("Enter the number of units consumed: "))

# Initialize amount
amt = 0

# Calculate bill based on units
if units > 0:
    if units <= 50:
        amt = units * 0.5
    elif units <= 150:
        amt = 50 * 0.5 + (units - 50) * 0.75
    elif units <= 250:
        amt = 50 * 0.5 + 100 * 0.75 + (units - 150) * 1.2
    else:
        amt = 50 * 0.5 + 100 * 0.75 + 100 * 1.2 + (units - 250) * 1.5
else:
    amt = 0

# Display the total amount
print("Electricity Bill Amount = ₹", amt)