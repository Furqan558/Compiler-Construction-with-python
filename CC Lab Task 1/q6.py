my_dict = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
my_list = list(my_dict.items())
my_list.sort(key=lambda x: x[1], reverse=True)
print(my_list)
