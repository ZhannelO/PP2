def unique(list):
    h=[]
    for i in list:
        h.append(i)
    uni=[]
    for x in h:
        if x not in uni:
            uni.append(x)
    for x in uni:
        print(x,end=" ")
list=[1,7,2,0,4,5,0]
unique(list)