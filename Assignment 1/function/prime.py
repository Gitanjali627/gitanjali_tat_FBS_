def checkPrime(num):
    if(num <= 1):
        return False
    for i in range(2,num // 2 + 1):
        if(num % i == 0):
            return False
    else:
        return True

n = int(input("Enter number to check prime or not:"))
print(checkPrime(n))
if(result):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not prime number.')


