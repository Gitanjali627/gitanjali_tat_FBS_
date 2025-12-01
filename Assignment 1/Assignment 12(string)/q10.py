s1 = "apple"
s2 = "pineapple"

count1 = 0
for _ in s1:
    count1 += 1

count2 = 0
for _ in s2:
    count2 += 1

if count1 > count2:
    print("Larger:", s1)
else:
    print("Larger:", s2)