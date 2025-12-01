# Program to calculate total ticket cost for 5 people

total_amount = 0

for i in range(1, 6):
    print("\nPerson", i)
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))
    
    if age < 12:
        discount = ticket * 0.30     # 30% discount
        amount = ticket - discount
    elif age > 59:
        discount = ticket * 0.50     # 50% discount
        amount = ticket - discount
    else:
        amount = ticket              # no discount
        
    print("Final ticket amount for person", i, "=", amount)
    total_amount += amount

print("\nTotal amount to be paid for all 5 people =", total_amount)