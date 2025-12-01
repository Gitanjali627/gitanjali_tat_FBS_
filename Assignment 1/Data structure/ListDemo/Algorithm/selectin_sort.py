def selectionSort(li):
    size = len(li)
    for i in range(0, size):
        min = 1
        for j in range(i +1, size):
            if(li[min] > li[j]):
                min = j
        li[i], li[min] = li[min], li[i]
        print(li)
    return li

li = [60, 50, 40, 30, 20, 10]
print("Before sorting:", li)
li = selectionSort(li)
print("After sorting:", li)

###Time complexity
#1.Worst case: 0(n ^ 2)
#2. Average case: 0(n^2)
#3. best case: 0(n^2)
