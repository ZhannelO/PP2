def tozero(n):
    for i in range(n)[::-1]:
        yield i
n=int(input())
for x in tozero(n):
    print(x)