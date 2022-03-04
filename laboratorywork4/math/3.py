import math
def Area(n,a):
    tg=math.tan(math.pi/n)
    den=a**2
    k=4*tg
    area=n*den/k
    return area
n=int(input("number of sides:"))
a=int(input("the length of a side:"))
print("The area of the polygon is:"+" "+str(Area(n,a)))
