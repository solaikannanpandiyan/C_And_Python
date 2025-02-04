
---

### **Problem 1: Create a `Car` Class**
- Create a class `Car` with the following attributes:
  - `make` (string): The make of the car (e.g., "Toyota").
  - `model` (string): The model of the car (e.g., "Corolla").
  - `year` (int): The year the car was made.
  - `speed` (float): The current speed of the car (default is 0).
- Add the following methods:
  - `accelerate(speed_increase)`: Increases the car's speed by the given amount.
  - `brake(speed_decrease)`: Decreases the car's speed by the given amount.
  - `display_speed()`: Prints the current speed of the car.

---

### **Problem 2: Create a `BankAccount` Class**
- Create a class `BankAccount` with the following attributes:
  - `account_holder` (string): The name of the account holder.
  - `balance` (float): The current balance in the account (default is 0).
- Add the following methods:
  - `deposit(amount)`: Adds the given amount to the balance.
  - `withdraw(amount)`: Subtracts the given amount from the balance (ensure the balance doesn't go negative).
  - `display_balance()`: Prints the current balance.

---

### **Problem 3: Create a `Student` Class**
- Create a class `Student` with the following attributes:
  - `name` (string): The name of the student.
  - `age` (int): The age of the student.
  - `grades` (list): A list of grades (default is an empty list).
- Add the following methods:
  - `add_grade(grade)`: Adds a grade to the `grades` list.
  - `average_grade()`: Calculates and returns the average of the grades.
  - `display_info()`: Prints the student's name, age, and average grade.

---

### **Problem 4: Create a `Rectangle` Class**
- Create a class `Rectangle` with the following attributes:
  - `length` (float): The length of the rectangle.
  - `width` (float): The width of the rectangle.
- Add the following methods:
  - `area()`: Calculates and returns the area of the rectangle.
  - `perimeter()`: Calculates and returns the perimeter of the rectangle.
  - `is_square()`: Returns `True` if the rectangle is a square (length == width), otherwise `False`.

---

### **Problem 5: Create a `Library` Class**
- Create a class `Library` with the following attributes:
  - `books` (list): A list of book titles (default is an empty list).
- Add the following methods:
  - `add_book(title)`: Adds a book title to the `books` list.
  - `remove_book(title)`: Removes a book title from the `books` list.
  - `display_books()`: Prints all the books in the library.

---

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