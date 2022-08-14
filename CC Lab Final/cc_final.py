# Reading tables from files for NFA
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
    stack.append(NT(symbol=lhs[temp], attr=current_rule))
    row = int(stack[-2])
    obj = stack[-1]
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


def parser():
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


def read_fsa_files(files):
    fsa_tables = []
    x = 0
    for i in files:
        table = []
        f = open(f"{i}", "r")
        lines = f.readlines()
        for line in lines:
            line.replace("\n", "")
            table.append(line.split())
        fsa_tables.append(table)
        f.close()
        x = x+1
    return fsa_tables


def read_inputs(input_filename):
    f = open(input_filename, "r")
    inputs = f.readline()
    inputs = inputs.split()
    f.close()
    return inputs


def get_all_characters(filename_list):
    characters_all = []
    for x in filename_list:
        file = open(x, "r")
        lines = file.readlines()
        file.close()
        lines = [x.replace("\n", "").split() for x in lines]
        characters = {x[1] for x in lines}
        characters_all.append(characters)
    return characters_all


def identifier_check():

    return


def fsa_handling(fsa_tables, inputs, characters_all):
    T = ""
    operators_1 = ["=", '+', '-', "*", "&", "!",
                   "|", "~", "<", ">", '^', "[", "]", ":"]
    operators_2 = ["::", '[]', '++', "--", "<=", ">=", "!=",
                   "^=", "%=", '*=', "-=", "+=", "&&", "||", ">>", "<<", "?:"]
    operators_3 = [">>=", '===', "<<="]
    termination_states = [{"1"}]
    fsa_flags = [True for x in range(len(fsa_tables))]
    for sample_input in inputs:
        input_length = len(sample_input)
        print("\n---------------------------Sting starts here---------------------------\n")
        print(sample_input)
        current_state = [{"0"}]

        for id, current_character in enumerate(sample_input):
            if current_character in operators_1:
                if input_length == 1:
                    if current_character in operators_1:
                        print(
                            f"~~~~~~~~~~~~~~~~~~~  operator: {current_character}  ~~~~~~~~~~~~~~~~~~~")
                        operator_flag = True
                        T = T+current_character
                        break
                    else:
                        print(
                            f"!!!!!!!!!!!!!!!!!  Invalid Operator: {current_character}  !!!!!!!!!!!!!!!!!")
                        break
                elif input_length == 2:
                    temp_ip = current_character + sample_input[id+1]
                    if temp_ip in operators_2:
                        print(
                            f"~~~~~~~~~~~~~~~~~~~  operator: {temp_ip}  ~~~~~~~~~~~~~~~~~~~")
                        operator_flag = True
                        T = T + temp_ip
                        break
                    else:
                        print(
                            f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {temp_ip}  ~~~~~~~~~~~~~~~~~~~")
                        break
                elif input_length == 3:
                    temp_ip = current_character + \
                        sample_input[id+1] + sample_input[id+2]
                    if temp_ip in operators_3:
                        print(
                            f"~~~~~~~~~~~~~~~~~~~  operator: {temp_ip}  ~~~~~~~~~~~~~~~~~~~")
                        operator_flag = True
                        T = T+temp_ip
                        break
                    else:
                        print(
                            f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {temp_ip}  ~~~~~~~~~~~~~~~~~~~")
                        break
                else:
                    print(
                        f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {temp_ip}  ~~~~~~~~~~~~~~~~~~~")
                    break

            for i in range(len(fsa_tables)):
                if current_character not in characters_all[i]:
                    fsa_flags[i] = False
                if fsa_flags[i] == False:
                    continue
                print(f"<----------------- FSA {i+1} -------------->")
                print("current state = ", current_state[i])
                print("Input processing = ", current_character)
                next_state = set()
                for my_state in current_state[i]:
                    for current_condition in fsa_tables[i]:
                        if my_state == current_condition[0] and current_character == current_condition[1] and fsa_flags != "T":
                            next_state.add(current_condition[2])

                print("Next state will be = ", next_state)
                current_state[i] = next_state
        for j in range(len(fsa_tables)):
            if fsa_flags[j] == False:
                print(f"FSA{j+1} rejected --invalid character--")
            else:
                for x in current_state[j]:
                    found1 = 0
                    if x in termination_states[j]:
                        found1 = 1
                        print(f"\nFSA{j+1} This string is accepted as last state was : ",
                              current_state[j])
                        if j == 0:
                            T = T+"i"
                    if found1 == 0:
                        print(f"\nFSA{j+1} This string is rejected as last state should be : ",
                              termination_states[j])
        print(fsa_flags)
    print(T)
    return T


table_files = ["identifier.txt"]
inputs = read_inputs("input.txt")
fsa_tables = read_fsa_files(table_files)
characters_all = get_all_characters(table_files)

input = fsa_handling(fsa_tables, inputs, characters_all) + \
    "$"  # lexical analyzer
stack = [0]
row = stack[-1]
col = input[0]
i = 0
# execute parser
parser()
