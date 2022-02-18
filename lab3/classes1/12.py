def histogram(list):
    a=[]
    for i in list:
        a.append(i)
    v=[]
    for i in a:
        n=""
        while(i!=0):
            n=str(n)+"*"
            i=i-1
        v.append(n)
    for x in v:
         print(x)       
b=[4, 9, 7]
histogram(b)