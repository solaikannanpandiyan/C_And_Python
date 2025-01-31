# Tuples CONCEPTS
def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()
    
# definition
tup = tuple([1,2,3,4]) # inbuild function for creation adn type casting
print(tup)
tup = (1,2,3,4)
print(tup)
tup = (1,2.2,"wow",['a','b'],{"hel","wow"},{1:"one",2:"two"})
print(tup)

# indexing
print("indexing")
tup = tuple([i for i in range(1,11)])
print(tup)
print(tup[8]) # 9
print(tup[0]) # 1

# slicing
print("slicing")
tup= (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
#   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     ^     ^
print(tup[1:4]) # 9, 8, 7
print(tup[1:4:2]) # 9, 7
print(tup[1:4:-1]) # empty ()
print(tup[5:2:-1]) # 5, 6, 7
print(tup[5:2:1]) # empty ()

# Mutability
tup= (10, 9)
# tup[1] = 1  -> wont work because immutable
tup= (10, [1,2,3])
# tuples data cannot be changes
# [1,2,3] is stored in different location
# tup= (10, address of [1,2,3])
# list, tuple, dict, set -> complex datatype
tup[1][1] = "hello"
print(tup)
# tup[1] = [4,5,6] # not allowed -> address is reassinged
tup= (10, "hii")
# tup[1] += " how are you" # not allowed
# tup[1] = tup[1] + " how are you" 

# Common Methods in tuple Class
# visit doc

# Iteration
tup = (1,2,3,4,5)
for i in tup:
    print(i, end= " ")
print()

# Tuple Comprehensions
print("Tuple Comprehensions")
print(tup)
tup = tuple(i for i in range(1,11))
print(tup)
tup = tuple([i for i in range(1,11)])
print(tup)

# Nested Tuples
print("Nested Tuples")
tup = tuple( tuple(j for j in range(1,11)) for _ in range(1,11))
print(tup)
# tup[0] = ()
# tup[0][0] = 10

# Shallow Copy
# to be explored

# tuple Unpacking
a,b,c = (1,2,3)
print(a,b,c)

# Inbuilt methods -> len, filter, map, sorted
print("Inbuilt methods")
tup = (1,2,3)
print(len(tup))
print(tuple(filter(lambda x: x%2,tup)))
print(tuple(map(lambda x: print(f"mapped: {x}"),tup)))
# no inplace sorting available in tuple
# if there is sorting there is always comparison
# 2 values without comparing no sorting works
print(tuple(sorted(tup,reverse=True)))
print(tup)


# operations ->  concat and repition
print("Operations")
tup1 = (1,2,3)
printformat(tup1)
tup2 = (1,2,3)
printformat(tup2)
tup1 = tup1 + tup2
printformat(tup1)

tupinput = (1,2,3)
printformat(tupinput)
tupinput = tupinput * 3
printformat(tupinput)
# printformat(tuprep)