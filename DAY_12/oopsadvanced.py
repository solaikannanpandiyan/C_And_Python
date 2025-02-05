from abc import ABC, abstractmethod
# Abstraction -> generally hiding complexity and replacing simpler interface
# backend - hiding | only need are visible | blueprint of all other class

# template 
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

class Scooty(ABC):
    @abstractmethod
    def accelerate():
        pass
    
    @abstractmethod
    def decelerate():
        pass
    
    @abstractmethod
    def brake():
        pass
    
    @abstractmethod
    def fuel():
        pass

class TVS(Scooty):
    def __init__(self, name):
        self.name = name
        
    def accelerate(self):
        print(f"{self.name} moves forward..")
    
    def decelerate(self):
        print(f"{self.name} slow down..")
    
    def brake(self):
        print(f"{self.name} stops.")
    
    def fuel(self):
        print(f"{self.name} runs on petrol")
        
class Aether(Scooty):
    def __init__(self, name):
        self.name = name
        
    def accelerate(self):
        print(f"{self.name} moves forward..")
    
    def decelerate(self):
        print(f"{self.name} slow down..")
    
    def brake(self):
        print(f"{self.name} stops.")
    
    def fuel(self):
        print(f"{self.name} runs on petrol")
    
def printfunc(obj:Scooty):
    obj.accelerate()
    obj.decelerate()
    obj.brake()
    obj.fuel()
    
bike1 = TVS("Jupiter")
bike2 = Aether("Ritz")
printfunc(bike1)
printfunc(bike2)


# inheritance open-closed principle:
# class car():
#     def __init__(self, name):
#         self.name = name
        
#     def getinfo(self):
#         print(f"this is a {self.name}")
    
# class specialeditioncar(car):
#     def __init__(self, name):
#         self.name = "special edition " + name

# cr1 = car("ferrari")
# cr2 = specialeditioncar("ferrari")
# cr1.getinfo()
# cr2.getinfo()

# a = 10
# print(a)
# class customint(int):
#     def __str__(self):
#         return f"Int type(value : {super().__str__()})"
# b = customint(10) 
# print(b)
        

# association -> some relationship between objects
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Author is associated with the Book

# Creating objects
author1 = Author("J.K. Rowling")
book1 = Book("Harry Potter", author1)

print(f"Book: {book1.title}, Author: {book1.author.name}")

# aggregation
# -> owned objects can exist independtly
# -> ownder object will not get destroyed if parent or holder is destroyed
print("# AGGREGATION -> no dependency on existence")
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Creating objects
department = Department("Engineering")
employee1 = Employee("Alice")
employee2 = Employee("Bob")

# Adding employees to the department
department.add_employee(employee1)
department.add_employee(employee2)

print(f"Department: {department.name}")
for emp in department.employees:
    print(f"Employee: {emp.name}")


# composition 
# -> owned objects cannot exist independtly
# -> ownder object get destroyed if parent destroyed
print("# COMPOSITION -> strictly dependent ")