# Write a program that reads input data from file “file.txt” character by character and
# output each character separated by “tab”. Some characters are separator , they should
# be titled with separator. { “ “, ; , =, ==, ( , ), { , } } are separators.

f = open("file.txt", "r")
data = f.readlines()
seprators = ['"', ';', '=', '==', '(', ')', '{', '}']
for line in data:
    for word in line:
        if word in seprators:
            print(word, "This is a seprator")
        else:
            print(word, end="")
