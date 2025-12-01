# Program to find the sum of digits of a three-digit number

# Input a three-digit number
num = int(input("Enter a three-digit number: "))

# Extract digits
digit1 = num // 100            # hundreds place
digit2 = (num // 10) % 10      # tens place
digit3 = num % 10              # ones place

# Calculate sum
sum_of_digits = digit1 + digit2 + digit3

# Display the result
print("Sum of digits =", sum_of_digits)