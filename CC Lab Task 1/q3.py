mydic = {"1": ['a', 'b'], "2": ['c', 'd']}

for key, value in mydic.items():
    print(key, end='\t')
print('\n')
i = 0
for key1, value1 in mydic.items():
    for value in mydic.items():
        print(value[i], end='\t')
    print('\n')
    i = i+1

# for key1, value1 in mydic.items():
#         if key != key1:
#             for x in range(len(value1)):
#                 print(value[x], value1[x])
