#1. Structure:{}, key : value
dict = {1:'Python', 2:'java', 3:'C', 'a': 345}

#2. Type of data: hetrogenous
print(dict)

#3. Sequence: Ordered

#4. Changable: Key-Immutable, Value-Mutable
dict['a'] = 999
print(dict)

dict['b'] = 1000
print(dict)

dict2 = {(1,2,3):'First value 1', [10, 20, 30]:'Second value'}
print(dict2)