# FA18-BCS-048_7A
# Accept for this
# int a = b+d

# Reject for this input 
# int a = b + d

# Because it includes space which act as token seperator

import re

keywords_list = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
            'for', 'from', 'int', 'float', 'bool', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
arithmetic_Operators = ["+", "-", "*", "=", "==", "<=", ">=", "<", ">", "/"]

# Make a regular expression for
# identifying Floating point number 
regex = '[+-]?[0-9]+\.[0-9]+'

def isFloatNumber(floatnum): 
     # pass the regular expression
     # and the string in search() method
    if(re.search(regex, floatnum)): 
        return True
    else: 
        return False

# Precedence Operator Grammar Table
nfa = [
    [None, 'id', '+', '*', '$'],
    ['id', None, '>', '>', '>'],
    ['+', '<', '>', '<', '>'],
    ['*', '<', '>', '>', '>'],
    ['$', '<', '<', '<', None]
]
# print("2name".isidentifier())

# File's Input should be in one line as it make sense
file = open("src.txt", "r")

file_input = file.readlines()[0]

splits = []

# a = b + d <- input will like this tokens will be seperated with space and any arithmetic operator according to question

# it will be List of identified tokens from input
identifier = []
number = []
floating = []
pointNumber = [],
keywords = []
arithmetic_operator = []
invalid_token = []

# Now in here we will have split tokens and seperators too, we will next remove seperators
split_input = file_input.split(' ')

# Here we will have removed seperators and have just unverified tokens
unidentify_tokens = []

# Removing seperators
for unknown_token in split_input:
    if unknown_token not in arithmetic_Operators:
        unidentify_tokens.append(unknown_token)
    else:
        arithmetic_operator.append(unknown_token)

# Here we are seperating the Tokens
for unverify_token in unidentify_tokens:
    if (unverify_token in keywords_list):
        keywords.append(unverify_token)

    elif (unverify_token.isidentifier()):
        identifier.append(unverify_token)

    elif (unverify_token.isnumeric()):
        number.append(int(unverify_token))

    elif (isFloatNumber(unverify_token)):
        floating.append(float(unverify_token))

    elif (unverify_token in arithmetic_Operators):
        arithmetic_operator.append(unverify_token)

    else:
        invalid_token.append(unverify_token)

# print(identifier, number, floating, keywords, arithmetic_operator, invalid_token)

# From here onwards we are going to put required tokens to the buffer

buffer = []

# all_valid_tokens = identifier + number + floating + pointNumber + keywords + arithmetic_operator
all_valid_tokens = identifier + number + floating + keywords + arithmetic_operator

# print(all_valid_tokens, 'asd')

# for index, terminal in enumerate(nfa[0]):
for index, token in enumerate(all_valid_tokens):
  
    if (token == '$'):
        continue

    if (token in nfa[0]):
        buffer.append(token)

buffer.append('$')

print("BUFFER:")
print(buffer, '\n')

# Now parse this buffer input through precedence operator nfa

stack = ['$']

isAccepted = False

for indexNumber, terminal in enumerate(buffer):
    print('State:', indexNumber)
    if (terminal == '$' and buffer[-1] == '$' and len(stack) == 1 and stack[0] == '$'):
        isAccepted = True
        break

    # nfa indexes
    bufferIndex = nfa[0].index(terminal)
    stackIndex = None

    for index, list in enumerate(nfa):
        if list[0] == stack[-1]:
            stackIndex = index
            break

    # print(stackIndex, bufferIndex)

    # Just push if if its low
    if nfa[stackIndex][bufferIndex] == '<':
        stack.append(terminal)
        print('Addded to stack')
    
    # Pop if its high
    elif nfa[stackIndex][bufferIndex] == '>':
        stack.pop()
        print('popped from stack')
        for stackElement in reversed(stack):

            index = None
            for indexs, list in enumerate(nfa):
                if list[0] == stackElement:
                    index = indexs
                    break

            
            if nfa[index][bufferIndex] == '<':
                stack.append(terminal)
                break
            else:
                stack.pop()

        
print('STACK', stack)
if (isAccepted):
    print('Accepted')
else:
    print('Rejected')

