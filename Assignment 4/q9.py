start = int(input("Enter start: "))
end = int(input("Enter end: "))
div = int(input("Enter divisor: "))
print("Numbers divisible by", div, ":")
for i in range(start, end+1):
    if i % div == 0:
        print(i)