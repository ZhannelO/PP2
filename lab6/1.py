#Write a Python program with builtin function to multiply all the numbers in a list
def mul(list):
    ans=1
    for i in list:
        ans=ans*i
    print(ans)
n=int(input())
list=[]
for x in range(0,n):
    a=int(input())
    list.append(a)
mul(list)

