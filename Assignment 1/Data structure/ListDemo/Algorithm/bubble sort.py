def bubbleSort(li):
    size = len (li)
    for i in range (1, size):
        for j in range (0, size-1):
            print(j, end = '')
            if (li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j +1], li[j]
            print(li)
        return li

li =[60, 50, 40, 30, 20, 10]
print ("Before Sorting:", li)
li = bubbleSort(li)
print ("After Sorting:", li)

###Time comlexity
#1. worst case: 0(n^2)
#2. Average case:0(n^2)
#3. Best case:0(n^2)