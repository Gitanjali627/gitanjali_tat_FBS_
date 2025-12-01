# Program 2: Calculate percentage and average marks
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i+1)
    total = 0
    for j in range(5):
        marks = float(input(f"Enter marks of subject {j+1}: "))
        total += marks
    percent = total / 5
    print(f"Percentage of Student {i+1}: {percent:.2f}%")

print("\nCalculation complete!")