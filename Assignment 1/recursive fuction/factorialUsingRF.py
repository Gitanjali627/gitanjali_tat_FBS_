#WAP to calculate factorial using recursive function
def  fact(n):
    if (n == 0):
        return 1
    elif(n < 0):
        return f'{n} is an negative number.'
    else:
        return n * fact(n-1)

n = int(input("Enter value:"))
result = fact(n)
print(result)

