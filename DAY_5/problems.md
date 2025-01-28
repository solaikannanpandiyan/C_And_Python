1. build a calculator function:
   def calculate(x, y, operation):
   if operation == "*":
   return x*y # continue logic

x = calculate(2,3,"\*")
print("output : ",x)

# should work for all below opertions

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
