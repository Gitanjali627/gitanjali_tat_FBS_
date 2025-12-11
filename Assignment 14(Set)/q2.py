set1 = {10, 20, 30, 40}
set2 = {20, 40, 60}

set1 = set1 - (set1 & set2)
print(set1)