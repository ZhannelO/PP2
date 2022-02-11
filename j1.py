n=int(input())
a=set()
for i in range(n):
    s=str(input())
    a.add(s)
u=[]
for x in a:
    u.append(x)
res=[]
for l in range(0,len(u)):
    cntupper=0
    cntlower=0
    cntnum=0
    for j in u[l]:
        if 'A'<=j and j<='Z':
            cntupper=cntupper+1
        if 'a'<=j and j<='z':
            cntlower=cntlower+1
        if '0'<=j and j<='9':
            cntnum=cntnum+1
    if cntupper>0 and cntlower>0 and cntnum>0:
        res.append(u[l])
print(len(res))
for x in sorted(res):
    print(x)