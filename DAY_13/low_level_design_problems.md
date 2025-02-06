# Real-Life Low-Level Design Problems

## 1. ATM/UPI Simulator

### Objective

Simulate an ATM/UPI system where users can perform transactions like withdrawing cash, depositing money, checking balance, and changing their PIN.

### OOP Concepts

- **Classes**: `ATM`, `BankAccount`, `Transaction`
- **Classes**: `UPI`, `BankAccount`, `Transaction`
- **Encapsulation**: Private attributes for account balance and PIN.
- **Methods**:
  - `withdraw(amount)`
  - `deposit(amount)`
  - `check_balance()`
  - `change_pin(old_pin, new_pin)`

### Problem-Solving

- Validate PIN before allowing transactions.
- Handle insufficient balance during withdrawals.
- Ensure thread safety (optional, for advanced learners).

---

## 2. E-Commerce Cart System

### Objective

Design a shopping cart system for an e-commerce platform. Users can add products, remove products, calculate the total cost, and apply discounts.

### OOP Concepts

- **Classes**: `Product`, `Cart`, `Discount`
- **Encapsulation**: Private attributes for product details and cart items.
- **Methods**:
  - `add_to_cart(product, quantity)`
  - `remove_from_cart(product)`
  - `calculate_total()`
  - `apply_discount(code)`

### Problem-Solving

- Handle out-of-stock products.
- Apply multiple discounts (e.g., percentage-based and fixed discounts).
- Ensure the cart updates correctly when products are removed.

---

## 3. Parking Lot Management System

### Objective

Design a system to manage a parking lot. The system should handle parking vehicles, calculating fees, and tracking available spots.

### OOP Concepts

- **Classes**: `ParkingLot`, `Vehicle`, `ParkingSpot`
- **Encapsulation**: Private attributes for spot availability and vehicle details.
- **Methods**:
  - `park_vehicle(vehicle)`
  - `unpark_vehicle(vehicle_id)`
  - `calculate_fee(vehicle_id)`
  - `check_availability()`

### Problem-Solving

- Handle different vehicle types (e.g., car, bike, truck) and assign appropriate spots.
- Calculate fees based on parking duration.
- Handle full parking lot scenarios.

---

## 4. Flight Booking System

### Objective

Design a system to manage flight bookings. Users can search for flights, book seats, and view their bookings.

### OOP Concepts

- **Classes**: `Flight`, `Passenger`, `Booking`
- **Encapsulation**: Private attributes for flight details and seat availability.
- **Methods**:
  - `search_flights(source, destination, date)`
  - `book_seat(flight_id, passenger)`
  - `cancel_booking(booking_id)`
  - `view_bookings(passenger_id)`

### Problem-Solving

- Handle seat availability and overbooking.
- Validate passenger details during booking.
- Allow cancellations and update seat availability.

---

## 5. Library Management System

### Objective

Build a system to manage books in a library. Users can add books, borrow books, return books, and view available books.

### OOP Concepts

- **Classes**: `Book`, `Library`
- **Inheritance**: `FictionBook` and `NonFictionBook` inheriting from `Book`
- **Composition**: `Library` contains a list of `Book` objects.

### Problem-Solving

- Track borrowed books and ensure a book cannot be borrowed twice.
- Handle exceptions like invalid book IDs.

---

## Why These Are Better for Real-Life Low-Level Design

1. **ATM Simulator**: Mimics real-world banking systems, requiring validation and transaction handling.
2. **E-Commerce Cart System**: Reflects the complexity of managing products, discounts, and user interactions in online shopping.
3. **Parking Lot Management System**: Requires handling multiple vehicle types, spot allocation, and fee calculation.
4. **Flight Booking System**: Involves managing dynamic data like seat availability and bookings, similar to real-world airline systems.
5. **Library Management System**: Teaches how to maintain inventory, enforce borrowing rules, and handle exceptions.
