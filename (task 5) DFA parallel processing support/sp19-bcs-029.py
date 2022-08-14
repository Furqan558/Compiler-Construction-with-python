# Generic Program for FSA

# Reading file for NFA
f = open("fsa1.txt", "r")
fsa1_conditions = []
with open("fsa1.txt", "r")as file:
    for line in file:
        fsa1_conditions.append(line.strip())
f.close()

# Reading file for DSA
f = open("fsa2.txt", "r")
fsa2_conditions = []
with open("fsa2.txt", "r")as file:
    for line in file:
        fsa2_conditions.append(line.strip())
f.close()
# Reading Inputs
all = open("inputs.txt", "r")
all_strings = all.readline()
all_strings = all_strings.split()

current_states1 = {"0"}               # start state
found1 = 0
termination_state1 = ["3", "4"]           # end state

current_states2 = {"0"}               # start state
found2 = 0
termination_state2 = ["2"]           # end state

# print("Starting state is : ", current_states)
# print("termination state will be : ", termination_state)

for sample_input in all_strings:
    print("\n---------------------------Sting starts here---------------------------\n")
    print(sample_input)
    current_states1 = {"0"}
    current_states2 = {"0"}
    for current_character in sample_input:
        print("<----------------- FSA 1 -------------->")
        print("current state = ", current_states1)
        print("Input processing = ", current_character)
        next_state = set()
        for my_state in current_states1:

            for current_condition in fsa1_conditions:

                if my_state == current_condition[0] and current_character == current_condition[2]:

                    next_state.add(current_condition[4])
        print("Next state will be = ", next_state)
        current_states1 = next_state

        print("<----------------- FSA 2 -------------->")
        print("current state = ", current_states2)
        print("Input processing = ", current_character)
        next_state = set()
        for my_state in current_states2:

            for current_condition in fsa2_conditions:

                if my_state == current_condition[0] and current_character == current_condition[2]:

                    next_state.add(current_condition[4])
        print("Next state will be = ", next_state)
        current_states2 = next_state
        # break
        # print("\n\n")
    for x in current_states1:
        if x in termination_state1:
            found1 = 1
            print("\nThis string is accepted as last state was : ", current_states1)
    if found1 == 0:
        print("\nThis string is rejected as last state should be : ",
              termination_state1)
    for x in current_states2:
        if x in termination_state2:
            found2 = 1
            print("\nThis string is accepted as last state was : ", current_states2)
    if found2 == 0:
        print("\nThis string is rejected as last state should be : ",
              termination_state2)

# f.close()
