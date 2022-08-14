# Generic Program for FSA
f = open("table.txt", "r")
fsa_conditions = []
with open("table.txt", "r")as file:
    for line in file:
        fsa_conditions.append(line.strip())

all = open("test_strings.txt", "r")
all_strings = all.readline()
all_strings = all_strings.split()
current_state = "a"               # start state
next_state = "a"                  # will store next state here for iteration
termination_state = "b"           # end state
print("Starting state is : ", current_state)
print("termination state will be : ", termination_state)
for sample_input in all_strings:
    print("\n---------------------------Sting starts here---------------------------\n")
    print(sample_input)
    current_state = "a"
    for current_integer in sample_input:
        for current_condition in fsa_conditions:
            if current_state == current_condition[0] and current_integer == current_condition[2]:
                print("current state = ", current_state)
                print("Input processing = ", current_integer)
                next_state = current_condition[4]
                print("Next state will be = ", next_state)
                current_state = next_state
                break
                # print("\n\n")
    if next_state == termination_state:
        print("\nThis string is accepted as last state was : ", next_state)
    else:
        print("\nThis string is rejected as last state should be : ",
              termination_state)

# f.close()
