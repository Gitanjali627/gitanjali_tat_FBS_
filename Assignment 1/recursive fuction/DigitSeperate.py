def digSep(num):
    if(num <= 0):
        pass
    else:
        digit = num % 10
        print(digit)
        num = num // 10
        digSep(num)

n = int(input("Enter a number:"))
digSep(n)

    