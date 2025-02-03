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
        print(x)
        return x * y # x is in enclosing scope variable
    return multiply # returning function

print("multiplier : ",type(multiplier))
double = multiplier(2) # x=2; 
print("double : ",type(double))
triple = multiplier(3) # x=3; 
print("triple : ",type(triple))

print(double(10)) # y=10; 20
print(triple(10)) # y=10; 30
