from itertools import permutations
def permut(str):
    list=permutations(str)
    for i in list :
        print(i,end=" ")
s=str(input())
permut(s)