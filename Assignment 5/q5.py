# Program 5: Minimum number of notes
amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Notes needed:")
for note in notes:
    count = amount // note
    if count:
        print(note, "x", count)
    amount %= note