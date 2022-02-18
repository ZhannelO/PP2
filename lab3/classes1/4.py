import math
def filter_prime(list):
    h=[]
    for i in list:
        h.append(i)
    for i in h:
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            print(i,end=" ")
list=[2,3,4,5,6,7,8,13] # 2 3 5 7 13
filter_prime(list)

