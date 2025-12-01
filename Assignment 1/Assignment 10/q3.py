lst = [10, 30, 20, 50, 40]

largest = lst[0]
second = lst[0]

for x in lst:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest =", second)