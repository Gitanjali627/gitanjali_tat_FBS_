#1. Structure: []
li = [10, 20, 30, 40]
print(type(li))

#2. Type of data: Hetroenous
li = [10, 'abc', 3.14]
print(type(li))
print(li)

#3. Sequence: Ordered
print(li)

#4. Changable: Mutable
print(id(li))
li[0] = 20
print(li)
print(id(li))

#5. Duplicate elements can be allowed
#6. By defult not sorted