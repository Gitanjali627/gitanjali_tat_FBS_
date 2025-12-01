# Program to swap two numbers using a third variable

# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping using a third variable
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)