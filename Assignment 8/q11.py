def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

n = int(input("Enter number: "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")