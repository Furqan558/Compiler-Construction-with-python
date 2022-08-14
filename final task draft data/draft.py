def read_fsa_table(filename_list):
    all_fsa_table = []
    all_fsa_char = []
    for x in filename_list:
        file = open(x, "r")
        lines = file.readlines()
        file.close()
        lines = [x.replace("\n", "").split('\t') for x in lines]
        characters = {x[1] for x in lines}
        all_fsa_table.append(lines)
        all_fsa_char.append(characters)
    return all_fsa_table, all_fsa_char


def read_input(filename):
    file = open(filename)
    data = file.readline()
    file.close()
    return data.split()


def fsm_in_parallel(all_lines, all_characters, input_list, e_states):
    for j in input_list:
        print("Processing String: ", j)
        input_lexeme_list = list(j)
        s_state = "0"
        current_states = [{s_state} for i in range(len(all_lines))]

        for char in input_lexeme_list:

            for fsa in range(len(all_lines)):

                print(f"fsa{fsa+1} current state: ", current_states[fsa])
                print("input processing: ", char)
                next_states = set()
                for current_state in current_states[fsa]:

                    for y in all_lines[fsa]:

                        if(y[0] == current_state and y[1] == char):
                            next_states.add(y[2])

                print("next states: ", next_states, "\n...")
                current_states[fsa] = next_states

        for i in range(len(all_lines)):
            isAccepted = False
            for x in current_states[i]:
                if x in e_states[i]:
                    isAccepted = True
                    break
            print(
                f"~~~~~~~~~~~~~~~~~~FSA{i+1} string accepted!~~~~~~~~~~~~~~~~~~~" if isAccepted else f"~~~~~~~~~~~~~~~FSA{i+1} string rejected!~~~~~~~~~~~~~~~~~")


files = ["fsa1.txt", "fsa2.txt"]
all_lines, all_characters = read_fsa_table(files)
print(all_lines, all_characters)
input_list = read_input("input_tests.txt")
end_states = [["3", "4"], ["2"]]

fsm_in_parallel(all_lines, all_characters, input_list, end_states)
