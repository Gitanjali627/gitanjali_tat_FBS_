# Program 3: Ticket cost with discount
passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost per person: "))
total = 0

for i in range(passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        cost = ticket_cost * 0.7
    elif age > 59:
        cost = ticket_cost * 0.5
    else:
        cost = ticket_cost
    total += cost

print(f"\nTotal Ticket Amount: ₹{total:.2f}")