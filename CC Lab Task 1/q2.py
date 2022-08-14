mystr = "w3resource"
new_dict = {}
for i in range(len(mystr)):
    count1 = mystr.count(mystr[i])
    new_dict[mystr[i]] = count1

for key, value in new_dict.items():
    print(key)
    print(value)
