class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        print("add called")
    
    def __mul__(self, other):
        print("mul called")
        
    def __sub__(self, other):
        print("sub called")
    
    def __neg__(self, other):
        print("sub called")
        
    def __len__(self):
        print("len() is called")
    
    def __getitem__(self, key):
        print("subcript called")
        
pt1 = coordinate(10,2)
pt2 = coordinate(10,2)
pt1 + pt2
pt1 - pt2
pt1 * pt2
pt1[""]