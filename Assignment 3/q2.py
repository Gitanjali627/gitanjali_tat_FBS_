# Program to check whether an alphabet is a vowel or consonant
ch = input("Enter an alphabet: ")

# Convert to lowercase for easy comparison
ch = ch.lower()

# Check if it is a vowel
if ch in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a Vowel.")
else:
    print(ch, "is a Consonant.")