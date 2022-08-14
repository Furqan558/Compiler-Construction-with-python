def difference(lis1, lis2):
    li_dif = [i for i in lis1 + lis2 if i not in lis1 or i not in lis2]
    return li_dif


lis1 = [10, 15, 20, 25, 30, 35, 40]
lis2 = [25, 40, 35]
li3 = difference(lis1, lis2)
print(li3)
