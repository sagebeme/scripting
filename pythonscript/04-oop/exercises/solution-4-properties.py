#!/usr/bin/env python3
"""
Solution: Exercise 4 - Properties
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 4 - Properties")
print("=" * 60)

# Task 1: Create property with @property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

circle = Circle(5)
print(f"1. Radius: {circle.radius}")

# Task 2: Read-only property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"2. Area: {circle.area:.2f}")

# Task 3: Property with setter
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(5)
circle.radius = 10
print(f"3. New radius: {circle.radius}")

# Task 4: Property with deleter
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.deleter
    def radius(self):
        print("Radius deleted")
        self._radius = 0

circle = Circle(5)
del circle.radius
print(f"4. After delete: {circle.radius}")

# Task 5: Computed property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def diameter(self):
        return 2 * self._radius

circle = Circle(5)
print(f"5. Diameter: {circle.diameter}")

# Task 6: Property with validation
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Uses setter
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

circle = Circle(5)
print(f"6. Validated radius: {circle.radius}")

# Task 7: Cached property
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
    
    @property
    def area(self):
        if self._area is None:
            self._area = 3.14159 * self._radius ** 2
        return self._area

circle = Circle(5)
print(f"7. Cached area: {circle.area:.2f}")

# Task 8: Property with getter and setter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"8. Celsius: {temp.celsius}, Fahrenheit: {temp.fahrenheit:.1f}")

# Task 9: Property descriptor
class PositiveNumber:
    def __init__(self):
        self._value = None
    
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._value = value

class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(5, 3)
print(f"9. Rectangle: {rect.width} x {rect.height}")

# Task 10: Property with side effects
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        self._transactions = []
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        old_balance = self._balance
        self._balance = value
        self._transactions.append(f"Balance changed from {old_balance} to {value}")

account = BankAccount(100)
account.balance = 150
print(f"10. Balance: {account.balance}, Transactions: {len(account._transactions)}")

print("\n✅ Solution completed!")
