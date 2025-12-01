# Program to check marriage eligibility

# Input gender and age
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

# Check eligibility
if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
    print("Eligible for marriage.")
else:
    print("Not eligible for marriage.")