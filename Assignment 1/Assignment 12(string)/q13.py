s = "Python1234"
digits = letters = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print("Letters:", letters)
print("Digits:", digits)