# Program to reverse a three-digit number

# Input a three-digit number
num = int(input("Enter a three-digit number: "))

# Extract digits
digit1 = num // 100            # hundreds place
digit2 = (num // 10) % 10      # tens place
digit3 = num % 10              # ones place

# Form the reversed number
reverse = (digit3 * 100) + (digit2 * 10) + digit1

# Display result
print("Reversed Number =", reverse)