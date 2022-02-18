class Point():
    def __init__(self,x,y):
        self.xo=x
        self.yo=y
    def show(self):
        xo= str(self.xo)
        yo=str(self.yo)
        return "Coordinates of the point:"+"{"+xo+"; "+yo+"}"
    def move(self,num):
        newx=str(self.xo+num)
        newy=str(self.yo+num)
        str(newy)
        return "Changed coordinates of the point:"+"{" +newx+";"+newy+"}"
    def dist(self,x1,y1):
        print((((self.xo - x1 )**2) + ((self.yo-y1)**2) )**0.5)
x=int(input())
y=int(input())
ch=int(input())
points=Point(x,y)
print(points.show())
print(points.move(ch))
points.dist(2,6)
