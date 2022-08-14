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
    table = []
    converted = []
    f = open(table_file, "r")
    lines = f.readlines()
    for line in lines:
        line.replace("\n", "")
        table.append(line.split())

    for x in table:
        lis = []
        for y in x:
            lis.append(int(y))
        converted.append(lis)
    f.close()
    return converted


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


def ll1_parser(data, Table_input):
    Rules_input = con(data[2])
    String_input = con(data[3])
    NT_inputs = con(data[1])
    T_inputs = con(data[0])
    record = []
    record.append('$')
    record.append(NT_inputs[0])
    # last_index = len(String_input)-1
    invalid_flag = False
    for ip in String_input:
        while ip != record[-1]:
            row = NT_inputs.index(record[-1])
            col = T_inputs.index(ip)
            production = Table_input[row][col]
            if production == -1:
                print("invalid production")
                invalid_flag = True
                break
            production = Rules_input[production]
            if production == "EPSILON":
                record.pop()
                continue
            production_list = list(production)
            production_list.reverse()
            record.pop()
            for x in production_list:
                record.append(x)

        if invalid_flag == True:
            break
        if ip == "$" and record[-1] == "$":
            print("parsed")
        record.pop()


other_files = ["terminals.txt", "non_terminals.txt",
               "productions.txt", "input.txt"]
data = read_files(other_files)
table = read_table("table.txt")
ll1_parser(data, table)
