# Program to swap two numbers without using a third variable

# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping without third variable
a = a + b
b = a - b
a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)