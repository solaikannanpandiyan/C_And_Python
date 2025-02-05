from abc import ABC, abstractmethod
# Abstraction -> generally complexity hide panrathu
# backend - hiding | only need are visible | blueprint of all other class
# 
class Shape(ABC):
    @abstractmethod
    def area(self) -> int | float:
        pass
    
    # def parent(self):
        print("this method is a child of Shape")
    
class Cirle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width

# circle = Cirle(7)
# square = Square(5)
# rectangle = Rectangle(8,9)
# shapes = [circle, square, rectangle]
# def findarea(shape):
#     print(shape.area())

# for i in shapes:
#     findarea(i)

# shape = Shape()

class scooty(ABC):
    

# association


# aggregation

# composition