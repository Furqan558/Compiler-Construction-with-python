# . write a program that reads data from file, and save it to list, with following sample
# data.
# 0 a 1
# 0 a 2
# 1 a 4
# 2 b 3
# 3 x 3
# 4 f 6
# following should be the output
# list = [ “0 a 1”, “0 a 2”,"0 a 2", “1 a 4”, “2 b 3”, “3 x 3”, “4 f 6”]
# Do following tasks
# 1. Input a character from user e.g a
# 2. Input an integer from user e.g 0
# 3. create an empty set
# 4. Iterate through list, split each element with “Tab”, convert first value of splitted list
# to integer. If input character (in task 1) and second value of splitted list are equal and
# integer is equal to first value, then append last element of splitted list to set (defined in
# step 3).
# At the end print the value of set.
# For example suppose we enter “a” in step 1 , and “0” in step 2, ultimate value of set will
# be {1,2}

f = open("q4.txt", "r")
new_list = []
with open("q4.txt", "r")as file:
    for line in file:
        new_list.append(line.strip())

print(new_list)

unique_set = set()
char = input("Please Input Character :")
integer = input("Please Input Number :")
# print(new_list[0][2])
for i in new_list:
    if integer == i[0] and char == i[2]:
        unique_set.add(i[4])
f.close()
print(unique_set)
