s1 = "hello"
s2 = "worldwide"

c1 = c2 = 0

for _ in s1:
    c1 += 1
for _ in s2:
    c2 += 1

if c1 > c2:
    print("Larger string:", s1)
else:
    print("Larger string:", s2)