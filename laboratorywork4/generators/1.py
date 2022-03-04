def square(N):
    for i in range(N):
        yield i**2
N=int(input())
for k in square(N):
    print(k)
