# Reading tables from files for NFA
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
        lk_check = 0
        temp_ip = ""
        for id, current_character in enumerate(sample_input):
            # lookahead

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

                # if lk_check == 0 and (current_character != sample_input[-1] or current_character != sample_input[-2]):
                #     lk_index = sample_input.index(current_character)
                #     identifier = current_character + sample_input[lk_index+1]
                #     print("this is with single lookahead", identifier)
                # if lk_check == 1 and current_character != sample_input[-2]:
                #     lk_index = sample_input.index(current_character)
                #     identifier = current_character + \
                #         sample_input[lk_index+1] + sample_input[lk_index+2]
                #     print("this is with double lookahead", identifier)
                # if identifier in operators_1 and lk_check == 0:
                #     print("operator without lookahead", identifier)
                #     lk_check = 1
                #     T.append(identifier)
                #     continue
                # elif current_character in operators_1 and lk_check == 0:
                #     print("operator dected:!", current_character)
                #     T.append(current_character)
                #     continue
                # elif lk_check == 1 or lk_check == 2:
                #     continue
                # else:
                #     lk_check = 0
            for i in range(len(fsa_tables)):
                if current_character not in characters_all[i]:
                    fsa_flags[i] = False
                    if fsa_flags[i] == False:
                        continue
                    print(f"<----------------- FSA {i+1} -------------->")
                    print("current state = ", current_state[i])
                    print("Input processing = ", current_character)
                    next_state = set()
                    # print(fsa_tables)
                    for my_state in current_state[i]:
                        for current_condition in fsa_tables[i]:
                            # if current_character in fsa_tables[i]:
                            if my_state == current_condition[0] and current_character == current_condition[1]:
                                next_state.add(current_condition[2])

                    print("Next state will be = ", next_state)
                    current_state[i] = next_state
        for j in range(len(fsa_tables)):
            if fsa_flags[j] == False:
                print(f"FSA{j+1} rejected --invalid character--")
            else:
                for x in current_state[j]:
                    found1 = 0
                    print("x", x)
                    if x in termination_states[j]:
                        found1 = 1
                        print(f"\nFSA{j+1} This string is accepted as last state was : ",
                              current_state[j])
                        if j == 0:
                            T = T+"i"
                        if j == 1:
                            T = T+"i"

                    if found1 == 0:
                        print(f"\nFSA{j+1} This string is rejected as last state should be : ",
                              termination_states[j])
        print(fsa_flags)
    print(T)


def main():
    table_files = ["identifier.txt"]
    inputs = read_inputs("input.txt")
    fsa_tables = read_fsa_files(table_files)
    characters_all = get_all_characters(table_files)
    fsa_handling(fsa_tables, inputs, characters_all)


main()
