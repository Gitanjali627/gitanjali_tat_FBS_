lst = [5, 2, 7, 5, 9, 5]
n = 5

count = 0
for x in lst:
    if x == n:
        count += 1

if count > 0:
    print(n, "is present", count, "times")
else:
    print(n, "is NOT present")