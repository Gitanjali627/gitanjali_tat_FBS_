##perform a multiple task are iterables
## map return time
## to use get output multiple times
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x: x ** 3, data))

print(result)