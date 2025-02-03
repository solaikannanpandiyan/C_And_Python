# higher order function
def operation(opp, val1,val2):
    print("val1", val1)
    print("val2", val2)
    output = opp(val1,val2)
    print("output", output)
    
def summ(x, y):
    return x+y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

print("HIGHER ORDER FUNCTION")
# print(type(operation))
# print(type(summ))
# print(type(mul))
# print(type(div))
# operation(summ, 10,12) 
# operation(mul, 10,12)
# operation(div, 10,5)

# closure
print("CLOSURE")
# function
# None -> default return type
# number, float, list, tuple, dict - data
# function (function is also a object)
# object 


# enclosing scope variable and data will be alive and persisted
def multiplier(x): # x value is in enclosing scope for function multiply
    # x = 5
    def multiply(y):
        return x * y # x is in enclosing scope variable
    return multiply # returning function

# print("multiplier : ",type(multiplier))
# double = multiplier(2) # x=2; 
# print("double : ",type(double))
# triple = multiplier(3) # x=3; 
# print("triple : ",type(triple))

# print(double(10)) # y=10; 20
# print(triple(10)) # y=10; 30

# DECORATORS -> syntax
# closure -> input function and output is also function
# log all input to the funciton
# also log all output from the function

print("# DECORATORS")
# without decorator approach
# tuple variable arguments
# def summ(*x):
#     print("input : ",x) # not business function
#     output = sum(x)
#     print("output : ", output) # not business function
#     return output

# def productt(*x):
#     print("input : ",x) # not business function
#     prod = 1
#     for i in x:
#         prod *= i
#     print("output : ", prod) # not business function
#     return prod

# print(summ(1,2,3,4,5,6))
# print(productt(1,2,3,4,5,6))

# decorator  -> python helps us to implement easily
# annotations -> java
def funclogger(func): # input function | func -> enclosing scope
    
    def wrapped(*args):
        print("input : ",args)
        output = func(*args)
        print("output : ", output)
        return output
    
    return wrapped # output function


# is equivalent to summ = funclogger(summ) # summ function is wrapped
@funclogger
def summ(*x):
    return sum(x)

# is equivalent toproductt = funclogger(productt) # productt function is wrapped
@funclogger
def productt(*x):
    prod = 1
    for i in x:
        prod *= i
    return prod

# x = 10
# x = x+ 10

# productt = funclogger(productt) # productt function is wrapped
print(summ(1,2,3,4,5,6))
print(productt(1,2,3,4,5,6))



# is python call by value or reference?
print("# is python call by value or call by reference?")
x = 10 # immutable
y = ("hello","hi") # immutable tuple, number, string -> pass by value/data
z = [3,2,1] # list, dict, set  -> pass by object reference

print("Before passing")
print(x) # 10
print(y) # hello
print(z) # [3,2,1]

def change(obj1,obj2,obj3):
    obj1 += 20
    obj2 += (" world","")
    obj3[2] = 5
    print("Inside function")
    print(obj1) # x30
    print(obj2) # xhello world
    print(obj3) # v[3,2,5]

change(x,y,z) 

print("After passing")
print(x) # x30
print(y) # xhello world
print(z) # v[3,2,5]


# unpacking
print("# unpacking") 
# tuple, list, set 
# dict(key,value) -> difference
tup = (1,2,3,4)
print(tup) #  (1,2,3,4)
# both are same
print(*tup) # 1,2,3,4
print(1,2,3,4)

print("# position based")
# tuple, set, list
first, *tup, last = (1,2,3,4)
# first, *tup, last = [1,2,3,4]
# first, *tup, last = {1,2,3,4}
print(first)
print(tup)
print(last)

# dictory or key-value pair unpacking
dct = {"one":"1", "two":"2", "three":"3"}
print(*dct.items()) # set(setlike) of tuples
print(*dct.values()) # set of any
print(*dct.keys()) # set of hashablle, int, str, tuple
# for k,v in dct.items:
#     print(k,v)
dct = {"sep":" ", "end":" "}
print("hello","hi","good","day",**dct)# both statements are equivalent
print("hello","hi","good","day",sep=" ", end=" ") 
# print("hello","hi","good","day",one="1", two="2",three="3")  -> not works

# # generic function in python
print()
print()
print("# generic function in python")
def genericfunc(*args, **kwargs):
    print("args: ",args)
    print("*args: ",*args)
    print("args: ",kwargs)
    
genericfunc(1,2.0,"hello",lst=[1,2,3],tup=(1,2,3),set={1,2,3},dct={1:1,2:2,3:3})
genericfunc(1,2)
genericfunc(1,2,3,x=10,y=10)
genericfunc()
