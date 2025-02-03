# functions -> script file or module
# package -> group of modules

# function definition
# reason: code - reustopping="cheese", bread="wheat"ablity
# code destruction - code reorganization and feature addition is easier
# function oriented -> using functions
# object oriented


# global scope
# globalx = 10

# default return type is None
# global
def summ(x,y):
    # print("x : ", x)
    # print("y : ", y)
    return x+y

# 2 types of arguments:
# positional argument
# keyword argument
# default values only for keyword argument
def makePizza(count, price, bread ="wheat", topping="cheese" ):
    print("count : ",count)
    print("price : ",price)
    print("topping : ",topping)
    print("bread : ",bread)
    
# variable arguments
def summvariable(*vars, **kwargs):
    print(vars)
    print(type(vars))
    print(kwargs)
    print(type(kwargs))
    return sum(vars)

# local scope
def scoping(v):
    # design patterns
    # antipatterns -> exception
    # monkey patching
    
    # local scope
    # we cannot define a global variable in local scope
    # we can point to or change value of global variable inside a function using global keyword
    global globalx
    globalx = v
    # x = 13
    print("inside scoping globalx", globalx) # 15
    
    
    
print("before if main block", globalx) # 10
if __name__ == '__main__':
    # function and return types
    print(summ(10,12)) # 22
    print(summ(12,12.0)) # 24.0
    print(summ("hello ","world")) #hello world
    
    a = 10
    b = a
    print(b) # 10
    print(type(b))
    # print(b())
    
    # functions as objects
    summduplicate = summ
    print(summduplicate(10,12))
    print(type(summduplicate))
    
    # variable parameters/arguments
    # print("hello", 1,None,1.1,"")
    output = summvariable(1,2,3,4,5,141,232, type="integer sum",functype="variable" )
    print(output)
    
    
    # positional and keyword arguments
    # position -> ordering is importaant and no default values
    # keyword -> ordering is not important, we can have default and optionval parmeters
    makePizza(1,5,bread="maida", topping="soy sauce")
    
    print("1","2","3")
    print("1","2","3",sep="")
    print("1","2","3",sep="",end=" ")
    print("hello")
    # output
    # 1 2 3
    # 123
    # 123 hello
    
    print("Scoping Rules")
    scoping(15) # 15
    scoping(20) # 20 
    scoping(40) # 40
    print("inside if main block globalx", globalx) # 15
    # scope
    # L -> E -> G -> B
    # L - local
    # E - enclosing -> closures
    # G - global -> module level
    # B - buildin, inbuilt functions -> across module
print("outside if main blockglobalx", globalx) # 15
    