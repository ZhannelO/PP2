class Shape:
    def __init__(self,lenght,width):
        self.lenght=lenght 
        self.width=width
class Rectangle(Shape):
    def area(self):
        return self.lenght*self.width
l=int(input())
w=int(input())
rec=Rectangle(l,w)
print(rec.area())