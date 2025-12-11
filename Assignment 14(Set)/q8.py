words = ["eat", "tea", "ate", "bat", "tab", "tan", "nat"]

groups = {}

for w in words:
    key = "".join(sorted(w))
    groups.setdefault(key, []).append(w)

print(groups)