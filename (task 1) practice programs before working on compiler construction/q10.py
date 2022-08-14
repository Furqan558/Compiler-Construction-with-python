def compare(a):
    counter = 0
    for i in a:
        if len(i) > 2 and i[0] == i[-1]:
            counter += 1
    return counter


a = ['abc', 'xyz', 'aba', '1221', 'aaa', 'asdasdsada']
for i in a:
    z = compare(a)

print(z)
