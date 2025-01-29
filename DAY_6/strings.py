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
printformat(strng[0])
printformat(strng[3])


# string slicing
# strng = "apple"
# printformat(strng)
# printformat("apple")
# string slicing [start:stop:step]
# printformat(strng[0:3])
# printformat(strng[::-1])
# printformat(strng[:100])


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
