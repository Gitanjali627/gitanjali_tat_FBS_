# Program to check if a 3-digit number is a palindrome

# Input number
num = int(input("Enter a 3-digit number: "))

# Reverse the number
rev = int(str(num)[::-1])

# Check palindrome
if num == rev:
    print(num, "is a Palindrome number.")
else:
    print(num, "is not a Palindrome number.")