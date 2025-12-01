# Program to calculate area of an equilateral triangle

import math  # to use the square root function

# Input side length from user
side = float(input("Enter the side of the equilateral triangle: "))

# Calculate area using formula
area = (math.sqrt(3) / 4) * (side ** 2)

# Display the result
print("Area of the equilateral triangle =", area)