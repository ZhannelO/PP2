n=int(input())
a=[[0]*n for i in range(n)]
if n%2==0:
    for i in range(0,n):
        for j in range(0,n):
            if i<j:
                a[i][j]="."
            else:
                a[i][j]="#"
else:
    for i in range(0,n):
        for j in range(0,n):
            if i+j==j+i and i+j>=n-1:
                a[i][j]="#"
            else:
                a[i][j]="."
for r in a:
    print("".join([str(k) for k in r]))
