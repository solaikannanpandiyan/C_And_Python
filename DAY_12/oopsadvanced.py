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
# interface segratate
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

    def info(self):
        print("Scooty info")


class TVS(Scooty):
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f"{self.name} moves forward..")

    def decelerate(self):
        print(f"{self.name} slow down..")

    def brake(self):
        print(f"{self.name} stops.")

    # def info(self):
    #     print("tvs info")

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
    
    # def info(self):
    #     print("aether info")

    def fuel(self):
        print(f"{self.name} runs on electric")


def printfunc(obj : Scooty):
    obj.info()
    obj.decelerate()
    obj.brake()
    obj.fuel()


bike1 = TVS("Jupiter")
bike2 = Aether("Ritz")
printfunc(bike1)
printfunc(bike2)


# inheritance open-closed principle:
print("# inheritance open-closed principle:")
# closed for modification
class car():
    def __init__(self, name):
        self.name = name

    def getinfo(self):
        print(f"this is a {self.name}")

# open for extension
class specialeditioncar(car):
    def __init__(self, name):
        self.name = "special edition " + name

    # def getinfo(self):
    #     raise Exception("this is a secret car, we cannot reveal info.")

cr1 = car("ferrari")
cr1.getinfo() # this is a ferrari

cr2 = specialeditioncar("ferrari")
cr2.getinfo()

a = int(10)
print(a) # 10
# Int type(value: 10)

class customint(int):
    def __str__(self):
        return f"Int type(value : {super().__str__()})"
b = customint(10)
print(b)


# association -> some relationship between objects
# one to one
# one to many -> one author can have many books
# many to many
class Author:
    def __init__(self, name):
        self.name = name
    
    def getAuthorDetails():
        return "author details"


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
class Engine:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"Engine {self.model} started.")

class Car:
    def __init__(self, make, engine_model):
        self.make = make
        self.engine = Engine(engine_model)  # The Car "owns" the Engine

    def drive(self):
        print(f"Driving {self.make} car...")
        self.engine.start()  # Accessing engine method from Car

# Creating objects
car = Car("Tesla", "Model S")

# Driving the car (which starts the engine)
car.drive()