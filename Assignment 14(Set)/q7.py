set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 6}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in Set2:", missing_in_set2)
print("Missing in Set1:", missing_in_set1)