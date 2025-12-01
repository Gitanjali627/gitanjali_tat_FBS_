lst = [1, 2, 2, 3, 4, 4, 5]
new = []

for x in lst:
    found = 0
    for y in new:
        if x == y:
            found = 1
            break
    if found == 0:
        new.append(x)

print("List without duplicates =", new)