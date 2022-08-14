# Write a program that read a tabular structure data from a file “data.txt” and save in 2d
# list. Data is separated by “Tab”. Control characters must be eliminated from data. For
# example
# 12 state2
# test abc
# 26 cui
# list=[[“12”,”state2”],[“test”, “abc”], [“26”, “cui”]]

f = open("data.txt", "r")
data = f.readlines()
complete_list = []
for line in data:
    line = line.rstrip()
    temp = line.split("    ")
    complete_list.append(temp)
    # print(temp)
print(complete_list)
