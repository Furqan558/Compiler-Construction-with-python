def read_files(files):
    Reads = []

    for i in files:
        temp_values = []
        f = open(f"{i}", "r")
        lines = f.readline()
        lines.replace("\n", "")
        temp_values.append(lines.split())
        Reads.append(temp_values)
        f.close()
    return Reads


def read_table(table_file):
    given_table = []
    converted = []
    f = open(table_file, "r")
    lines = f.readlines()
    for line in lines:
        line.replace("\n", "")
        line.replace("  ", "")
        given_table.append(line.split())

    for x in given_table:
        lis = []
        for y in x:
            lis.append(y)
        converted.append(lis)
    f.close()
    # print(converted)
    return converted


def con(arr):
    return arr[0]


# "->" = "="
# NP = E, VP = V, DT = D, NN = N, SBAR = A, VBD = C, PRP = T, IN = I
# motorcycle = y, guy = g, sister = b, rode = o, married = m, rusted = u, that = h, the = e, my = i
symbol = ["$", "h", "u", "m", "o", "b", "g", "y", "i",
          "e", "S", "E", "V", "A", "D", "T", "N", "C", "I"]
rhs = ["EV", "DN", "TN", "EA", "C", "IS", "e",
       "i", "y", "g", "b", "o", "m", "u", "h"]
lhs = ["S", "E", "E", "E", "V", "A", "D",
       "T", "N", "N", "N", "C", "C", "C", "I"]
table = []

input = "ibmeghoeyhu$"
stack = [0]
row = stack[-1]
col = input[0]


# def start_parse():
#     global input
#     global row
#     global col
#     global stack
#     input =
#     stack = [0]
#     row = stack[-1]
#     col = input[0]


def shift_stack():
    global input
    global row
    global col
    print(table[row][col])
    s_temp = table[row][col]
    print(s_temp)
    stack.append(input[0])
    stack.append(int(s_temp.replace('s', '')))
    input = input[1:]
    row = int(stack[-1])


def reduce_stack():
    global row
    global col
    r_temp = table[row][col]
    temp = int(r_temp.replace('R', ''))
    l = len(rhs[temp])
    l = l*2
    for x in range(l):
        stack.pop()
    stack.append(lhs[temp])
    row = int(stack[-2])
    col = symbol.index(stack[-1])
    r_temp = table[row][col]
    if "s" in table[row][col]:
        temp = int(r_temp.replace('s', ''))
    elif "R" in table[row][col]:
        temp = int(r_temp.replace('R', ''))
    else:
        temp = int(r_temp)
    stack.append(temp)
    # restores the row number after pushing the number that was extracted using last two items of stack
    row = stack[-1]


def slr1_parser():
    global col
    while(True):
        input_s = input[0]
        col = symbol.index(input_s)
        if 's' in table[row][col]:
            shift_stack()
        elif "R" in table[row][col]:
            reduce_stack()
        elif "accept" in table[row][col] and input[0] == "$":
            print("Parsing successful")
            print(stack)
            break
        else:
            print("Parsing failed")
            print(stack)
            break


other_files = ["production.txt", "validInput.txt"]
data = read_files(other_files)
table = read_table("table.txt")
slr1_parser()
