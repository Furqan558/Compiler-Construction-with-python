from utility import main

print(main())


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


def clean_rule(temp_rule):
    if "print" in temp_rule:
        return temp_rule[7:-2]
    elif "=" in temp_rule:
        return temp_rule[1:]
    else:
        return ""


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


symbol = ["+", "*", "(", ")", "i", "$", "J", "E", "T",
          "F"]  # id is i here and E' is J here
rhs = ["E", "E+T", "T", "T*F", "F", "(E)", "i"]
lhs = ["J", "E", "E", "T", "T", "F", "F"]
rules = ['print("At Last Accepted")', 'print("T is reduced")', 'print("E+T is reduced")',
         'print("F is reduced")', 'print("T*F is reduced")', 'print("(E) is reduced")', 'print("id.val, is reduced")', "=flight"]  # =flight is syntax for putting assignment in these rules and empty can be reperesented by ""

table = [
    ["", "", "S4", "", "S5", "", "", "1", "2", "3"],
    ["S6", "", "", "", "", "accept", "", "", "", ""],
    ["R2", "S7", "", "R2", "", "R2", "", "", "", ""],
    ["R4", "R4", "", "R4", "", "R4", "", "", "", ""],
    ["", "", "S4", "", "S5", "", "", "8", "2", "3"],
    ["R6", "R6", "", "R6", "", "R6", "", "", "", ""],
    ["", "", "S4", "", "S5", "", "", "", "9", "3"],
    ["", "", "S4", "", "S5", "", "", "", "", "10"],
    ["S6", "", "", "S11", "", "", "", "", "", ""],
    ["R1", "S7", "", "R1", "", "R1", "", "", "", ""],
    ["R3", "R3", "", "R3", "", "R3", "", "", "", ""],
    ["R5", "R5", "", "R5", "", "R5", "", "", "", ""],

]

input = "i+i+$"
stack = [0]
row = stack[-1]
col = input[0]
i = 0


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
    current_rule = rules[temp]
    current_rule = clean_rule(current_rule)
    l = l*2
    for x in range(l):
        stack.pop()
    # stack.append(lhs[temp])
    stack.append(NT(symbol=lhs[temp], attr=current_rule))
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


clr0_parser()
