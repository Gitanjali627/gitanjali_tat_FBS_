lst = [5, 1, 5, 2, 5, 3]
n = 5
new = []

for x in lst:
    if x != n:
        new.append(x)

print("List after removing", n, "=", new)