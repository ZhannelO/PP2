n=int(input())
k=[]
a=[]
str=str(input())
k=str.split()
for i in range(len(k)):
    j=int(k[i])
    a.append(j)
max=int(a[0])
ind=0
for x in range(len(a)):
    if a[x]>max:
        max=a[x]
        ind=x
a.pop(ind)
max2=int(a[0])
for x in range(len(a)):
    if a[x]>max2 :
        max2=a[x]
ans=max*max2
print(ans)
