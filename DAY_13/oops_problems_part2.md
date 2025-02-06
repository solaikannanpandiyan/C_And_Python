
### **Problem 6: Create a `Person` Class with Inheritance**
- Create a base class `Person` with the following attributes:
  - `name` (string): The name of the person.
  - `age` (int): The age of the person.
- Create a subclass `Employee` that inherits from `Person` and adds the following attributes:
  - `employee_id` (int): The ID of the employee.
  - `salary` (float): The salary of the employee.
- Add a method `display_info()` to both classes to print the details of the person/employee.

---

### **Problem 7: Create a `Shape` Abstract Class**
- Create an abstract class `Shape` with the following methods:
  - `area()`: Abstract method to calculate the area.
  - `perimeter()`: Abstract method to calculate the perimeter.
- Create two subclasses `Circle` and `Square` that inherit from `Shape` and implement the abstract methods.

---

### **Problem 8: Create a `ShoppingCart` Class**
- Create a class `ShoppingCart` with the following attributes:
  - `items` (list): A list of items in the cart (default is an empty list).
- Add the following methods:
  - `add_item(item, price)`: Adds an item and its price to the cart.
  - `remove_item(item)`: Removes an item from the cart.
  - `calculate_total()`: Calculates and returns the total price of all items in the cart.

---

### **Problem 9: Create a `Dog` Class**
- Create a class `Dog` with the following attributes:
  - `name` (string): The name of the dog.
  - `age` (int): The age of the dog.
  - `breed` (string): The breed of the dog.
- Add the following methods:
  - `bark()`: Prints a message like "Woof! Woof!".
  - `display_info()`: Prints the dog's name, age, and breed.

---

### **Problem 10: Create a `Bank` Class with Multiple Accounts**
- Create a class `Bank` with the following attributes:
  - `accounts` (list): A list of `BankAccount` objects (from Problem 2).
- Add the following methods:
  - `add_account(account)`: Adds a `BankAccount` object to the list.
  - `remove_account(account_holder)`: Removes a `BankAccount` object based on the account holder's name.
  - `total_balance()`: Calculates and returns the total balance of all accounts in the bank.

---