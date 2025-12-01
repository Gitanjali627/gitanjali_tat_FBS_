# Program 1: Login system with 3 attempts
userid = "admin"
password = "1234"

for i in range(3):
    user = input("Enter User ID: ")
    pwd = input("Enter Password: ")
    if user == userid and pwd == password:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials. Try again.")
else:
    print("Too many attempts! Access Denied.")