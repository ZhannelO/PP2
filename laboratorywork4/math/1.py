import math
def radians(degree):
    k=float(math.pi/180)
    radian=degree*k
    return radian
degree=int(input())
print(radians(degree))