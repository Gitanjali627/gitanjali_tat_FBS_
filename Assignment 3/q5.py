# Program to check type of triangle

# Input all sides of the triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check triangle type
if a == b == c:
    print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")