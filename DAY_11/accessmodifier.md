In Python, access modifiers (or visibility modifiers) determine the accessibility of class attributes and methods. Python doesn't have explicit keywords like `public`, `private`, or `protected` found in other languages (e.g., Java or C++). However, Python uses naming conventions to indicate the intended visibility of class attributes and methods.

### 1. **Public Members**:
   - **Public** members are accessible from both inside and outside the class.
   - By default, all attributes and methods are public unless specified otherwise.
   
   **Example**:
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name  # Public attribute
           self.age = age    # Public attribute

       def greet(self):
           print(f"Hello, my name is {self.name}.")  # Public method
   ```

   **Usage**:
   ```python
   person = Person("Alice", 30)
   print(person.name)  # Accessing public attribute
   person.greet()      # Calling public method
   ```

### 2. **Protected Members**:
   - **Protected** members are intended to be accessible only within the class and its subclasses (inherited classes). In Python, this is done using a single underscore (`_`) prefix.
   - This is a convention, not a strict enforcement. It signals to the programmer that these members should not be accessed directly, but it is still possible to do so.

   **Example**:
   ```python
   class Person:
       def __init__(self, name, age):
           self._name = name  # Protected attribute
           self._age = age    # Protected attribute

       def _greet(self):      # Protected method
           print(f"Hello, my name is {self._name}.")
   ```

   **Usage**:
   ```python
   person = Person("Bob", 25)
   print(person._name)  # Technically accessible, but should be avoided
   person._greet()      # Technically accessible, but should be avoided
   ```

### 3. **Private Members**:
   - **Private** members are intended to be accessible only within the class itself. This is done using a double underscore (`__`) prefix.
   - This is also a convention, but Python uses name mangling to make it harder (but not impossible) to access private members outside the class.
   - When you use double underscores, Python changes the name of the variable internally (name mangling), making it less likely to be accidentally accessed.

   **Example**:
   ```python
   class Person:
       def __init__(self, name, age):
           self.__name = name  # Private attribute
           self.__age = age    # Private attribute

       def __greet(self):      # Private method
           print(f"Hello, my name is {self.__name}.")
   ```

   **Usage**:
   ```python
   person = Person("Charlie", 35)
   # The following will raise an AttributeError since __name is private
   # print(person.__name)

   # However, you can access it using the mangled name:
   print(person._Person__name)  # Accessing private attribute (not recommended)
   ```

### 4. **Summary of Access Modifiers**:
   - **Public**: No prefix (accessible from anywhere).
   - **Protected**: Single underscore (`_`) prefix (intended for internal use or subclasses).
   - **Private**: Double underscore (`__`) prefix (name mangling, intended to prevent access outside the class).

### Access Modifier Usage Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Public
        self._age = age   # Protected
        self.__password = "secret"  # Private

    def show_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Password: {self.__password}")

p = Person("John", 40)
print(p.name)  # Access public attribute
print(p._age)  # Access protected attribute (possible, but not recommended)
# print(p.__password)  # This will raise an error
print(p._Person__password)  # Access private attribute via name mangling
```

While Python does not strictly enforce access control, these conventions help organize code and maintain proper encapsulation by signaling the intended use of attributes and methods.