LIST =[]
Input=[]
with open ('S_Input.txt') as file:
    data=file.readlines()
    for line in data:
        line = line.rstrip()
        LIST.append(line)
    for value in LIST:
        for char in value:
            Input.append(char)
        

Rules=[]
with open ('S_Rules.txt') as file:
    data=file.readlines()
    for line in data:
        line = line.rstrip().split()
        Rules.append(line)
    
print("############## Symantic Functions #################\n",Rules)

    
# =================== Grammer Part ====================
print("\n############## Grammer #################\n")

# Grammer 
Grammer=[]
with open('S_Grammer.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        Grammer.append(line)
print("\nGrammer  ----",Grammer)


# ================= Tables ================
print("\n############## Table  ##################")

# Table 
table=[]
with open('Symantic_Table.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        table.append(line)

for i in table:
    print(i)
print("\n############## User INPUT ####################\n",Input)



# ================= Lexical Analyzer ================
Buffer= []

for i in Input:
    if i.isdigit() == True:
        Buffer.append('d')  
    else:
        Buffer.append(i)
        
Buffer.append('$')
print("Buffer = ",Buffer)        
  

# ================= Parsing ================
print("\n############ Parser ##############\n")
A = 0
chk=False
Stack=['$','0']
Symbol_value=[]
temp=(Buffer[A],Input[A])
Symbol_value.append(temp)
print("Initial Stack = ",Stack)
# loop on input
while(A < len(Buffer)):
    if chk:
        break
    if Stack[-1] not in 'ETF':
        if Buffer[A] in table[0]:
            
            print("Symbol ",Symbol_value)
            #Index of input within the Table
            index = table[0].index(Buffer[A])
            # Top Most value of Stack
            Stack_value = Stack[-1]
            
            for i in table:
                # i = each row of grammer , i[0] = first value of each row(i)
                if Stack_value == i[0]:
                
                    table_value = i[index]

                    print("\nTable Value = ",table_value)
                    # Table Value for Non Terminal
                    if table_value.isdigit() == True:
                        Stack.append(Buffer[A])
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
                            Stack.append(Buffer[A])
                            Stack.append(char_2)
                            print("Stack = ",Stack)
                            A=A+1
                        # Reduce Case
                        elif char_1 == 'R':
                            PRV= Grammer[int(char_2)-1][1]         #Production Right Value
                            #PLV= Grammer[int(char_2)-1][0]         #Production Left Value
                            print("Production Value = ",PRV)
                            pop_value = len(PRV) * 2
                            print("Pop Value = ",pop_value)
                            print("Stack = ",Stack)
                            for i in range(pop_value):
                                Stack.pop()
                            #Stack.append(PLV)
                            production=Rules[int(char_2)-1]
                            if len(production)==3:
                                NT_value_first=production[0].split('.')[0]      #Taking First value
                                #print(NT_value_first)

                                NT_value_third=production[2].split('.')[0]      #Taking Third Value
                                #print(NT_value_third)

                                for i in range(len(Symbol_value),0,-1):
                                    if NT_value_third in Symbol_value[i-1][0]:
                                        val= Symbol_value[i-1][1]
                                        Stack.append(NT_value_first)
                                        Symbol_value.append((NT_value_first,val))
                                        break
                            elif len(production) ==5:
                                NT_value_first=production[0].split('.')[0]      #Taking First value
                                #print(NT_value_first)

                                NT_value_third=production[2].split('.')[0]      #Taking Third Value
                                #print(NT_value_third)

                                NT_value_fourth=production[3].split('.')[0]      #Taking First value
                                #print(NT_value_fourth)

                                NT_value_fifth=production[4].split('.')[0]      #Taking Third Value
                                #print(NT_value_fifth)

                                temp=[]

                                for i in range(len(Symbol_value),0,-1):
                                    if NT_value_third in Symbol_value[i-1][0]:
                                        #Accessing value of var
                                        val= Symbol_value[i-1][1]
                                        temp.append(int(val))
                                        break

                                for i in range(len(Symbol_value),0,-1):
                                    if NT_value_fifth in Symbol_value[i-1][0]:
                                        val= Symbol_value[i-1][1]
                                        temp.append(int(val))
                                        break

                                if NT_value_fourth == '+':
                                    sol=sum(temp)
                                    #Appending first value
                                    Stack.append(NT_value_first)
                                    #Appending Symbol and its value 
                                    Symbol_value.append((NT_value_first,str(sol)))
                                    
                                elif NT_value_fourth == '*':
                                    sol=1               # For Taking Product
                                    for i in temp:
                                        sol=sol*i
                                    #Appending first value
                                    Stack.append(NT_value_first)
                                    #Appending Symbol and its value 
                                    Symbol_value.append((NT_value_first,str(sol)))
                                    print("Stack ",Stack)
                                    print("Symbol value ",Symbol_value)
                
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

