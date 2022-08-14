

mydic = {"1": ['a', 'b'], "2": ['c', 'd']}

for key, value in mydic.items():
    # print(key)
    # print(value)
    for key1, value1 in mydic.items():
        if key != key1:
            for x in range(len(value1)):
                print(value[x], value1[x])
