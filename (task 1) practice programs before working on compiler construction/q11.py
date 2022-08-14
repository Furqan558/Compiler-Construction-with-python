lis = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

iterations = len(lis)
for i in range(0, iterations):   # (2,5)
    # print(min)
    # print(i[1])
    for j in range(0, iterations-i-1):  # (2,5)
        if (lis[j][-1] > lis[j + 1][-1]):
            temp = lis[j]
            lis[j] = lis[j + 1]
            lis[j + 1] = temp


print(lis)
