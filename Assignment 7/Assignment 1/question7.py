# Program to find roots of a quadratic equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b ** 2) - (4 * a * c)

# Check the nature of the discriminant and find roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)
    print("Roots are real and equal.")
    print("Root 1 = Root 2 =", root)

else:
    realPart = -b / (2 * a)
    imagPart = math.sqrt(-d) / (2 * a)
    print("Roots are complex and different.")
    print("Root 1 =", realPart, "+", imagPart, "i")
    print("Root 2 =", realPart, "-", imagPart, "i")