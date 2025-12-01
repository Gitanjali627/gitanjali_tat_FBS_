def sum_odd(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

n = int(input("Enter n: "))
print("Sum of odd numbers =", sum_odd(n))