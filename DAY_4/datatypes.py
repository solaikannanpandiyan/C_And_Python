# from .pythonbasics import printformat
    
    
def examplelen(obj):
    return obj.__len__()
    
if __name__ == "__main__":
    # datatype methods and inbuild functions
    a = 10  # class int
    # normal methods
    # 8 4 2 1
    # 1 0 1 0
    # print(a)
    
    # dunder methods or magic methods
    a = -10.5 
    
    print(a.__floor__())
    # a = [1,2,3,4,5] 
    a = "hello"
    # how inbuild methods works using dunder or magic methods
    # use magic or dunder to work
    print(examplelen(a))
    print(a.__len__())
   
    # printformat(a)
    # a = 4.4
    # printformat(a)
    # a = 3 + 4j
    # printformat(a)
    
    # # random address ->hashfunction -> unique number
    # # Boolean
    # a = True # both literal and keyword
    # a = False # both literal and keyword
    # a = None 
    # a
    
    # # # String
    # a = 'h'
    
    # # Sequence
    # # List -> ordered
    # a = [1 , 'a', 5.5]
    # # xdynamic/static -> size runtime automically increased
    # # xhetorogeneous/homogenous -> can contain any type of data
    # # xmutuable/immutable -> mutable
    # # [] -> delimiter
    # # , -> delimiter
    # # 1 -> int
    # # 'a' -> str
    # # 5.5 -> float
    # printformat(a)
    # # Tuple -> ordered
    # a = (1 , 'a', 5.5)
    # # xheterogeneous
    # #-> dynamic/xstatic
    # #-> ximmutable
    
    # printformat(a)
    # # Set -> unordered
    # a = {1, 2, 'a'}
    # # sample hash value: {1001, 1003, 1004} // also a number
    # # [1, 3, 4]
    # # 'a' -> 1004
    # # data -> consitent hashing hash function -> unqiue hashvalue
    # # no duplicates
    # # 
    # # xdynamic/static -> size runtime automically increased
    # # xhetorogeneous/homogenous -> can contain any type of data
    # # xmutuable/immutable -> mutable
    # printformat(a)
    
    # # # Mapping
    # # Dict -> key, value -> very very common, very important -> 90% problem
    # # othername: hashmap, map, dict, 
    # a = {1 : 'one', 2: 'two', 3:'three', 4: 1.1}
    # # sample hash value: {1001, 1003, 1004} // also a number
    # # 'one' 'two' 'three'
    # # ll      ll     ll
    # #  ^       ^      ^
    # # [1,       3,    4]
    # # 'a' -> 1004
    # # data -> consitent hashing hash function -> unqiue hashvalue
    # # no duplicate keys
    # # 
    # # xdynamic/static -> size runtime automically increased
    # # xhetorogeneous/homogenous -> can contain any type of data
    # # xmutuable/immutable -> mutable
    # printformat(a)
    
    # # # print(id("hello"))
    
    
    
    
    
    