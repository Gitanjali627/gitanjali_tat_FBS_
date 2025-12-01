###Reverse a numder using recursion (second method)
def rev(n):
    if n < 10:
        return str(n)
    return str(n % 10) + rev(n // 10)

num = int(input("Enter number: "))
print("Reversed =", rev(num))
