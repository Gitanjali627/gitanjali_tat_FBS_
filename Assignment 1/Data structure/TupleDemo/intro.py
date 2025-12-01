#1. structure: ()
tu (10,)
tu = ()

#2. Type of data: heterogeneous
tu (10, 3.14, 'a')
print(type(tu))

#3. Sequence: Ordered
print(tu)

#4. Changable: Immutable
# tu[0] = 39 agives error

#5. Speed: Faster the list
import sys
tu = ()
print(sys.getsizeof(tu))
li = []
print(sys.getsizeof(li))

