# Reading tables from files for NFA


def read_fsa_files(files):
    fsa_tables = []

    for i in files:
        table = []
        f = open(f"{i}", "r")
        lines = f.readlines()
        for line in lines:
            line.replace("\n", "")
            table.append(line.split())
        fsa_tables.append(table)
        f.close()
    return fsa_tables


def read_inputs(input_filename):
    f = open(input_filename, "r")
    inputs = f.readline()
    inputs = inputs.split()
    f.close()
    return inputs


def fsa_handling(fsa_tables, inputs):
    termination_states = [{"3", "4"}, {"2"}]
    for sample_input in inputs:
        print("\n---------------------------Sting starts here---------------------------\n")
        print(sample_input)
        current_state = [{"0"}, {"0"}]

        for current_character in sample_input:

            for i in range(len(fsa_tables)):
                print(f"<----------------- FSA {i} -------------->")
                print("current state = ", current_state[i])
                print("Input processing = ", current_character)
                next_state = set()
                for my_state in current_state[i]:

                    for current_condition in fsa_tables[i]:

                        if my_state == current_condition[0] and current_character == current_condition[1]:
                            next_state.add(current_condition[2])
                print("Next state will be = ", next_state)
                current_state[i] = next_state
        for j in range(len(fsa_tables)):
            for x in current_state[j]:
                if x in termination_states[j]:
                    found1 = 1
                    print("\nThis string is accepted as last state was : ",
                          current_state[j])
                if found1 == 0:
                    print("\nThis string is rejected as last state should be : ",
                          termination_states[j])


table_files = ["fsa1.txt", "fsa2.txt"]
inputs = read_inputs("inputs.txt")
fsa_tables = read_fsa_files(table_files)
fsa_handling(fsa_tables, inputs)
# print(inputs)
# print(fsa_tables)
