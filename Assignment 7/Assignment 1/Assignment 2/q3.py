# Program to convert feet and inches into meters and centimeters

# Input distance in feet and inches from user
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Conversion factors
# 1 foot = 0.3048 meters
# 1 inch = 0.0254 meters

# Convert feet and inches to meters
total_meters = (feet * 0.3048) + (inches * 0.0254)

# Separate into meters and centimeters
meters = int(total_meters)
centimeters = (total_meters - meters) * 100

# Display the result
print("Distance =", meters, "meters and", round(centimeters, 2), "centimeters")