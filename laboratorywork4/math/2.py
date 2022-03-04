import math
def Area(base1,base2,h):
    sum=base1+base2
    area=float(sum/2)*h
    return area
h=int(input("Height: "))
base1=int(input("Base, first value: "))
base2=int(input("Base, second value: "))
print(Area(base1,base2,h))
