
# FOR LOOP and RANGE


# always start from start value
# always return till a step value smaller
# than or greater than stop based on step value
# the values increment or decrements by count    
# -3 -2 -1 0 1 2 3 4
# ------------------> number line 
# which is greater -1 or -3 ? -1


def algorithm():
    pass

algorithm()


for i in range(1,5): # 1, 2, 3, 4
    # print(i)
    pass
    

for i in range(1,5,2): # 1, 3
    # print(i)
    pass
    
for i in range(1,-4,-1): 
# 1, 0, -1, -2, -3
    # print(i) 
    pass
    
for i in range(1,-4,-1): 
# 1, 0, -1, -2, -3
    # print(i) 
    pass

for i in range(1,4,-1): 
# 1, 0, -1, -2, -3
    print(i) 
    
# -32,768 to 32,767
# 1, 0, -1, -2, ... -32,768, 32,767, 32,766, ..... 6, 5

# range(1,3,1)
# start = 1
# stop = 3
# step = 1
# start < stop and step is positive
# start > stop and step is negative
# lastvalue = 1 < stop
# lastvalue + step = 1 + 1 = 2 < stop
# lastvalue + step = 2 + 1 = 3 < stop = false
# 1 , 2
