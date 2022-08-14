def comb(di):
    i=0
    for key , value in di.items():
        for key1 , value1 in di.items():
            if key==key1:
                continue
            for x in value1:
                print(value[i],x)

        i=i+1

di={"1":['a','b'],
    "2":["c","d"]}
comb(di)
