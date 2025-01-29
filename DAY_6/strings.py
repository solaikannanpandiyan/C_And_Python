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
str2 = "wor"

# repetition

# lenght of string

# membership

# comparison

# iteration

# escape characters or raw string

# getting input
