# DICT CONCEPTS -> unique keys mapping to unique or same values
import pprint
def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()
# definition
# key : value,
vardct = {1:'asf',1:'a'}
printformat(vardct) # {1:'a'}
vardct = dict()
printformat(vardct)
# keys -> numbers, character, string, tuple of immutables(numbers, character, string, tuple)
# values -> any(number, character, string, tuple, etc)
vardct = {(1,2,3,(1,2)):'asf'}
printformat(vardct) #  {(1,2,3,(1,2)):'asf'}


# see the doc


# ACCESSING -> not based on order but based on keys
vardct = {1:'asf',2:'a'}
print("ACCESSING")
print(vardct[1])
print(vardct[2])

# slicing -> no slicing
# print(vardct[1:2])

# Mutability -> dict is mutable
print("Mutability")
vardct = {1:'asf',2:'a'}
printformat(vardct)
vardct[1] = 'hello'
vardct[3] = 'wow!'
printformat(vardct)

# Common Methods in Dict Class
vardct = {"arun":1,"vimal":2,"kamal":3}
vardct2 = {"arjun":4,"ashwin":5}
print("keys: ",vardct.keys())
printformat(vardct.keys()) # set like object
print("values: ",vardct.values())
printformat(vardct.values())
print("items: ",vardct.items())
printformat(vardct.items())
print(vardct.get("arun1"))
vardct.update(vardct2)
print(vardct)
vardct.pop("arjun")
print(vardct)
print(vardct.popitem())


# Iteration
vardct = {"arun":1,"vimal":2,"kamal":3,"arjun":4,"ashwin":5}
printformat(vardct.items()) # dictitems class
for item in vardct.items():
    k,v = item # unpacking tuple
    printformat(item)
    print(f"key {k} : value {v}")

for key in vardct.keys():
     printformat(key)
    
for value in vardct.values():
     printformat(value)

# Dict Comprehensions -> list, tuples, set
print("Dict Comprehensions -")
# ^ -> xor
# ** -> power
vardict = {i : i**3 for i in range(10)}
print(vardict)
input = [(1,3),(2,3),(3,4)] # list of tuples
vardict = dict(input)
print(vardict)

# Nested Dict
# i : i**3 -> expression
vardict = {i : i**3 for i in range(3)}
# {i : i**3, i : i**3, i : i**3}
# {0 : 0**3, 1 : 1**3, 2 : 2**3}
# {0 : 0, 1 : 1, 2 : 8}
print(vardict)
vardict = {j: {i : j for i in range(3)} for j in range(3)} # 
pprint.pprint(vardict,indent=2)
# vardict
# {
#  0: {0: 0, 1: 0, 2: 0}, 
#  1: {0: 1, 1: 1, 2: 1}, 
#  2: {0: 2, 1: 2, 2: 2}
#  }

#   {0:0,1:0,2:0}, | {0:0,0:1,0:2}
#   {1:0,1:1,1:1},
#   {1:0,1:1,1:2},
# }


# Shallow Copy
print("# Shallow Copy")
vardict = {j: [i for i in range(3)] for j in range(3)} # 

print(vardict)
# {
#  0: [0,1,2]
#  1: [0,1,2]
#  2: [0,1,2]
# }

vardct2 = vardict.copy()
vardct2[0][0]= "hello"
printformat(vardict)
# {
#  0: ["Hello",1,2]
#  1: [0,1,2]
#  2: [0,1,2]
# }
printformat(vardct2)
# {
#  0: ["Hello",1,2]
#  1: [0,1,2]
#  2: [0,1,2]
# }
vardct2[3]= "wow" # copied
# {
#  0: ["Hello",1,2]
#  1: [0,1,2]
#  2: [0,1,2]
#  3: "wow"
# }
printformat(vardict) # orginal
printformat(vardct2) # copied

print("# Deep Copy")
vardict = {j: [i for i in range(3)] for j in range(3)} # 
# {
#  0: [0,1,2]
#  1: [0,1,2]
#  2: [0,1,2]
# }
import copy
vardct2 = copy.deepcopy(vardict)
vardct2[0][0]= "hello"
printformat(vardict) 
printformat(vardct2)

# dict Unpacking
# dict items -> unpacking


# Inbuilt methods -> 
# len -> performed directly
# filter, map, sorted -> performed on keys, values, items
vardict = {j: [i for i in range(3)] for j in range(3)} # 
print(len(vardict))
print(list(sorted(vardict)))

# operations ->  | -> union
vardict = {j: [i for i in range(3)] for j in range(3)} # 
vardict2 = {j: [i for i in range(3)] for j in range(3,7)} # 
vardict3 = vardict | vardict2
print(vardict3)

# not possible
# vardict3 = vardict - vardict2
# vardict3 = vardict & vardict2
# vardict3 = vardict ^ vardict2

