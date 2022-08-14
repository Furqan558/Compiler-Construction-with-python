#List of Arithmetic Operators in Python
Python_Arithmetic=['+','-','*','=','==','<=','>=','<','>','/']

#List of Numbers in Python
Numbers=['0','1','2','3','4','5','6','7','8','9']

#List of Keywords in Python 
Python_Keywords=['print','False','else','import','None','break','in','True','class','is','return','and','for','as','def','from','while','not','elif','if','or']

#List of Separators in Python
Separators=[" ",'\n','(',')',',',':']

#Read Source File
List=[]
file = open("src.txt","r")
List = file.readlines()
print("Source :",List )
print("###### Text ########\t\t\t##### Tokens #####")

Numbers_List= []
Keywords_List = []
Arithmetic_List= []
Identifier_List = []
FloatNumbers_List = []

#Checking the Text in Source File
###Important
# Note: Arthmetic symbols should be written with space (before and after) in the source file otherwise Arithmetic symbols will not be considered!!!  

for x in List :
    token = ''
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
                token = token + y
        else :
            if len(token)> 0 :
                if token in Python_Keywords:
                    print(token,"\t\t\t\t\t Keyword")
                    Keywords_List.append(token)
                    token = ''
                    print('\n')
                
                elif token[0] in Numbers or token[0] == '.' :
                    if '.' in token :
                        print(token,"\t\t\t\t\t Floating Point Number")
                        FloatNumbers_List.append(token)
                        token = ''             
                        print('\n')
                    else :
                        print(token,"\t\t\t\t\t Number")
                        Numbers_List.append(token)
                        token = ''
                        print('\n')
                    
                elif token in Python_Arithmetic :
                    print(token,"\t\t\t\t\t Arithmetic Operator")
                    Arithmetic_List.append(token)
                    token = ''
                    print('\n')
                else :
                    print(token, "\t\t\t\t\t Identifier")
                    Identifier_List.append(token)
                    token = ''
                    print('\n')


buffer= []
for item in Arithmetic_List:
        if item=='*' or item=='+':
            buffer.append(item)
buffer.append('$')    
print("Buffer = ",buffer)
BUFFER = ['id','+','id','*','id','$']
    

# Operational Precedence Table With  Indexes
Operational_Precedence_Table2 = [['-','id','+','*','$'],['id','-','>','>','>'],['+','<','>','<','>'],['*','<','>','>','>'],['$','<','<','<','-']]
Operational_Precedence_Table = [['-','>','>','>'],['<','>','<','>'],['<','>','>','>'],['<','<','<','-']]
#Given id M A $
PrecedenceValues = {'id':1 , '*':2 , '+':3 , '$':4}

Stack = []
Stack.append('$')
print("######################################################################")
print("Operational Precedence Table  = ",Operational_Precedence_Table)
print("\n######################################################################")
print("Initial Stack",Stack)
print("\n######################################################################")

# required buffer entries
Required_Buffer_Entries = list() # to store unique values
for row in Operational_Precedence_Table2:
    for item in row :
        if item != '-' and item!='<' and item!='>' and item!='$':
            Required_Buffer_Entries.append(item)
# again convert it into the list to access
Required_Buffer_Entries.append('$')
ToList = []
for i in Required_Buffer_Entries:
    if i not in ToList:
            ToList.append(i)

# iterate through bufffer and searching through stack
print("Terminal Symbols  = ",ToList)


