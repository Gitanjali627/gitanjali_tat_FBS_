def linearSearch(li, searchEle):
    for ind in range(0, len(li)):
        if(li[ind] == searchEle):
            return ind
    else:
        return -1

li = [25, 39, 70, 26, 55, 89]
ele = int(input("Enter number to find:"))
result = linearSearch(li, ele)
if(result != -1):
    print(f'{ele} is present at index {result}.')
else:
    print(f'{ele} is not present in list.')


###Time complexity
#Best: 0(1)
#Worst:0(n)
#Average: 0(n)


