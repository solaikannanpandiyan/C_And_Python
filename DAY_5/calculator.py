

def calculator(x, y):
    return x+y

opp = "mul"

# add 2, 3
# jump 101
if opp == "add": # true jump 1002 | false = jump 1004 #add 1000
    print(calculator(2,3)) #add 1002
    if True:
        print("hi")
else:   #add 1003
    print("not supported") #add 1004
    print()
    
