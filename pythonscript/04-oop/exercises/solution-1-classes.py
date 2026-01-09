#!/usr/bin/env python3
"""
Solution: Exercise 1 - Classes and Objects
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 1 - Classes and Objects")
print("=" * 60)

# Task 1: Define a simple class
class Person:
    pass

# Task 2: Add __init__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Task 3: Create an object
person = Person("Alice", 30)
print(f"1-3. Created person: {person.name}, {person.age}")

# Task 4: Add instance method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old"

person = Person("Alice", 30)
print(f"4. {person.greet()}")

# Task 5-6: Instance variables and access
person = Person("Bob", 25)
print(f"5-6. Name: {person.name}, Age: {person.age}")

# Task 7: Class variable
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(f"7. Species: {Person.species}")

# Task 8: Class method
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(f"8. Total persons: {Person.get_count()}")

# Task 9: Static method
class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(f"9. Is 20 adult? {Person.is_adult(20)}")

# Task 10: String representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 30)
print(f"10. {person}")

print("\n✅ Solution completed!")
