x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sort_by_key = dict(sorted(x.items(), key=lambda item: item[0]))
sort_by_value = dict(sorted(x.items(), key=lambda item: item[1]))

print("sort_by_key:", sort_by_key)
print("sort_by_value:", sort_by_value)
