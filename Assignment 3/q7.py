# Program to check if userid and password are correct

# Predefined userid and password
userid = "admin"
password = "12345"

# Input from user
u = input("Enter User ID: ")
p = input("Enter Password: ")

# Check
if u == userid and p == password:
    print("Login Successful!")
else:
    print("Invalid UserID or Password.")