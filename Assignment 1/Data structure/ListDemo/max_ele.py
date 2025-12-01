def maxEle(li):
    max = li[0]
    for ind in range(0, len(li)):
        if(max < li[ind]):
            max = li[ind]
    return max
li = [34, 65, 23, 56, 89, 26, 46, 76, 85]
max_ele = maxEle(li)
print("Maximum ele is", max_ele)
