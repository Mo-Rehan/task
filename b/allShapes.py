from a.shapes import shapes

class rectangle(shapes):
    # perimeter of a rectangle
    def perimeter(self):
        return (2 * (self.side1 + self.side2))
    
class square(shapes):
    # perimeter of a square
    def perimeter(self):
        return (4 * self.side1)
    

class triangle(shapes):
    # perimeter of a square
    def perimeter(self):
        return (self.side1+self.side2+self.side3)
    

t= triangle(4,6,8)
print(t.area())
print(t.perimeter())

t= rectangle(4,6)
print(t.area())
print(t.perimeter())

t= square(4)
print(t.area())
print(t.perimeter())