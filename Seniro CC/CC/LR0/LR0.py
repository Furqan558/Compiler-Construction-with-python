# Imlimentaion of LR-0 Parser
# main grammer table
grammer=[[' ','a','b','$','A','S'],
         ['0','S3','S4',' ','2','1'],
         ['1',' ',' ','Accept',' ',' '],
         ['2','S3','S4',' ','5',' '],
         ['3','S3','S4',' ','6',' '],
         ['4','R3','R3','R3 ',' ',' '],
         ['5','R1','R1','R1 ',' ',' '],
         ['6','R2','R2','R2 ',' ',' '],
         ]

# set of productions
Production  =  [['S-','S'],['S','AA'],['A','aA'],['A','b']]

# input buffer
Input=['a','a','b','b','$']
# initial stack
Stack=['$','0']
A = 0
chk=False
# loop on input
while(A < len(Input)):
    if chk:
        break
    if Stack[-1] not in "AS":
        if Input[A] in grammer[0]:
            # here I am finding the index of input within the grammer of zero ---> grammer[0]
            index = grammer[0].index(Input[A])
            # access the second last Input[A] of the stack such as (0) from inital stack, in order
            # to access the Input[A] crossponding to A and 0 --> 2 (Input[A])
            Stack_value = Stack[-1]

            # append table's Input[A] to the stack
            for i in grammer:
                # i = each row of grammer , i[0] = first value of each row(i)
                if Stack_value == i[0]:
                
                    table_value = i[index]

                    print("Table Value ",table_value)
                    # check that the number is digit, if yes then append it as it is
                    if table_value.isdigit() == True:
                        Stack.append(Input[A])
                        Stack.append(table_value)
                        

                        # if table Input[A] is "accept" then print the acceptance Input[A] and break the loop
                    elif table_value == 'Accept':
                        print("Input is Parsed Successfully")
                        chk=True
                        break    
                    elif table_value == ' ':
                        print("Input in Invalid")
                        chk=True
                        break

                        # if Input[A] is not ''digit'' and not ''accept'' then go for S(1,2,3,4) and R(1,2,3)
                    else:
                        # first and second character of S(1,2,3,4) or R(1,2,3) 
                        char_1 = table_value[0]
                        char_2 = table_value[1]
                        # if character is "S" the append the second character as it is
                        # and if character is "R" then count the second character's length and then multiply by 2
                        # after multiply by 2 , pop resulted number of Input[A]s from the stack
                        if char_1 == 'S':
                            # append above index into the stack
                            Stack.append(Input[A])
                            Stack.append(char_2)
                            print(Stack)
                            A=A+1
                        elif char_1 == 'R':
                            pop_value = len(Production[int(char_2)][1]) * 2
                            print(pop_value)
                            print(Stack)
                        
                            for i in range(pop_value):
                                Stack.pop()
                            Stack.append(Production[int(char_2)][0])
                
        else:
            print("Input is Invalid")
            chk=True
            break
    else:
         index_1 = grammer[0].index(Stack[-1])  #Stack[-1] is Non Terminal Symbol
         for i in grammer:
             if i[0] == Stack[-2]:          #Stack[-2] is state value
                value= i[index_1]           #Store the value w.r.t Symbol and State

         if value == ' ':
             print("Input is Invalid")
             break
         else:
            Stack.append(value)
            print(Stack)
    
         
print("Final Stack: ",Stack)
        

