def has_33(list):
    h=[]
    for i in list:
        h.append(i)
    for i in range(0,len(h)-1):
        if h[i]==3 and h[i+1]==3:
            print("True")
            break
    else:
        print("False")
a=[1,3,3]
has_33(a)
b=[1, 3, 1, 3]
has_33(b)
c=[3, 1, 3]
has_33(c)