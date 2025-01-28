Python provides a variety of **operators** that are used to perform operations on variables and values. These operators are categorized into different types based on their functionality. Below is a detailed explanation of each type of operator and its usage:

---

### **1. Arithmetic Operators**

Used to perform mathematical operations.

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |
| `//`     | Floor Division      | `5 // 2` | `2`    |

---

### **2. Comparison Operators**

Used to compare two values.

| Operator | Description              | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 3` | `False` |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `5 < 3`  | `False` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | Less than or equal to    | `5 <= 3` | `False` |

---

### **3. Logical Operators**

Used to combine conditional statements.

| Operator | Description                            | Example               | Result  |
| -------- | -------------------------------------- | --------------------- | ------- |
| `and`    | True if both conditions are true       | `(5 > 3) and (2 < 4)` | `True`  |
| `or`     | True if at least one condition is true | `(5 > 3) or (2 > 4)`  | `True`  |
| `not`    | Reverses the result                    | `not (5 > 3)`         | `False` |

---

### **4. Assignment Operators**

Used to assign values to variables.

| Operator | Description             | Example   | Equivalent to |
| -------- | ----------------------- | --------- | ------------- |
| `=`      | Assign                  | `x = 5`   | `x = 5`       |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 3`  | `x = x - 3`   |
| `*=`     | Multiply and assign     | `x *= 3`  | `x = x * 3`   |
| `/=`     | Divide and assign       | `x /= 3`  | `x = x / 3`   |
| `%=`     | Modulus and assign      | `x %= 3`  | `x = x % 3`   |
| `**=`    | Exponent and assign     | `x **= 3` | `x = x ** 3`  |
| `//=`    | Floor divide and assign | `x //= 3` | `x = x // 3`  |

---

### **5. Bitwise Operators**

Used to perform operations on binary numbers.

| Operator | Description | Example    | Result |
| -------- | ----------- | ---------- | ------ |
| `&`      | Bitwise AND | `5 & 3`    | `1`    |
| '\|'     | Bitwise OR  | `5 \| 1`   | `5`    | 
| `^`      | Bitwise XOR | `5 ^ 3`    | `6`    |
| `~`      | Bitwise NOT | `~5`       | `-6`   |
| `<<`     | Left shift  | `5 << 1`   | `10`   |
| `>>`     | Right shift | `5 >> 1`   | `2`    |

---

### **6. Membership Operators**

Used to test if a value is present in a sequence (e.g., list, tuple, string).

| Operator | Description                | Example              | Result |
| -------- | -------------------------- | -------------------- | ------ |
| `in`     | True if value is found     | `"a" in "apple"`     | `True` |
| `not in` | True if value is not found | `"b" not in "apple"` | `True` |

---

### **7. Identity Operators**

Used to compare the memory locations of two objects.

| Operator | Description                                            | Example      | Result         |
| -------- | ------------------------------------------------------ | ------------ | -------------- |
| `is`     | True if both variables point to the same object        | `x is y`     | `True`/`False` |
| `is not` | True if both variables do not point to the same object | `x is not y` | `True`/`False` |

---

### **8. Ternary Operator**

A shorthand for an `if-else` statement.

| Syntax                  | Description                                | Example             | Result |
| ----------------------- | ------------------------------------------ | ------------------- | ------ |
| `x if condition else y` | Returns `x` if condition is true, else `y` | `5 if 2 > 1 else 0` | `5`    |

---

### **Examples of Operator Usage**

#### Arithmetic Operators

```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a ** b) # Output: 1000
```

#### Comparison Operators

```python
x = 5
y = 10
print(x < y)  # Output: True
print(x == y) # Output: False
```

#### Logical Operators

```python
print((5 > 3) and (2 < 4))  # Output: True
print(not (5 > 3))          # Output: False
```

#### Assignment Operators

```python
x = 5
x += 3
print(x)  # Output: 8
```

#### Bitwise Operators

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(a & b)  # Output: 1 (Binary: 0001)
```

#### Membership Operators

```python
fruits = ["apple", "banana"]
print("apple" in fruits)  # Output: True
```

#### Identity Operators

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False (different objects)
```

#### Ternary Operator

```python
result = "Even" if 10 % 2 == 0 else "Odd"
print(result)  # Output: Even
```

---

Let me know if you need further clarification or examples!
