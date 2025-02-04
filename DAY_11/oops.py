# OOPS -> pardigm,
# object oriented programming
# function -> can do a lot
# why? oops ->

# solid principle | design patterns 

# feature -> cost-efficient, optimized
# why? 
# backend development, oops -> java
# real world problems -> model oops easy
# ticket booking, movie, banking, transport
# oops -> easy

# real world -> object
# object -> data | behavior
# function oriented -> behaviour
# oops -> low level design easy
# games, real problem oops -> complexity , 
# java|c# is good oops (paradigm) language
# web scrapping script, file movement -> functional
# python -> multipardigm, functional, oops,
# dynamically typed -> python | javascript -> runtime type checking
# python everything is an object -> tinkering (magic or dunder methods)
# why? -> real time problem model oops easy,

# features 
# real work problem model -> model clean(no code repition), modular(easy to change)

# OOPS concept
# abstraction -> java features, python
# polymorphism -> xcompile time, runtime
# encapsulation -> tight binding of data and behavior/function
# inheritance -> code reusage |   
# original utils class - 1000 function -> 10 modules
# utils class -> 1 function different

# util clone -> copy all 1000 nfunction adn then change 1 alone

# inheritance - > object 1 function overide -


# open for extension and extend modify, 
# closed for modification

# read design, -> low level design
# SOLID PRINCIPLE ->
# DESIGN-PATTERN -> 23 

# association - 
# composition - composition
# aggregation -
# only data, no behavior
    # data class
    # django, flask -> schema
    # object to table mapping -> ORM
    # SQL(postgres, oracle, mysql) | NOSQL -> 4 types
    # constructor
    
class student(object):
    def __init__(self, name, rollno): # constructor
        self.name = name # data
        self.rollno = rollno # data
        print(self.action())
    
    def action(self): # behaviour/function
        return "study"
    
print("# OOPS")
std1 = student("arun",101) 
# __call__ -> object create in memory
# __new__ -> we will get self argument 
# object is of instance type student verify
# self objectt will be pased to __init__
print(std1.name)
print(std1.rollno)
std1.name = "vijay"
std1.rollno = 102
print(std1.name)
print(std1.rollno)

# both are same
print(std1.action())
print(student.action(std1))

# ENCAPSULATION - python
# not strictly enforced in python
# data hiding -> features | no access specifier in python __
# access restriction/control -> features

# python design philosphy -> everything should be visible and open to access
class student2:
    def __init__(self, name, rollno): # constructor
        self.__name = name # private
        self.__rollno = rollno # private
        print("called inside constructor", self.action())
        
    def setname(self,name):
        if not isinstance(name, str):
            print('student name should be only string')
        else:
            self.__name = name
        
    def action(self):
        return f"student name :{self.__name} studies"


std2 = student2("arun",101)
print(std2.action())

# Data Hiding
# print(std2.__name) # cannot acces since private
# print(std2.__rollno) # cannot acces since private
# bypass
# print(std2._student2__name)

# Data restriction
std2.setname("kamal")
print(std2._student2__name)
# bypass
std2._student2__name = 1
print(std2._student2__name)


# INHERITANCE

class Animal(object): # parent class
    def walk(self):
        print("walks")
        
class Dog(Animal): # subclass or child class
    def speak(self):
        print("bark")
    
animal = Animal() 
dog = Dog() 
dog.walk() # v walks
dog.speak() # v bark
animal.walk() # v walks
# animal.speak()  # error
# MRO - method resolution 
# -> current class -> left class -> right class -> ancestor
# java multiple inheritance no
# python mltiple inhertiance is there

# diamond problem
class Animal(): # parent class
    # pass
    def sound(self):
        print("animal sound")

class Tiger(Animal): # parent class
    pass
    # def sound(self):
    #     print("Tiger sound")

class Lion(Animal): # parent class
    pass
    # def sound(self):
    #     print("Lion sound")

class Liger(Tiger, Lion):
    pass
    #  def sound(self):
    #     print("Liger sound")
        
liger = Liger()
# liger.sound() # "Liger sound"
# liger.sound() # "Tiger sound"

# 

