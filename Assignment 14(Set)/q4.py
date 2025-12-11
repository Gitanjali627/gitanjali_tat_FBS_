nums = [1, 2, 3, 4, 5, 6]
target = 7

pairs = set()

for x in nums:
    if (target - x) in nums:
        pairs.add(tuple(sorted((x, target - x))))

print(pairs)