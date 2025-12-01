def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    return sum(i for i in range(2, n + 1) if is_prime(i))

n = int(input("Enter n: "))
print("Sum of prime numbers =", sum_primes(n))