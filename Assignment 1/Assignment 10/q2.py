lst = [10, 3, 25, 8, 1]

maxi = lst[0]
mini = lst[0]

for x in lst:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x

print("Maximum =", maxi)
print("Minimum =", mini)