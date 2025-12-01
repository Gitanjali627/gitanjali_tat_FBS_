import math

def sum_series2(n):
    s = 0
    for i in range(1, n + 1):
        s += math.factorial(i)
    return s

n = int(input("Enter n: "))
print("Sum =", sum_series2(n))