# OOPS 
# object oriented programming
# function -> can do a lot
# why? oops
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
# dynamically typed
# python everything is an object
# why? -> real time problem model oops easy

# features 
# real work problem model -> model clean(no code repition), modular(easy to change)

# abstraction -> java features, python
# polymorphism -> compile time, runtime
# encapsulation -> tight binding of data and behavior/function
# inheritance -> code reusage, 
# open for extension and extend modify, 
# closed for modification

# read
# SOLID PRINCIPLE - >
# DESIGN PATTERN -23 

# association - 
# composition - composition
# aggregation -
# only data, no behavior
    # data class
    # django, flask -> schema
    # object to table mapping -> ORM
    # SQL(postgres, oracle, mysql) | NOSQL -> 4 types
    # constructor
    
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
    def action(self):
        return "study"
    
print("# OOPS")
std1 = student("arun",101) 
# object create in memory
# self argument stored
# object is of instance type student verify
# self objectt will be pased to __init__
print(std1.name)
print(std1.rollno)

print(std1.action())
print(student.action(std1))

# ENCAPSULATION
# not strictly enforced
# data hiding
# access restriction or 
# control 
class student2:
    def __init__(self, name, rollno):
        self.__name = name # private
        self.__rollno = rollno # private
    
    # def setter(self, name, rollno):
    #     if not isinstance(rollno, int):
    #         throw Exception()
    
    def action(self):
        return f"student name :{self.__name} studies"
std2 = student2("arun",101)
print(std2.action())
print(dir(std2))
# print(dict(std2))
print(std2._student2__name)
print(std2.__name)
# print(std2.action())