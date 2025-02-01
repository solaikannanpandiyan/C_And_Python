def printformat(a):
    print()
    print("Data : ", a)
    print("Type of data : ", type(a))
    print("Id of data:", id(a))
    print()

# # # String
# a = 'h'
# # '' -> delimiter
# printformat(a)
# a = "i"
# # "" -> delimiter
# printformat(a)
# a = 'hello'
# printformat(a)
# a = "wonderful \
# hello"
# printformat(a)
# a = '''
# hello today is first day in python.
# '''
# printformat(a)

# Some Common String methods: 

# teststring = "hello {} how are you!"
# # fstring alternative
# x = 10
# y = 12
# out = f"the sum of x and y is {x+y}"
# print(out)

# out = teststring.format("arun")
# print(out)

# out = " ".join(("hello", "world","!!"))
# print(out)

# teststring = "hello how are you!"
# out = teststring.capitalize()
# print(out)
# out = teststring.replace("hello", "Goodday")
# print(out)
# out = teststring.split("h",1)
# print(out)
# teststring = "   hello, how are you!  "
# out = teststring.strip()
# print(out)
# teststring = "hello, how are you!"
# out = teststring.count("hello",0,len(teststring)-1)
# print(out)
# out = teststring.find("hell")
# print(out)
# out = teststring.partition(" ")
# print(out)
# out = teststring.index("how")
# print(out)


# accessing character
strng = "apple"
#        012345
#      -5-4-3-2-1
# strng = "green apple"
# len() -> number -2 
# [] -> array
printformat(strng[0]) # a
printformat(strng[3]) # l
printformat(strng[-1]) # e -> negative indexing
# printformat(strng[10]) # -> error
# printformat(strng[-10]) # -> error

# string slicing
strng = "apple"
printformat(strng)
printformat("apple")

# string slicing [start:stop:step] -> range(), step: 1
printformat(strng[0:3]) # app 
printformat(strng[::-1]) # elppa
printformat(strng[:100]) # error | xapple | orange
printformat(strng[4:1:-1]) # lpp | lp | xelp | elpp
# a p p l e
# 0 1 2 3 4
printformat(strng[1:4:-1]) # elpp | error | xnoerror ""
printformat(strng[4:1:1]) #  error | xnoerror ""

# concatenation
str1 = "hello"
str2 = "world"
printformat(str1 + str2)
printformat(str1.__add__(str2))

# repetition
str1 = "hello"
printformat(str1 * 3)
printformat(str1.__mul__(3))

# length of string
printformat(len(str1))
printformat(str1.__len__())

# membership
str1 = "apple is good for health"
printformat("good for" in str1)

# comparison -> lexicographical
str1 = "apple" # latter is always larger
str2 = "america" # earlier is always smaller
# a --->   m    n   o    p
# 97      109 110  111  112
printformat(str1<str2) # False | True
# 112 < 109 = false
printformat(str1 == str2) # False
# 112 < 109 = false
printformat(str1 > str2) # False
# 112 > 109 = false

# iteration
str1 = "" 
rev = str1[::-1]

for character in rev:
    print(character)

character = ""
print(character in str1)

# while character in rev:
#     print(character)\n

# escape characters or raw string
# wirwqoioav13417~`002\]`
# \n
print("apple a\nnbanana")
print("Good\t\tday")
print("Good day, \"life is beautiful\"")
print("Good day, \'life is beautiful\'")
print("Good day,\\tlife is beautiful\\n")
# print("\a")
print("Good day   ,\vhwo are you!.")
# https://docs.python.org/3/reference/lexical_analysis.html
# rawstring
print(r"asofjqoi\n\n\\'''''232''98223")
# byte string
# "".encode("utf-8")
print(b"hello")


# getting input
# input(stdin) -> python program -> output(stdout)
# inputdata = input("please enter ur name: ") # user data from stdin
# printformat(inputdata)

# type casting - implicit | explicit
# print("string" + 3)
print("number ", str(3))
# inbuild function
# str()
# int()
# float()
inpt = '13'
printformat(inpt)
# precheck and convert
# if inpt.isdigit():
#     inpt = int(inpt)
#     printformat(inpt)
# else:
#     print("not a valid number")

# exception handling
# try:
#     inpt = int(inpt)
#     printformat(inpt)
# except Exception as err: # alias
#     print(f"value is not int{err}")
# finally:
#     # to execute a closeup code, that should always execute
#     print("this is finally always executed")

# inputdata = input("please enter a value: ") # user data from stdin
# printformat(inputdata)
# inputdata = str(int(inputdata))
# printformat(inputdata)

# valid
# 4 numbers seperated by .(delimiter)
# each number should be between 0 - 255
# 0.0.0.0 -> min valid
# 255.255.255.255 -> max valid


# immutability
# different address on each manipulation
# python string -> mutable/ximmutable
# x = "hello" # string pool | interning 
# y = "hello"
# printformat(x)
# printformat(y)
# printformat("hello")


# # x = x + " world"
# x = "Hello world% asef! af"
# y = "Hello world% asef! af"
# printformat(x)
# printformat(y)

# c = "hello world, this is a long string"
# d = "hello world, this is a long string"
# print(c is d)  # Output: False
# x = "hi"
# printformat(x)
# x[0] = 'b' -> cannot change

x = "world"
printformat(x)
x = x.replace('w','g')
printformat(x)




