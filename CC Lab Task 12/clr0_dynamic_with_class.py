class NT:
    def __init__(self, symbol, attr) -> None:
        self.symbol = symbol
        self.attr = attr
        print(self.attr)


def read_files(files):
    Reads = []
    for i in files:
        table = []
        f = open(f"{i}", "r")
        lines = f.readline()
        lines.replace("\n", "")
        table.append(lines.split())
        Reads.append(table)
        f.close()
    return Reads


def read_table(table_file):
    given_table = []
    converted = []
    f = open(table_file, "r")
    lines = f.readlines()
    for line in lines:
        line.replace("\n", "")
        given_table.append(line.split())

    for x in given_table:
        lis = []
        for y in x:
            lis.append(int(y))
        converted.append(lis)
    f.close()
    return converted


def con(arr):
    return arr[0]


symbol = ["c", "d", "$", "S", "C"]
rhs = ["S", "CC", "cC", "d"]
lhs = ["J", "S", "C", "C"]
table = [
    ["S3", "S4", "", "1", "2"],
    ["", "", "accept", "", ""],
    ["S6", "S7", "", "", "5"],
    ["S3", "S9", "", "", "8"],
    ["R3", "R3", "", "", ""],
    ["", "", "R1", "", ""],
    ["S6", "S7", "R0", "", "9"],
    ["", "", "R3", "", ""],
    ["R2", "R2", "", "", ""],
    ["", "", "R2", "", ""],
]

input = "dcd$"
stack = [0]
row = stack[-1]
col = input[0]


def shift_stack():
    global input
    global row
    global col
    s_temp = table[row][col]
    stack.append(input[0])
    stack.append(int(s_temp.replace('S', '')))
    input = input[1:]
    row = int(stack[-1])


def reduce_stack():
    global row
    global col
    r_temp = table[row][col]
    temp = int(r_temp.replace('R', ''))
    print(temp)
    l = len(rhs[temp])
    reduced_symbol = rhs[temp]
    l = l*2
    for x in range(l):
        stack.pop()
    # stack.append(lhs[temp])
    stack.append(NT(symbol=lhs[temp], attr=reduced_symbol))
    row = int(stack[-2])
    obj = stack[-1]
    # col = symbol.index(stack[-1])
    col = symbol.index(obj.symbol)
    r_temp = table[row][col]
    if "S" in table[row][col]:
        temp = int(r_temp.replace('S', ''))
    elif "R" in table[row][col]:
        temp = int(r_temp.replace('R', ''))
    else:
        temp = int(r_temp)
    stack.append(temp)
    # restores the row number after pushing the number that was extracted using last two items of stack
    row = stack[-1]


def clr0_parser():
    global col
    # Rules_input = con(data[0])
    # String_input = con(data[1])
    # print(Rules_input)
    # print(String_input)
    # print(table[row][col])
    while(True):
        input_s = input[0]
        col = symbol.index(input_s)
        if 'S' in table[row][col]:
            shift_stack()
        elif "R" in table[row][col]:
            reduce_stack()
        elif "accept" in table[row][col] and input[0] == "$":
            print("Parsing successful")
            break
        else:
            print("Parsing failed")
            break
        print(stack)


# other_files = ["production.txt", "validInput.txt"]
# data = read_files(other_files)
# table = read_table("table.txt")
clr0_parser()
