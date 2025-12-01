import random

# Predefined userid and password
userid = "admin"
password = "12345"

# Input from user
u = input("Enter User ID: ")
p = input("Enter Password: ")

if u == userid and p == password:
    # Generate 4-digit random number
    code = random.randint(1000, 9999)
    print("Verification code:", code)
    
    # Ask user to re-enter it
    user_code = int(input("Enter the same code: "))
    
    if user_code == code:
        print("Login Successful ✅")
    else:
        print("Verification Failed ")
else:
    print("Invalid UserID or Password.")