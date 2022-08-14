# Write a program data uses program 2 output and write it to file “output.txt”


f = open("file.txt", "r")
output = open("output.txt", "a")
data = f.readlines()
seprators = ['"', ';', '=', '==', '(', ')', '{', '}']
for line in data:
    for word in line:
        if word in seprators:
            temp = word+"This is a seprator"
            output.write(temp)
            output.write("\n")
        else:
            output.write(word)
