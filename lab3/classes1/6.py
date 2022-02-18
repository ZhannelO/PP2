def reversed(s):
    a=s.split()
    i=len(a)-1
    while i>=0:
        print(a[i],end=" ")
        i=i-1
s=str(input())
reversed(s)