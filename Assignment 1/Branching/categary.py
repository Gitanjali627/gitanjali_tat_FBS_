# Input from user
n = int(input("Enter a number: "))

# Check the range
if n > 0:
    if n > 50:
        if n > 100:
            if n > 150:
                if n > 200:
                    if n > 250:
                        print("Number is greater than 250")
                    else:
                        print("Number is between 201 and 250")
                else:
                    print("Number is between 151 and 200")
            else:
                print("Number is between 101 and 150")
        else:
            print("Number is between 51 and 100")
    else:
        print("Number is between 1 and 50")
else:
    print("Number is less than or equal to 0")