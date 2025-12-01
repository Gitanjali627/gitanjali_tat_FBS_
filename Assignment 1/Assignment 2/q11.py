# Program to find minimum number of notes needed for a given amount

# Input the amount
amount = int(input("Enter the amount: "))

# Initialize note denominations (you can change as per currency)
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum number of notes needed:")

# Loop through each denomination
for note in notes:
    if amount >= note:
        count = amount // note     # Number of notes of this denomination
        amount = amount % note     # Remaining amount
        print(note, "x", count)