# Program to convert days into years, weeks, and days

days = int(input("Enter number of days: "))

# Calculate years, weeks, and remaining days
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

# Display the result
print("Years =", years)
print("Weeks =", weeks)
print("Days =", remaining_days)
