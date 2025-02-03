# Function-Based Problems

## 1. Function Call Counter Decorator

### Problem Description
Create a decorator `count_calls` that keeps track of how many times a function has been called. The count should be stored as an attribute of the function.

### Boilerplate Code
```python
from functools import wraps

def count_calls(func):
    # Implement the decorator here
    pass

@count_calls
def example_function():
    print("Function called")

example_function()
example_function()

print(f"example_function has been called {example_function.call_count} times")
```

---

## 2. Calculator with Operations Stored in a Collection

### Problem Description
Design a calculator that supports multiple operations (addition, subtraction, multiplication, division) by storing them in a dictionary or list.

### Boilerplate Code
```python
def add(a, b):
    pass

def subtract(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def calculate(operation, a, b):
    pass

# Example usage
print(calculate("add", 5, 3))  # Expected output: 8
```

---

## 3. Memoization Decorator

### Problem Description
Implement a decorator `memoize` that caches function results to optimize repeated calls with the same inputs.

### Boilerplate Code
```python
from functools import wraps

def memoize(func):
    # Implement the memoization logic
    pass

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Expected output: 55
```

---

## 4. Function Execution Timer

### Problem Description
Write a decorator `execution_time` that measures and prints the execution time of a function.

### Boilerplate Code
```python
import time
from functools import wraps

def execution_time(func):
    # Implement timing logic
    pass

@execution_time
def slow_function():
    time.sleep(2)
    print("Finished")

slow_function()
```

---