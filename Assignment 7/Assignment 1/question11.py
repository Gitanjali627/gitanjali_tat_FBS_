# Program to find area and circumference of a circle

import math  # to use the value of pi (π)

# Input radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius * radius
circumference = 2 * math.pi * radius

# Display the results
print("Area of the circle =", area)
print("Circumference of the circle =", circumference)