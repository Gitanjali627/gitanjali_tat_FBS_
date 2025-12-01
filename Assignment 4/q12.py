start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Armstrong numbers are:")
for num in range(start, end+1):
    temp = num
    sum_cube = 0
    while temp > 0:
        digit = temp % 10
        sum_cube += digit ** 3
        temp //= 10
    if sum_cube == num:
        print(num)