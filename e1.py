s=str(input())
num=s.split()
if len(num)==1:
    x=int(input())
    n=int(num[0])
else :
    n=int(num[0])
    x=int(num[1])
a=[]
for j in range(0,n):
    k=x+2*j
    a.append(k) 
ans=a[0]
for i in range(1,len(a)):
    ans=ans^a[i]
print(ans) 
