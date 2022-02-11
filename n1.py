a=[]
n=str()
while(n!='0'):
     n=str(input())
     a.append(n)
a.remove(a[len(a)-1])
sum=[]
ind=len(a)-1
if(len(a)%2==0):
    for i in range(0,int(len(a)/2)):
         pair=int(a[i])+int(a[ind])
         sum.append(pair)
         ind=ind-1
else:
    for i in range(0,int(len(a)/2)):
        pair=int(a[i])+int(a[ind])
        sum.append(pair)
        ind=ind-1
    k=int(len(a)/2)
    sum.append(a[k])
print(*sum)

