#dic= {
 #   "nsme" : "FAIZA AHMAD" }
#for key in dic:
 #   print(key)
#for value in dic.values():
 #   print(value)

#Q1
z=3
data = {
    1:["a","b","c"],
    2:["e","f","g"]}
lis=[]
lis2=[]

for values in data.values():
    lis.append(values)
print(lis)
for y in range (z):
  for i in range(len(lis)):
      for x in range(z):
          try:
              print(lis[i][y],lis[i+1][x])
          except:
              continue
            

#Q2
#sum all the items in list
def summation(lis):
    s=0
    for i in lis:
        s=s+i

    return s
l=[1,2,3]
print(summation(l))



#Q3
#multiply all the items in list
def multi(lis):
    m=1
    for i in lis:
        m=m*i
    return m
ll=[1,2,3]
print(multi(ll))


#Q4
#removing 0th 4th 5th item
lis=["Red","Green","white","black","pink","Yellow"]
lis.remove("Red")
lis.remove("Green")
print(lis)
.





    
    
    
