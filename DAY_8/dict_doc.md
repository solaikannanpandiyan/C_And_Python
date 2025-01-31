### Dictionaries in Python: Core and Advanced Concepts

#### **Core Concepts**

1. **Definition**:

   - A dictionary in Python is an unordered, mutable collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.
   - Dictionaries are defined using curly braces `{}` with key-value pairs separated by commas.

   ```python
   my_dict = {"name": "Alice", "age": 25, "city": "New York"}
   ```

2. **Accessing Values**:

   - Values are accessed using their keys.

   ```python
   print(my_dict["name"])  # Output: Alice
   ```

3. **Adding/Updating Key-Value Pairs**:

   - Add or update a key-value pair by assigning a value to a key.

   ```python
   my_dict["age"] = 26          # Update existing key
   my_dict["occupation"] = "Engineer"  # Add new key-value pair
   ```

4. **Deleting Key-Value Pairs**:

   - Use the `del` statement, `pop()`, or `popitem()` to remove key-value pairs.

   ```python
   del my_dict["city"]          # Remove key "city"
   age = my_dict.pop("age")     # Remove key "age" and return its value
   item = my_dict.popitem()     # Remove and return the last inserted key-value pair
   ```

5. **Common Methods**:

   - `keys()`: Returns a view of all keys.
   - `values()`: Returns a view of all values.
   - `items()`: Returns a view of all key-value pairs as tuples.
   - `get()`: Safely retrieves a value for a key (returns `None` or a default value if the key doesn't exist).
   - `update()`: Merges another dictionary into the current one.

   ```python
   print(my_dict.keys())    # Output: dict_keys(['name', 'occupation'])
   print(my_dict.values())  # Output: dict_values(['Alice', 'Engineer'])
   print(my_dict.items())   # Output: dict_items([('name', 'Alice'), ('occupation', 'Engineer')])
   print(my_dict.get("name", "Unknown"))  # Output: Alice
   my_dict.update({"age": 30, "city": "San Francisco"})  # Merge new key-value pairs
   ```

6. **Length**:

   - Use the `len()` function to get the number of key-value pairs.

   ```python
   print(len(my_dict))  # Output: 3
   ```

7. **Iteration**:

   - You can iterate over keys, values, or key-value pairs.

   ```python
   for key in my_dict:
       print(key, my_dict[key])

   for key, value in my_dict.items():
       print(key, value)
   ```

---

#### **Advanced Concepts**

1. **Dictionary Comprehensions**:

   - A concise way to create dictionaries using a single line of code.
   - Syntax: `{key_expression: value_expression for item in iterable if condition}`.

   ```python
   squares = {x: x**2 for x in range(5)}
   print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   ```

2. **Nested Dictionaries**:

   - Dictionaries can contain other dictionaries, creating a multi-level structure.

   ```python
   nested_dict = {
       "person1": {"name": "Alice", "age": 25},
       "person2": {"name": "Bob", "age": 30}
   }
   print(nested_dict["person1"]["name"])  # Output: Alice
   ```

3. **Default Values with `defaultdict`**:

   - Use `collections.defaultdict` to provide default values for missing keys.

   ```python
   from collections import defaultdict
   my_dict = defaultdict(int)  # Default value is 0
   my_dict["count"] += 1
   print(my_dict["count"])  # Output: 1
   ```

4. **Merging Dictionaries**:

   - Use the `|` operator (Python 3.9+) or the `update()` method to merge dictionaries.

   ```python
   dict1 = {"a": 1, "b": 2}
   dict2 = {"b": 3, "c": 4}
   merged = dict1 | dict2  # Output: {'a': 1, 'b': 3, 'c': 4}
   ```

5. **Dictionary Views**:

   - `keys()`, `values()`, and `items()` return view objects that dynamically reflect changes to the dictionary.

   ```python
   keys_view = my_dict.keys()
   my_dict["new_key"] = "new_value"
   print(keys_view)  # Output: dict_keys(['name', 'occupation', 'new_key'])
   ```

6. **Ordered Dictionaries**:

   - Use `collections.OrderedDict` to maintain insertion order (Python 3.7+ dictionaries are ordered by default).

   ```python
   from collections import OrderedDict
   ordered_dict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
   print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
   ```

7. **Dictionary as Switch-Case**:

   - Use dictionaries to emulate switch-case behavior.

   ```python
   def switch_case(value):
       return {
           "case1": "Result for case1",
           "case2": "Result for case2",
       }.get(value, "Default case")

   print(switch_case("case1"))  # Output: Result for case1
   ```

8. **Inverting a Dictionary**:

   - Swap keys and values using dictionary comprehensions.

   ```python
   original = {"a": 1, "b": 2, "c": 3}
   inverted = {v: k for k, v in original.items()}
   print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}
   ```

9. **Memory Efficiency**:

   - Dictionaries are highly optimized for fast lookups but can consume more memory than lists or tuples.

10. **Dictionary vs. List**:
    - Use dictionaries for key-value mappings and lists for ordered collections.
    - Dictionaries provide O(1) average time complexity for lookups, while lists provide O(n).

```python
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2, "c": 3}
```

11. **Handling Missing Keys**:

    - Use `setdefault()` to handle missing keys and set a default value if the key doesn't exist.

    ```python
    my_dict.setdefault("new_key", "default_value")
    print(my_dict["new_key"])  # Output: default_value
    ```

12. **Filtering Dictionaries**:

    - Use dictionary comprehensions to filter key-value pairs.

    ```python
    original = {"a": 1, "b": 2, "c": 3}
    filtered = {k: v for k, v in original.items() if v > 1}
    print(filtered)  # Output: {'b': 2, 'c': 3}
    ```

13. **Sorting Dictionaries**:

    - Use the `sorted()` function to sort keys, values, or items.

    ```python
    sorted_keys = sorted(my_dict.keys())
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1])  # Sort by value
    ```

14. **Immutable Dictionaries**:

    - Use `types.MappingProxyType` to create an immutable dictionary.

    ```python
    from types import MappingProxyType
    immutable_dict = MappingProxyType(my_dict)
    # immutable_dict["new_key"] = "value"  # This will raise an error
    ```

---

By mastering these core and advanced concepts, you can effectively use dictionaries in Python for a wide range of programming tasks, especially when fast lookups and key-value mappings are required.
