class Shape:
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self,lenght):
        self.len=lenght
sqr=Square(0)
sqr.area()