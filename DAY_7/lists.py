def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()

# LIST CONCEPTS

# definition
varlst = []
print(varlst)
varlst = list()
print(varlst)
varlst = [1,2,3]
print(varlst)
varlst = [1,1.3,"good", [3,4,5], ('a','b','c'),{"one":1, "two":1}]
print(varlst)
# json -> list of dictionary, dictionary of list, dictionary of set
# int, float, str, list, tuples, dictionary, set

# indexing
print(varlst[0]) # 1
print(varlst[2]) # good
print(varlst[3]) # [3,4,5]
print(varlst[3][2]) # 5
print(varlst[4][1]) # 'b'
print(varlst[5]["one"]) # 1
 
# slicing -> string, list, tuple
varlst = [1,2,3,4,5]
#         0 1 2 3 4
# start: stop: step
# each start + step till it reaches stop
# while( start + step < stop)
#       print(varlst[start + step])
print(varlst[3:1:-1]) # 3, 2, 1 |  4, 3
print(varlst[2:4:2]) # 2 | 3
print(varlst[2:4:-1]) # [] -> 

# Mutability
varlst = [1,2,3,4,5]
printformat(varlst)
varlst[0] = 'a'
printformat(varlst)

# Common Methods in List Class
varlst = [1,2,3,4,5]
printformat(varlst)
print(varlst.append(6))
print(varlst.index(4))
print(varlst.count(3))
varlst.reverse()
print(varlst)
print(varlst.pop())
printformat(varlst)

# Iteration
for i in varlst:
    print(i)

# List Comprehensions
print(" List Comprehensions")
# 0 -> 100 all even numbers
data = [x for x in range(101) if x%2 == 0] #100
print(data)



# Nested Lists
print("Nested Lists")
# 3 x 3 list
data = [ [j for j in range(1,4)] for _ in range(3) ] #100
print(data)
# print([["*" for j in range(1,4)] for i in range(1,4)])

# Shallow Copy -> not only for python
print("Shallow Copy")
# shallow copy
# list(address:99) -> list(address:100) -> list(address:101)
# listnew(address:89) -> list(address:100) -> list(address:101)
# deep copy
# list(address:100) -> list(address:103) -> list(address:104)
# listnew(address:107) -> listnew(address:108) -> listnew(address:109)
list1 = ["apple","banana","grape"]
list2 = list1.copy()
list2[0] = "tomato"
printformat(list1) # ["apple","banana","grape"]
printformat(list2) # ["tomato","banana","grape"]

list1 = ["apple","banana",[1,2,3,4,5]]
#         string  string    reference: (list, dict set, tuple)
list2 = list1.copy() # shallow copy
list2[2][1] = "orange"
list2[1] = "grape"
printformat(list1) # ["apple","banana",[1,"orange",3,4,5]]
printformat(list2) # ["apple","grape",[1,"orange",3,4,5]]

# default -> shallow copy
# deep copy -> compute intensive, memory intensive
import copy
list1 = ["apple","banana",[1,2,3,4,5]]
list2 = copy.deepcopy(list1)
list2[2][1] = "orange"
printformat(list1[2]) # ["apple","banana",[1,2,3,4,5]]
printformat(list2[2]) # ["apple","banana",[1,"orange",3,4,5]]

# List Unpacking
fruit1, fruit2 = ["apple","banana"]
print(fruit1, fruit2)


# operations ->  concat and repetition
# list3 = ["apple","banana"] + ["orange"]
# printformat(list3)
# list3 = ["apple","banana"] * 2
# printformat(list3)


# Inbuilt methods -> len, filter, map, sorted
# list of number from 1 to 50

# all odd numbers
lst = []
for i in range(1,51):
    if i % 2 == 0:
        lst.append(i)
print(lst)

# step 2
def evenno(x):
    if x % 2 ==0:
        return True
    else:
        return False

lst = [i for i in range(1,51)] # 1 -> 50
# print(len(lst))
# for j in filter(evenno,lst):
#     print(j)
# filter(evenno,lst)
print(list(filter(evenno,lst)))


# step 3
# readablity
print(list(filter(lambda x:  x%2 ==0,[i for i in range(1,51)])))

def check():
    print(f"check")


# map
lst = [i for i in range(1,6)]
# map(lambda x: print(f"this is printed using map: {x}"),lst)
for _ in map(lambda x: print(f"this is printed using map: {x}"),lst):
    pass
    
# print(check())
# this is printed using map: 1
# this is printed using map: 2
# this is printed using map: 3
# this is printed using map: 4
# this is printed using map: 5
lst = ["varun", "ajay", "kamal"]
#        5        4        5
#        5        5        4
# relative ordering is preserved in both sorting
# inplace or outofplace -> memory complexity
# time complexity -> how much time takes (best: O(nlogn))
# relative ordering -> preserved or not
printformat(lst)
lst.sort(key=lambda x: len(x),reverse=True) # inplace sorting
printformat(lst)
lst = sorted(lst, key=lambda x: len(x), reverse=True)
printformat(lst)
lst = [["varun",4], ["ajay",0], ["kamal",1]]
lst = sorted(lst, key=lambda x: x[0]) # correct or any other approach
printformat(lst)


# how to do it
lst = [{5:"kamal"}, {9:"varun"}, {0:"varun"}]
for i in lst:
    print(list(i.keys())[0])
# lst = sorted(lst, key=lambda x: list(x.keys())[0]) # correct or any other approach
# printformat(lst)



