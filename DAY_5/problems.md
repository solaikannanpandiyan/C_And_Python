1. build a calculator function:

```python
def calculate(x, y, operation):
   if operation == "*":
      return x*y # continue logic

x = calculate(2,3,"\*")
print("output : ",x)
```

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

2. implement fizzbuzz logic
   take no x,
   case 1: if x is divisible by 3 alone print "fizz"
   case 2: if x is divisible by 5 alone print "buzz"
   case 3: if x is divisible by 3 and 5 print "fizzbuzz"
   case 4: if x is not divisible by both 3 and 5 print "not divisible"

3. Implement pagination using below
   for loop
   range
   break
   continue
   consider 100 pages you need start printing pages from start to end
   if start = 20, end = 27 print pages 20 -> 27

Additional: do the same using while loop

4. print numbers in reverse from 100, skips onces divisible by 3 and 5,

5. print below pattern using loops:
   even places are reversed
   odd places are normal

```python
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
```
