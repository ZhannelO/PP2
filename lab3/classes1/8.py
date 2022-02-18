def spy_game(list):
    h=[]
    for i in list:
        h.append(i)
    for i in range(0,len(h)):
        if h[i]==0 :
            for x in range(i+1,len(h)):
                if h[x]==0:
                    for j in range(x+1,len(h)):
                        if h[j]==7:
                            print("True")
                            break
    
a=[1,2,4,0,0,7,5]
spy_game(a)
b=[1,0,2,4,0,5,7]
spy_game(b)
c=[1,7,2,0,4,5,0]
spy_game(c)