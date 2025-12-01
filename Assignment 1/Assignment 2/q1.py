# Program to convert time into seconds

# Input hours, minutes, and seconds from user
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert total time into seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Display the result
print("Total time in seconds =", total_seconds)