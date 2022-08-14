import string
inm =input("Enter language: ")
list2=[]
l3=[]
num=[]
check=False
f = open("file.txt", "r")
x=f.readlines()
list2=[line.rstrip() for line in x]
rez = [x.split("\t") for x in list2]
state=0
print(rez)
for x in range(0,len(rez)):
  l3.append(list(rez[x]))
print(l3)

for i in inm:
  for j in l3[state]:
    if (j=='a-z'):
      if (i in string.ascii_lowercase):
        preState=state
        s="State {p}->{inp} moves to state: {s}"
        ind=l3[state].index(j)
        state=ind
        print(s.format(p=preState,inp=i,s=state))
        check=True
        break
      else:
        check=False
    elif (j=='0-9'):
      if (i=='0'or i=='1' or i=='2' or i=='3'or i=='4'or i=='5'or i=='6'or i=='7'or i=='8'or i=='9'):
        preState=state
        s="State {p}->{inp} moves to state: {s}"
        ind=l3[state].index(j)
        state=ind
        print(s.format(p=preState,inp=i,s=state))
        check=True
        break
      else:
        check=False
    elif (j=='A-Z'):
      if (i in string.ascii_uppercase):
        preState=state
        s="State {p}->{inp} moves to state: {s}"
        ind=l3[state].index(j)
        state=ind
        print(s.format(p=preState,inp=i,s=state))
        check=True
        break
      else:
        check=False
    elif (state ==4):
      if(i in string.ascii_lowercase or i=='0'or i=='1' or i=='2' or i=='3'or i=='4'or i=='5'or i=='6'or i=='7'or i=='8'or i=='9' or i in string.ascii_uppercase):
        s="State {p}->{inp} moves to state: {s}"
        print(s.format(p=state,inp=i,s=state))
        check=True
        break
      else:
        check=False
        break
        

    elif (i in l3[state]):
      preState=state
      s="State {p}->{inp} moves to state: {s}"
      ind=l3[state].index(i)
      state=ind
      print(s.format(p=preState,inp=i,s=state))
      check=True
      break
    else:
      if(j=='-'):

        check=True
      else:
        check=False
        break
  if(check==False):
    break
if(state==4 and check==True):
  print("String ", inm," is Accepted")
elif(state<4 or check==False):
  print("String ",inm,"is Not Accepted")

