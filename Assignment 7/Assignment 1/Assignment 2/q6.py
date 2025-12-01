# Program to calculate total salary of an employee

# Input basic salary
basic = float(input("Enter the Basic Salary of the employee: "))

# Calculate allowances
da = 0.10 * basic    # DA = 10% of basic
ta = 0.12 * basic    # TA = 12% of basic
hra = 0.15 * basic   # HRA = 15% of basic

# Calculate total salary
total_salary = basic + da + ta + hra

# Display the results
print("\n--- Salary Details ---")
print("Basic Salary =", basic)
print("DA (10%) =", da)
print("TA (12%) =", ta)
print("HRA (15%) =", hra)
print("Total Salary =", total_salary)