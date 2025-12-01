num = 1
for row in range(1, 11):
    line = []
    for col in range(10):
        line.append(num)
        num += 1
    
    if row % 2 == 0:
        line.reverse()

    print(line)