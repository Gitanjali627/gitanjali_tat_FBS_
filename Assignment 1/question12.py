# Program to find volume of a sphere

import math  # to use pi (π)

# Input radius from user
radius = float(input("Enter the radius of the sphere: "))

# Calculate volume
volume = (4 / 3) * math.pi * (radius ** 3)

# Display the result
print("Volume of the sphere =", volume)