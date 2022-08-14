with open("INPUT_LAB_6.txt","r") as file:
    data = file.readlines()

    # all keywords of python
    keywords = ['False','await','else','import','pass','None','break','except','in','raise','True','class','finally','is','return','and','continue','for','lambda','try','as','def','from','nonlocal','while','assert','del','global','not','with','async','elif','if','or','yield']
    #print("\nAll Python's keywords : \n",keywords)
    # operators
    PredefinedOperators = ['=','+','-','*','/','>','<','>=','<=','==','>','<','<=','>=','(',')']
    
    Tokens = []
    
    AllNumbers = []
    AllFloatingNumbers = []
    AllOperators = []
    KeywordsFind = []
    InValidTokens = []
    AllIdentifiers = []

    buffer = []

    # seperate tokens from the whole file
    for line in data:
        line = line.strip().split()
        for item in line:
            Tokens.append(item)

    print("Overall Tokens Found = ",Tokens)
    # insert all values within the lists
    for item in Tokens:
        if item in PredefinedOperators:
            AllOperators.append(item)
        elif item.isidentifier() == True and item not in keywords:
            buffer.append('id')
            AllIdentifiers.append(item)
        elif item.isdigit() == True  :
            AllNumbers.append(item)
        else:
            if item not in keywords:
                InValidTokens.append(item)    
        if item in keywords:
            KeywordsFind.append(item)
            
    print("Numbers Found = ",AllNumbers)
    print("Operators Found = ",AllOperators)
    print("Identifiers Found = ",AllIdentifiers)
    print("Keywords Found = ",KeywordsFind)
    print("In Valid Tokens Found = ",InValidTokens)
    
    

    #print("\nOperators = ",PredefinedOperators)
    for item in AllOperators:
        if item=='*' or item=='+':
            buffer.append(item)
    buffer.append('$')
    
    print("Buffer = ",buffer)
    BUFFER = ['id','+','id','*','id','$']
    

    # Operational Precedence Table With  Indexes
    OperationalPrecedenceTable2 = [['-','id','+','*','$'],['id','-','>','>','>'],['+','<','>','<','>'],['*','<','>','>','>'],['$','<','<','<','-']]
    OperationalPrecedenceTable = [['-','>','>','>'],['<','>','<','>'],['<','>','>','>'],['<','<','<','-']]
    # id M A $
    PrecedenceValues = {'id':1 , '*':2 , '+':3 , '$':4}

    Stack = []
    Stack.append('$')
    print("----------------------------------------------------------------------")
    print("Operational Precedence Table  = ",OperationalPrecedenceTable)
    print("----------------------------------------------------------------------")
    print("Initial Stack",Stack)
    print("----------------------------------------------------------------------")

   # required buffer entries
    RequiredBufferEntries = list() # to store unique values
    for row in OperationalPrecedenceTable2:
        for item in row :
            if item != '-' and item!='<' and item!='>' and item!='$':
                RequiredBufferEntries.append(item)
    # again convert it into the list to access
    RequiredBufferEntries.append('$')
    ToList = []
    for i in RequiredBufferEntries:
        if i not in ToList:
            ToList.append(i)
    #print("\nAll Buffer's Tokens From The Operational Precedence Table : \n",RequiredBufferEntries,"\n")

    # iterate through bufffer and searching through stack
    print("Terminal Symbols  = ",ToList)

        
