# =================== Input ====================
print("############## Input #################\n")
Input=[]
with open('Input.txt') as file:
    user_input = file.readlines()
    for line in user_input:
        line = line.rstrip().split()
        Input.append(line)
print(Input)

# =================== Table ====================
print("\n############## Table #################")
 
table=[]
with open('table.txt') as file:
    data = file.readlines()
    for line in data:
        line = line.rstrip().split()
        table.append(line)
for i in table:
    print(i)

# =================== Grammer ====================    
print("\n############## Grammer #################")
Non_Terminal=['S','X','Y','D','N','P','A','M','V','Q','G','R']
Python_Arithmetic=['+','-','*','=','==','<=','>=','<','>','/']
Numbers=['0','1','2','3','4','5','6','7','8','9']
Python_Keywords=['print','False','else','import','None','break','in','True','class','is','return','and','for','as','def','from','while','not','elif','if','or']
Separators=[" ",'\n','(',')',',',':']
Production  =  [['X','DN'],['X','P'],['N','AN'],['N','M'],['Y','VA'],['Y','VX'],['Y','VS'],['Y','VXQ'],['G','RX'],['P','buster'],['P','chatter'],['P','joe'],['D','the'],['D','a'],['M','bear'],['M','squirrel'],['M','tree'],['M','fish'],['M','fog'],['A','angry'],['A','frightened'],['A','little'],['A','tall'],['V','chased'],['V','saw'],['V','said'],['V','thought'],['V','was'],['V','put'],['R','or']]
count=1
for i in Production:
    print("Production ",count," -------",i)
    count+=1

# ================= Lexical Analyzer ================

Finalized_input=[]
print("\n############## Lexical Analyzer #################")
print("\n###### Text ########\t\t\t##### Tokens #####\n")

for x in user_input :
    tkn = ''
    checker = False
    check_count = 0
    for y in x:
        if y not in Separators :
            if y == '"' or checker == True:
                checker = True
                check_count = check_count + 1
                if check_count > 1 and y == '"' :
                     checker = False
            else :
                tkn = tkn + y
        else :
            if len(tkn)> 0 :
                if tkn in Python_Keywords:
                    print(tkn,"\t\t\t\t\t Keyword")
                    tkn = ''
                    print('\n')
                    
                elif tkn in Python_Arithmetic :
                    print(tkn,"\t\t\t\t\t Arithmetic Operator")
                    tkn = ''
                    print('\n')
                else :
                    print(tkn, "\t\t\t\t\t String")
                    Finalized_input.append(tkn)
                    tkn = ''
                    print('\n')


input_buffer=[]
for i in Finalized_input:
    if i not in Python_Arithmetic or Numbers:
        for list_ in Production:
            for item in list_:
                if i in item:
                    input_buffer.append(i)
input_buffer.append("$")
print("Finalized Input ----->",input_buffer)

# ================= Parser ================
print("\n############## Parser #################")
stk=["$","0"]
A = 0
chk=False
counter = 1

while(A < len(input_buffer)):
    if chk:
        break
    if stk[-1] not in Non_Terminal:
        if input_buffer[A] in table[0]:
            index = table[0].index(input_buffer[A])
            stk_value = stk[-1]
            for i in table:
                if stk_value == i[0]:
                    value = i[index]
                    print("\nIteration No = ",counter)
                    print("\nInput Value = ",input_buffer[A])
                    print("Table Value ",value)
                    if value.isdigit() == True:
                        stk.append(input_buffer[A])
                        stk.append(value)
                        
                    elif value == "A":
                        print(" Succeed ")
                        print("\nInput is Parsed Successfully")
                        chk=True
                        break    
                    elif value == "-":
                        print("\nInput is Invalid")
                        chk=True
                        break                        
                    else:
                        if len(value)==2:
                            Element_1 = value[0]
                            Element_2 = value[1]                          
                            if Element_1 == "S":
                                stk.append(input_buffer[A])
                                stk.append(Element_2)
                                print(stk)
                                A=A+1
                            elif Element_1 == "R":                               
                                if Production[int(Element_2)-1][1].isupper() == True:
                                    pop_value = len(Production[int(Element_2)-1][1]) * 2
                                    print("\nReduce ",Production[int(Element_2)-1][1]," with ",Production[int(Element_2)-1][0])
                                    print("\nPop Value = ",pop_value)
                                    print(stk)                          
                                    for i in range(pop_value):
                                        stk.pop()
                                    stk.append(Production[int(Element_2)-1][0])
                                    
                                elif Production[int(Element_2)][1].islower() == True:
                                    pop_value = 2
                                    print("\nPop Value = ",pop_value)
                                    print(stk)
                                
                                    for i in range(pop_value):
                                        stk.pop()
                                    
                                    stk.append(Production[int(Element_2)-1][0])
                                    
                        elif len(value)>2:
                            
                            Element_1 = value[0]
                            Element_2 = value[1:]
                            
                            if Element_1 == "S":
                                stk.append(input_buffer[A])
                                stk.append(value[1:])
                                print(stk)
                                A=A+1
                            elif Element_1 == "R":
                                pop_value = 2
                                print("Reduce ",Production[int(Element_2)-1][1]," with ",Production[int(Element_2)-1][0])
                                print("Pop Value = ",pop_value)
                                print(stk)
                            
                                for i in range(pop_value):
                                    stk.pop()
                                stk.append(Production[int(Element_2)-1][0])
                                print("After pop ",stk)
                              
                
        else:
            print("Input is Invalid")
            chk=True
            break
    else:

        print("\nIteration No = ",counter)
        index_1 = table[0].index(stk[-1])  
        
        for i in table:
            if i[0] == stk[-2]:          
                value= i[index_1]           
                print("Table Value ",value)
        if value == '-':
            print("Input is Invalid")
            break
        
        else:
            stk.append(value)
            print(stk)
        
    
    counter = counter + 1
print("Final stack : ",stk)
        
