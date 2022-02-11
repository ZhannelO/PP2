list=[]
s=str()
while(s!='0'):
    s=str(input())
    list.append(s)
list.remove(list[len(list)-1])
reversed=[]
for x in list:
    k=x.split()
    p=str(k[2]+" "+k[1]+" "+k[0])
    reversed.append(p)
reversed.sort()
ans=[]
for x in reversed:
    j=x.split()
    l=str(j[2]+" "+j[1]+" "+j[0])
    ans.append(l)
for i in ans:
    print(i)
    