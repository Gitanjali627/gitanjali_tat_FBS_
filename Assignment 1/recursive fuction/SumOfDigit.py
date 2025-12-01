def digSep(num):
    if(num <= 0):
        return 0
    else:
       return (num % 10) + digSep(num // 10)

n = int(input("Enter a number:"))
print(digSep(n))