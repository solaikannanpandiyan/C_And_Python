# SET CONCEPTS -> only unique keys

def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()
    
# definition
varset = {1,2}
printformat(varset)
varset = set()
printformat(varset)
varset = {1,3.3,"hello",'2'}
printformat(varset)
# varset = {[1,2,3]} # mutability and not hashable
# printformat(varset)
# varset = {{1,2,3}} # mutability and not hashable
# printformat(varset)
# varset = {1,2,{1:1,2:2,3:3}} # mutability and hashable
# printformat(varset)
varset = {1,2,(1,2,3)} # immutable <-> hashable (consitent)
# we can store: numbers, string, tuple of  string, tuple, or number
printformat(varset)

# indexing - no ordering -> no subscript operation
varset = {1,3.3,"hello",'2'}
# printformat(varset[1]) -> no allowed

# slicing
# not allowed

# Mutability
varset = {1,2,3}
printformat(varset)
varset.add(4)
printformat(varset)

# Common Methods in Set Class
varset1 = {1,2,3}
varset2 = {3,4,5}
varset3 = {7,8,9}
# printformat(varset1)
# varset1.update(varset2, varset3)
# printformat(varset1)

varset1.difference(varset2) # A -
printformat(varset1)

set1 = {1,2,3}
set2 = {1,2,3}
print(set1.issubset(set2)) # True
print(set1.issuperset(set2)) # False -> True

# Iteration
set1 = {1,2,3}
for i in set1: # list, tuple, set
    print(i)
 
# Set Comprehensions -> list, tuple, set
set1 = {i for i in range(10)}
print(set1)

# Nested Set -> not possible
# sett = {tuple({1,2,3}), tuple({4,5,6}), tuple({7,8,9})}
# print(sett)

# Shallow Copy -> list, set 
# varr = ("a","1",[1,2,3,4,5])
# sett = {varr}
# printformat(varr)
# sett2 = sett.copy()
# printformat(sett.pop())


# Set Unpacking - > doable
# *args, **kwargs
a,b,c = {1,2,6}
print(a)
print(b)

# Inbuilt methods -> len, filter, map, sorted
set1 = {i for i in range(10)}
print("len : ",len(set1))
print("list : ",list(set1)) # list, set, tuple, dict
print("filter : ",list(filter(lambda x: x%2 ==0, set1)))
print("map : ",list(map(lambda x: print(x,sep=" "),set1)))
print("sorted : ", list(sorted(set1)) )
# print("filter : ",list())

# operations ->  |, &, -, ^
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# | for union.
# & for intersection.
# - for difference.
# ^ for symmetric difference -> (A-B) U (B-A)
print(set1 | set2)  # 1,2,3,4,5
print(set1 & set2)  # 3
print(set1 - set2)  # 1,2
print(set1 ^ set2)  # 1,2,4,5
print((set1 - set2) | (set2 - set1)) # 1,2,4,5
# print(set1 + set2) -> not possible
# print(set1 * 2) -> not possible
