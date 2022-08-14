LIST =[]
Input=[]
with open ('Input.txt') as file:
    data=file.readlines()
    for line in data:
        line = line.rstrip()
        LIST.append(line)
    for value in LIST:
        for char in value:
            Input.append(char)
        

Numbers =['0','1','2','3','4','5','6','7','8','9']
Operators =['+','-','*','=','<','>','/']
Terminal_Symbols = ['a','b','c','d','n']
Alphabets =['A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N',
               'O','P','Q','R','S','T','U',
               'V','W','X','Y','Z']

# =================== Grammer Part ====================
print("############## Grammer #################\n")

# Grammer No 1 
Grammer1=[]
with open('Grammer1.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        Grammer1.append(line)
print("\nGrammer 1 ----",Grammer1)

# Grammer No 2
Grammer2=[]
with open('Grammer2.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        Grammer2.append(line)
print("\nGrammer 2 ----",Grammer2)
# Grammer No 3 
Grammer3=[]
with open('Grammer3.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        Grammer3.append(line)
print("\nGrammer 3 ----",Grammer3)

# ================= Tables ================
print("\n############## Table 1 #################")

# Table No 1 
table1=[]
with open('Table1.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        table1.append(line)

for i in table1:
    print(i)

print("\n############## Table 2 #################")

# Table No 2
table2=[]
with open('Table2.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        table2.append(line)
for i in table2:
    print(i)

print("\n############## Table 3 #################")

# Table No 3 
table3=[]
with open('Table3.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        table3.append(line)
for i in table3:
    print(i)

# ================= Lexical Analyzer ================
buffer1=[]
buffer2=[]
buffer3=[]
NT_Symbols=[]       #Non Terminal Symbols

for i in Input:
    if i in Terminal_Symbols or i in Operators or i in Numbers:
        for list_ in Grammer1:
            for item in list_:
                #For tokenizing Non Terminal Symbols in Grammer 1
                if item in Alphabets and item not in NT_Symbols:
                    NT_Symbols.append(item)
                #For tokenizing Terminal Symbols in Grammer 1
                if i in item:
                    buffer1.append(i)
                
        for list_2 in Grammer2:
            for item in list_2:
                #For tokenizing Non Terminal Symbols in Grammer 2
                if item in Alphabets and item not in NT_Symbols:
                    NT_Symbols.append(item)
                #For tokenizing Terminal Symbols in Grammer 2   
                if i in item:
                    buffer2.append(i)
    
        for list_3 in Grammer3:
            for item in list_3:
                #For tokenizing Non Terminal Symbols in Grammer 3
                if item in Alphabets and item not in NT_Symbols:
                        NT_Symbols.append(item)
                #For tokenizing Terminal Symbols in Grammer 3        
                if i in Numbers and item in 'n':    #If i is num
                    buffer3.append(i)
                elif i in '+*':
                    buffer3.append(i)       #i will be * or +


                        

print("\n############## User INPUT ####################\n",Input)
print("\n############ Input Buffer Values ##############\n")
print("Input Buffer 1 ----> \t",buffer1)
print("Input Buffer 2 ----> \t",buffer2)
print("Input Buffer 3 ----> \t",buffer3)

# ================= Parsing Function ================
def Parser(Input_buffer,table,Production):
    A = 0
    chk=False
    Stack=['$','0']
    print("Initial Stack = ",Stack)
    # loop on input
    while(A < len(Input_buffer)):
        if chk:
            break
        if Stack[-1] not in NT_Symbols:
            if Input_buffer[A] in table[0]:
                #Index of input within the Table
                index = table[0].index(Input_buffer[A])
                # Top Most value of Stack
                Stack_value = Stack[-1]
                
                for i in table:
                    # i = each row of grammer , i[0] = first value of each row(i)
                    if Stack_value == i[0]:
                    
                        table_value = i[index]

                        print("\nTable Value = ",table_value)
                        # Table Value for Non Terminal
                        if table_value.isdigit() == True:
                            Stack.append(Input_buffer[A])
                            Stack.append(table_value)
                            

                        # Table value for $
                        elif table_value == 'Accept':
                            print("Input is Parsed Successfully!!!")
                            chk=True
                            break    
                        elif table_value == '-':
                            print("Input is Invalid ---NOT Parsed")
                            chk=True
                            break

                            # Check for Shift and Reduce Case
                        else: 
                            char_1 = table_value[0]     # Alphabet value i.e. S or R
                            char_2 = table_value[1]     # Digit value with S or R

                            # Shift Case
                            if char_1 == 'S':
                                # append above index into the stack
                                Stack.append(Input_buffer[A])
                                Stack.append(char_2)
                                print("Stack = ",Stack)
                                A=A+1
                            # Reduce Case
                            elif char_1 == 'R':
                                #if 'num' in PRV


                                PRV= Production[int(char_2)][1]         #Production Right Value
                                PLV= Production[int(char_2)][0]         #Production Left Value
                                print("Production Value = ",PRV)
                                pop_value = len(PRV) * 2
                                print("Pop Value = ",pop_value)
                                print("Stack = ",Stack)
                                for i in range(pop_value):
                                    Stack.pop()
                                Stack.append(PLV)
                    
            else:
                print("Input is Invalid ---NOT Parsed")
                chk=True
                break
        else:
             index_1 = table[0].index(Stack[-1])  #Stack[-1] is Non Terminal Symbol
             for i in table:
                 if i[0] == Stack[-2]:          #Stack[-2] is state value
                    value= i[index_1]           #Store the value w.r.t Symbol and State

             if value == '-':
                 print("Input is Invalid ---NOT Parsed")
                 break
             else:
                Stack.append(value)
                print("Updated Stack = ",Stack)
        
             
    print("\n\n======= Final Stack =========\n",Stack)


# ================= Calling Parser ================
count=3             
if len(buffer1) > 0:
    print("\n\t================ Parser for Buffer 1 =====================")
    buffer1.append('$')
    print("Input Buffer = ",buffer1)
    Parser(buffer1,table1,Grammer1)
else:
    count=count-1

if len(buffer2) > 0:
    print("\n\t================ Parser for Buffer 2 =====================")
    buffer2.append('$')
    print("Input Buffer = ",buffer2)
    Parser(buffer2,table2,Grammer2)
else:
    count=count-1

if len(buffer3) > 0:
    print("\n\t================ Parser for Buffer 3 =====================")
    buffer3.append('$')
    print("Input Buffer = ",buffer3)
    Parser(buffer3,table3,Grammer3)
else:
    count=count-1
if count ==0:
    print("All the Buffers are Empty\n----INPUT is INVALID ----")


