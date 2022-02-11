a=[]
ans=[]
n=int(input())
for i in range(n):
    bk=input().split()
    if bk[0]=="1":
        ans.append(bk[1])
    else:
        if len(a)==0:
            pass
        else:
            ans.append(a.pop())
print(*ans)