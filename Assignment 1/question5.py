#program to calculate compound
P = float (input("Enter the principal amount:"))
T = float (input("Enter the time(in years):"))
R = float (input("Enter the rate of interest:"))

#calculate compound interest
A = P * (1 + R // 100)** T
CI = A -P

#Display result
print ("Compound Interest =", CI)
print ("Total Amount =", A)