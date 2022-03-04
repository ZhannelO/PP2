def even(n):
    for i in range(n):
        if i%2==0:
            yield i
n=int(input())
s=str()
for x in even(n):
    s=s+str(x)+","
print(s[:-1])