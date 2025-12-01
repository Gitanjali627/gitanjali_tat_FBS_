###Requirement
#1. data should be shorted
#2. duplicate ele not allowed.

def binarySearch(li, ele):
    beg = 0
    end = len(li)-1
    while(beg <= end):
        mid = (beg + end) // 2
        if(ele == li[mid]):
            return mid
        elif(ele < li[mid]):
            end = mid-1
        elif(ele > li[mid]):
            beg = mid +1
    else:
        return -1

li = [25, 39, 70, 26, 55, 89]
SearchEle = int(input("Enter ele for Search:"))
result = binarySearch(li, SearchEle)
print(result)
