Magic methods (also called **dunder methods**) in Python enable built-in behaviors for custom objects. Here are some important ones:

### **Object Creation & Initialization**

- `__new__(cls, *args, **kwargs)`: Controls instance creation (before `__init__`).
- `__init__(self, *args)`: Initializes a new object.
- `__del__(self)`: Called when an object is about to be destroyed.

### **String Representation**

- `__str__(self)`: Returns a human-readable string (used by `print()`).
- `__repr__(self)`: Returns an official string representation (used by `repr()`).

### **Arithmetic Operators**

- `__add__(self, other)`: `self + other`
- `__sub__(self, other)`: `self - other`
- `__mul__(self, other)`: `self * other`
- `__truediv__(self, other)`: `self / other`
- `__floordiv__(self, other)`: `self // other`
- `__mod__(self, other)`: `self % other`
- `__pow__(self, other)`: `self ** other`
- `__neg__(self)`: `-self`

### **Comparison Operators**

- `__eq__(self, other)`: `self == other`
- `__ne__(self, other)`: `self != other`
- `__lt__(self, other)`: `self < other`
- `__le__(self, other)`: `self <= other`
- `__gt__(self, other)`: `self > other`
- `__ge__(self, other)`: `self >= other`

### **Container & Iteration**

- `__len__(self)`: `len(self)`
- `__getitem__(self, key)`: `self[key]`
- `__setitem__(self, key, value)`: `self[key] = value`
- `__delitem__(self, key)`: `del self[key]`
- `__contains__(self, item)`: `item in self`
- `__iter__(self)`: Returns an iterator (`for item in self:`).
- `__next__(self)`: Returns the next item in iteration.

### **Callable & Context Manager**

- `__call__(self, *args, **kwargs)`: Makes an object callable like a function.
- `__enter__(self)`: Defines behavior for `with` statements.
- `__exit__(self, exc_type, exc_value, traceback)`: Handles exit for `with`.

### **Attribute Access**

- `__getattr__(self, name)`: Called when accessing a missing attribute.
- `__setattr__(self, name, value)`: Called when setting an attribute.
- `__delattr__(self, name)`: Called when deleting an attribute.
- `__dir__(self)`: Controls `dir(self)`.

