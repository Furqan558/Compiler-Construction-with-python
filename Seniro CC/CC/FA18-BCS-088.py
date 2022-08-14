import keyword
R = open("zzz.txt", "r")
Reserve_words = ["elif", "in", "try", "and", "else", "is", "while", "as", "except", "False", "def", "if",
                 "raise", "None", "del", "import", "return", "True" "lambda","with","assert","finally"
                  ,"nonlocal","yield","break","for","not","class","from","or","continue","global","pass"]
Arithmatic_Operators =  ('+', '-', '*', '=', '==', '<=', '>=', '<', '>', '/')
Logical_Operators = ['&&', '||', '!']


Digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
String = str(R.readlines())
print(String)
String = String.replace('[', '').replace(']', '').replace('\\n', '').replace("'", '')
print("check",String)
String = String.split("'*'|'-'|''|'/'|'+'|'='|'=='|'<='|'=>'|'<'|'>'")
print("spilt")
print(String)

data1=['$']
data=['$']

for i in String:
    space = ""
    for k in i:
        if k != ' ':
            space = space + k

        elif (space.isidentifier()) == True:
            if keyword.iskeyword(space):
                print("")

                space = ""
            else:
                print("Identifier===========------> ", space, end="")
                print()
                data.append('i')
                space = ""

        if (space in Reserve_words) == True  :
            print("Key_words============------> ", space, end="")
            print()
            space= ""


        elif (space in Logical_Operators) == True  :
            print("Logical Operators=======----> ", space, end="")
            print()
            space= ""
        elif (space in Arithmatic_Operators) == True:
            print("Arithmetic Operator=====----> ", space, end="")
            if space=='+':
                data.append('+')
            elif space=='*':
                data.append('*')
            print()
            space = ""


        elif (k in Digits)==True or k == ' ':
            Counter=0
            for x in k:
                if x>='0' and x<='9':
                    Counter=2
                else:
                    Counter=0
                    break
            if Counter==2:
                print("Digit----> ", space, end="")
                print()
            space= ""

print(data)

parse = [['_','i','+','*','$'],['i','_','>','>','>'],['+','<','>','<','>'],['*','<','>','>','>'],['$','<','<','<','_']]

print(data1)
l=0
while len(data)!=l:

    r=0
    while data[len(data)-1]!= parse [r] [0]:
        r= r+1

    c=0
    while data1[len(data1)-1] != parse [0] [c]:
        c= c+1

    if parse[r][c] == '>':
        data1.append(data[len(data)-1])
        data.pop()
        print(data1)
    else:
        data1.pop()
        print(data1)
    l+=1

print("Buffers Parsed")