n=int(input())
a=[[0]*n for i in range(n)]
for i in range(0,n):
    a[i][0]=i
    a[0][i]=i
for i in range(1,n):
    a[i][i]=a[0][i]*a[i][0]
for row in a:
    print(*row)
 