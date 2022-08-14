def read_fsa_files(files):
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


def con(arr):
    return arr[0]


TABLE = [
    #    i    +    *   (    )    $
    [0, -1, -1, 0, -1, -1],  # E
    [-1, 1, -1, -1, 2, 2],  # P
    [3, -1, -1, 3, -1, -1],  # T
    [-1, 5, 4, -1, 5, 5],  # G
    [6, -1, -1, 7, 0, 0],  # F
]


def ll1_parser(data):
    Table_input = data[3]
    Rules_input = con(data[2])
    String_input = con(data[4])
    NT_inputs = con(data[1])
    T_inputs = con(data[0])
    memory = []
    memory.append('$')
    memory.append(NT_inputs[0])
    last_index = len(String_input)-1
    invalid_flag = False
    for ip in String_input:
        while ip != memory[-1]:
            row = NT_inputs.index(memory[-1])
            col = T_inputs.index(ip)
            production = TABLE[row][col]
            if production == -1:
                print("invalid production")
                invalid_flag = True
                break
            production = Rules_input[production]
            if production == "EPSILON":
                memory.pop()
                continue
            production_list = list(production)
            production_list.reverse()
            memory.pop()
            for x in production_list:
                memory.append(x)

        if invalid_flag == True:
            break
        if ip == "$" and memory[-1] == "$":
            print("parsed")
        memory.pop()


table_files = ["terminals.txt", "non_terminals.txt",
               "productions.txt", "table.txt", "input.txt"]
data = read_fsa_files(table_files)
ll1_parser(data)
