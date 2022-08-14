import re

file = open("input.txt")

operators = {'=': 'Assignment operator', '+': 'Addition operator', '-': 'Subtraction operator', '/': 'Division operator',
             '*': 'Multiplication op', '<': 'Lessthan op', '>': 'Greaterthan op'}
operators_key = operators.keys()

data_type = {'int': 'integer type', 'float': 'Floating point', 'char': 'Character type', 'long': 'long int'}
data_type_key = data_type.keys()

punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {'a': 'variable', 'b': 'variable', 'c': 'variable', 'd': 'variable'}
identifier_key = identifier.keys()

logicaal_operator ={'&': 'AND op', '!': 'NOT op', '|': 'OR op'}
logicaal_operator_key = logicaal_operator.keys()

header_file = {'<stdio.h>': 'Standard I/O library', '<cstdlib>': 'Random Num library'}
header_file_key = header_file.keys()

comment = {'//': 'Single line comment', '/**/': 'Multiline Comment'}
comment_key = comment.keys()

keyword_in_cpp = {'for': 'For keyword', 'auto': 'Auto keyword', 'friend': 'Friend keyword', 'class': 'Classs keyword',
                  'private': 'Pricate keyword', 'this': 'This keyword', 'bool': 'Boolean keyword', 'true': 'True keyword',
                  'try': 'Try keyword', 'while': 'While keyword'}
keyword_in_cpp_key = keyword_in_cpp.keys()

dataFlag = False

a = file.read()

count = 0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#", count, "\n", line)

    tokens = line.split(' ')
    print("Tokens are ", tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in operators_key:
            print("operator --> ", operators[token])
        if token in data_type_key:
            print("datatype --> ", data_type[token])
        if token in punctuation_symbol_key:
            print(token, "Punctuation symbol --> ", punctuation_symbol[token])
        if token in identifier_key:
            print(token, "Identifier --> ", identifier[token])
        if token in logicaal_operator_key:
            print(token, "Logical Operator --> ", logicaal_operator[token])
        if token in header_file_key:
            print(token, "Library --> ", header_file[token])
        if token in comment_key:
            print(token, "Comment --> ", comment[token])
        if token in keyword_in_cpp_key:
            print(token, "Keyword --> ", keyword_in_cpp[token])


    dataFlag = False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")
