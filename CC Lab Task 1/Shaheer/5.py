data={
    1:45.50,
    2:35,
    3:41,
    4:90
    }
d2=dict(sorted(data.items(), key=lambda item: item[1]))
c=0
for x, y in d2.items():
    if c==3:
        break
    print (x,"  ",y)
    c=c+1
