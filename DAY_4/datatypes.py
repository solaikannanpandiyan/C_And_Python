# from .pythonbasics import printformat
    
import sys as s
def examplelen(obj):
    return obj.__len__()
    
if __name__ == "__main__":
    # datatype methods and inbuild functions
    a = 10  # class int
    # normal methods
    # 8 4 2 1
    # 1 0 1 0
    # print(a)
    s.maxsize()
    # dunder methods or magic methods
    a = -10.5 
    
    print(a.__floor__())
    # a = [1,2,3,4,5] 
    a = "hello"
    
    # how inbuild methods works using dunder or magic methods
    # use magic or dunder to work
    # print(examplelen(a))
    # print(a.__len__())

    var1 = "hello"
    var2 = "world"
    # var1  = var1.upper()
    # array | list, string -> interview 
    print(var1.upper())
    print(var1.isupper())
    print(var1 + var2)
    print()

    # python advantage
    # very good prototyping language -> low level design:  http implemention, cache, redis(key value), simple database 
    # very good interview language -> product - > language agnostic 
    # python -> performance improvment ->
    # GIL lock (python performace backslash)
    # 3 ways to do things better, 
    # multithreading(inefficient due GIL), -> for io
    # multiprocessing(faster), -> for cpu processing
    # asyncio(efficient) but not always possible -> fastapi(multi-processing and asyncio)
    # verh high -> 1 -> datascience/ dataengineering -> AI/ML
    #   python is 3% -> core concepts -> pandas, numpy, pyspark(distrubed), | cloudserver data
    # high -> 2 -> support enginerring, automation,  scripting, webscrapping, devops(good opportunities)(ansible, kubernetes, docker, jenkins, linux fundamentals)
    # mediocre -> 3 -> web developer -> django, fastapi(rest api), flask -> sparse (startups, or midlevel product) -> not too much recommended

    # problem solving:
    # lot inbuilt function, clean code, simple sytax
    # logic solve -> |  implementation simple

    # disadvantage:
    # tortoise level slow -> less efficient
    # heavy memory usage -> less efficient
    # job opportunities -> money -> not much unless u go into datascience 
    # or devops that required learning more technologies and concepts

    
    
   
    
    
    
    
    
    