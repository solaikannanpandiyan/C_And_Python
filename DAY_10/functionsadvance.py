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



#

    

