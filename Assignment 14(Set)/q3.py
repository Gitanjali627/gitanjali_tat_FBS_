words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique = set(words)
freq = {w: words.count(w) for w in unique}

print(unique)
print(freq)