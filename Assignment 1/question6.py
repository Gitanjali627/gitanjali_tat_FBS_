#program to find third angle of a triangle
angle1 = float (input("Enter first angle of the triangle:"))
angle2 = float (input("Enter second angle of the triangle:"))

#Calculate third angle
angle3 = 180 - (angle1 + angle2)

#Display the result
print ("Third angle of the triangle =",angle3)
