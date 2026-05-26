
class Rectangle:
    
  
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    
    def area(self):
        return self.length * self.breadth

  
    def perimeter(self):
        return 2 * (self.length + self.breadth)



class Square(Rectangle):
   
    def __init__(self, side):
        super().__init__(side, side)


rect = Rectangle(10, 5)

print("Rectangle")
print("Area =", rect.area())
print("Perimeter =", rect.perimeter())

sq = Square(4)

print("\nSquare")
print("Area =", sq.area())
print("Perimeter =", sq.perimeter())