n = int(input("Enter a number: "))
temp = n
sum_fact = 0

while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    sum_fact += fact
    n //= 10

if sum_fact == temp:
    print(temp, "is a Strong Number")
else:
    print(temp, "is not a Strong Number")