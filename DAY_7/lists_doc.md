### Lists in Python: Core and Advanced Concepts

#### **Core Concepts**

1. **Definition**:

   - A list in Python is an ordered, mutable collection of elements. It can store elements of different data types (e.g., integers, strings, other lists, etc.).
   - Lists are defined using square brackets `[]`, with elements separated by commas.

   ```python
   my_list = [1, 2, 3, "hello", 5.5]
   ```

2. **Indexing**:

   - Lists are zero-indexed, meaning the first element is at index `0`.
   - Negative indexing is also supported, where `-1` refers to the last element.

   ```python
   print(my_list[0])   # Output: 1
   print(my_list[-1])  # Output: 5.5
   ```

3. **Slicing**:

   - You can extract a sublist using slicing with the syntax `[start:stop:step]`.
   - `start` is inclusive, `stop` is exclusive, and `step` determines the interval.

   ```python
   print(my_list[1:4])  # Output: [2, 3, "hello"]
   print(my_list[::2])  # Output: [1, 3, 5.5]
   ```

4. **Mutability**:

   - Lists are mutable, meaning you can change their elements after creation.

   ```python
   my_list[0] = 100
   print(my_list)  # Output: [100, 2, 3, "hello", 5.5]
   ```

5. **Common Methods**:

   - `append()`: Adds an element to the end of the list.
   - `extend()`: Adds multiple elements (from another iterable) to the end.
   - `insert()`: Inserts an element at a specific index.
   - `remove()`: Removes the first occurrence of a value.
   - `pop()`: Removes and returns an element at a specific index (default is the last element).
   - `index()`: Returns the index of the first occurrence of a value.
   - `count()`: Returns the number of occurrences of a value.
   - `sort()`: Sorts the list in place.
   - `reverse()`: Reverses the list in place.

   ```python
   my_list.append(6)          # [100, 2, 3, "hello", 5.5, 6]
   my_list.extend([7, 8])     # [100, 2, 3, "hello", 5.5, 6, 7, 8]
   my_list.insert(1, 200)     # [100, 200, 2, 3, "hello", 5.5, 6, 7, 8]
   my_list.remove("hello")    # [100, 200, 2, 3, 5.5, 6, 7, 8]
   popped = my_list.pop(2)    # popped = 2, list = [100, 200, 3, 5.5, 6, 7, 8]
   ```

6. **Length**:

   - Use the `len()` function to get the number of elements in a list.

   ```python
   print(len(my_list))  # Output: 7
   ```

7. **Iteration**:

   - You can iterate over a list using a `for` loop.

   ```python
   for item in my_list:
       print(item)
   ```

---

#### **Advanced Concepts**

1. **List Comprehensions**:

   - A concise way to create lists using a single line of code.
   - Syntax: `[expression for item in iterable if condition]`.

   ```python
   squares = [x**2 for x in range(10)]
   print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```

2. **Nested Lists**:

   - Lists can contain other lists, creating a multi-dimensional structure.

   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   print(matrix[1][2])  # Output: 6
   ```

3. **Copying Lists**:

   - Shallow Copy: Creates a new list but references the same objects.
   - Deep Copy: Creates a new list and recursively copies all objects.

   ```python
   # Shallow Copy
   list1 = [1, 2, 3]
   list2 = list1.copy()  # or list2 = list1[:]
   list2[0] = 100
   print(list1)  # Output: [1, 2, 3]

   # Deep Copy
   import copy
   list3 = [[1, 2], [3, 4]]
   list4 = copy.deepcopy(list3)
   list4[0][0] = 100
   print(list3)  # Output: [[1, 2], [3, 4]]
   ```

4. **List Unpacking**:

   - Assign elements of a list to variables in a single statement.

   ```python
   a, b, c = [1, 2, 3]
   print(a, b, c)  # Output: 1 2 3
   ```

5. **List as Stack or Queue**:

   - Lists can be used as stacks (LIFO) using `append()` and `pop()`.
   - For queues (FIFO), use `collections.deque` for better performance.

   ```python
   # Stack
   stack = []
   stack.append(1)
   stack.append(2)
   stack.pop()  # Output: 2

   # Queue
   from collections import deque
   queue = deque()
   queue.append(1)
   queue.append(2)
   queue.popleft()  # Output: 1
   ```

6. **Filtering and Mapping**:

   - Use `filter()` and `map()` functions for functional programming.

   ```python
   numbers = [1, 2, 3, 4, 5]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   squares = list(map(lambda x: x**2, numbers))
   print(evens)    # Output: [2, 4]
   print(squares)  # Output: [1, 4, 9, 16, 25]
   ```

7. **List Sorting with Custom Keys**:

   - Use the `key` parameter in `sort()` or `sorted()` to sort based on a custom function.

   ```python
   words = ["apple", "banana", "cherry"]
   words.sort(key=lambda x: len(x))
   print(words)  # Output: ['apple', 'cherry', 'banana']
   ```

8. **List Concatenation and Repetition**:

   - Use `+` to concatenate lists and `*` to repeat lists.

   ```python
   list1 = [1, 2]
   list2 = [3, 4]
   combined = list1 + list2  # Output: [1, 2, 3, 4]
   repeated = list1 * 3      # Output: [1, 2, 1, 2, 1, 2]
   ```

9. **Memory Efficiency**:

   - Lists are dynamic arrays, which means they can grow in size, but this can lead to memory overhead.
   - For memory-efficient alternatives, consider using `array.array` or `numpy.array`.

10. **List vs. Tuple**:
    - Lists are mutable, while tuples are immutable.
    - Use tuples for fixed collections and lists for dynamic collections.

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # This will raise an error
```

---

By mastering these core and advanced concepts, you can effectively use lists in Python for a wide range of programming tasks.
