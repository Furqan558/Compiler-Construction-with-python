Keywords=['print','False','await','else','import','pass','None','break','except','in','raise','True','class','finally','is','return','and','continue','for','lambda','try',
'as','def','from','nonlocal','while','assert','del','global','not','with','async','elif','if','or','yield']

ArithmeticOperators=['+','-','*','=','==','<=','>=','<','>','/']
Numbers=['0','1','2','3','4','5','6','7','8','9']
Separators=[" ",'\n','(',')',',',':']
array=[]
f = open("src.txt","r")
array = f.readlines()
for a in array :
    print(a)
    token = ''
    chk = False
    chk1 = 0
    for b in a:
        if b not in Separators :
            if b == '"' or chk == True:
                chk = True
                chk1 = chk1 + 1
                if chk1 > 1 and b == '"' :
                     chk = False
            else :
                token = token + b
        else :
            if len(token)> 0 :
                if token in Keywords:
                    print("Token ",token)
                    token = ''
                
                elif token[0] in Numbers or token[0] == '.' :
                    if '.' in token :
                        print("Token is Floating Point",token)
                        token = ''
                    else :
                        print("Token is Number",token)
                        token = ''
                    
                elif token in ArithmeticOperators :
                    print("Token is ArithmeticOperators",token)
                    token = ''
                else :
                    print("Token is Identifier",token)
                    token = ''

