lst = [1, 2, 3, 4, 5, 6]
new = []

for x in lst:
    if x % 2 != 0:
        new.append(x)

print("List after removing even numbers =", new)