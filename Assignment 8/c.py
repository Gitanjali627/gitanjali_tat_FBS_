def sum_series3(n):
    return sum(i ** i for i in range(1, n + 1))

n = int(input("Enter n: "))
print("Sum =", sum_series3(n))