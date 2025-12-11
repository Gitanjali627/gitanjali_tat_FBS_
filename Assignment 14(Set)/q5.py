words = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(words[0])):
    char_set = {w[i] for w in words if i < len(w)}
    if len(char_set) == 1:
        prefix += char_set.pop()
    else:
        break

print(prefix)