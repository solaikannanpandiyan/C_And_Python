 
def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()
    
if __name__ == "__main__":
    # literals are objects in python 
    # Numbers
    a = 10 # a -> identifier, 10 -> literal, datatype
    # \t, \n -> raw file to understand code seperation
    # dynamically(runtime) typed
    # int a = 10; 
    # a -> identifier
    # int -> datatype
    # ; -> seperator
    printformat(a)
    a = 4.4
    printformat(a)
    a = 3 + 4j
    printformat(a)
    
    # random address ->hashfunction -> unique number
    # Boolean
    a = True # both literal and keyword
    # None = 10
    printformat(a)
    a = False # both literal and keyword
    printformat(a)
    a = None 
    printformat(a)
    
    # # String
    a = 'h'
    # '' -> delimiter
    printformat(a)
    a = "i"
    # "" -> delimiter
    printformat(a)
    a = 'hello'
    printformat(a)
    a = "wonderful \
    hello"
    printformat(a)
    a = '''
    hello today is first day in python.
    '''
    # ''' ''' -> delimiter
    printformat(a)
    
    # Sequence
    # List -> ordered
    a = [1 , 'a', 5.5]
    # xdynamic/static -> size runtime automically increased
    # xhetorogeneous/homogenous -> can contain any type of data
    # xmutuable/immutable -> mutable
    # [] -> delimiter
    # , -> delimiter
    # 1 -> int
    # 'a' -> str
    # 5.5 -> float
    printformat(a)
    # Tuple -> ordered
    a = (1 , 'a', 5.5)
    # xheterogeneous
    #-> dynamic/xstatic
    #-> ximmutable
    
    printformat(a)
    # Set -> unordered
    a = {1, 2, 'a'}
    # xdynamic/static -> size runtime automically increased
    # xhetorogeneous/homogenous -> can contain any type of data
    # xmutuable/immutable -> mutable
    printformat(a)
    
    # # Mapping
    # # Dict
    # a = {1 : 'one', 2: 'two', 3:'three'}
    # printformat(a)
    
    # # print(id("hello"))
    
    
    
    
    
    