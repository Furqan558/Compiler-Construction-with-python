# 0 0 0
# 0 1 1
# 1 0 2
# 1 1 1
# 2 1 3
# 2 0 0
# 3 1 1
# 3 0 2

# Your program should save this file data in to data structure, and then process input character by
# character, for example input is 1101, you program should output like following.
# Current State = 0
# Input processsing = 1
# Next State = 1
# Current state = 1
# InputProcessing = 1
# Next state = 1
# Current state = 1
# Input processing = 0
# Next state = 2
# Current state = 2
# Input processing = 1
# Next state =3
# String Accepted

f = open("task.txt", "r")
fsa_conditions = []
with open("task.txt", "r")as file:
    for line in file:
        fsa_conditions.append(line.strip())

print(fsa_conditions)

current_state = "0"               # start state
next_state = "0"                  # will store next state here for iteration
termination_state = "3"           # end state
sample_input = list(input("Please Input Number :"))
# print(fsa_conditions[0][2])
print("Sample input is : ", sample_input)
print("Starting state is : ", current_state)
print("termination state will be : ", termination_state)

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
    print("This string is accepted as last state was : ", next_state)
else:
    print("This string is rejected as last state should be : ", termination_state)

# f.close()
