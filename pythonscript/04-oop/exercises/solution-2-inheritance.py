#!/usr/bin/env python3
"""
Solution: Exercise 2 - Inheritance
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 2 - Inheritance")
print("=" * 60)

# Task 1: Create parent class
class Animal:
    def speak(self):
        return "Some sound"

# Task 2: Create child class
class Dog(Animal):
    pass

# Task 3: Override method
class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(f"1-3. Dog speaks: {dog.speak()}")

# Task 4: Use super()
class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("Fluffy")
print(f"4. {cat.speak()}")

# Task 5: Multiple inheritance
class Bird(Animal):
    def fly(self):
        return "Flying!"

bird = Bird()
print(f"5. Bird: {bird.speak()}, {bird.fly()}")

# Task 6: Method resolution order
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"6. MRO: {D.__mro__}")

# Task 7: Abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"7. Rectangle area: {rect.area()}")

# Task 8: isinstance and issubclass
print(f"8. isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"   issubclass(Dog, Animal): {issubclass(Dog, Animal)}")

# Task 9: Multiple inheritance with super
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

print("9. Multiple inheritance init order:")
d = D()

# Task 10: Composition vs inheritance
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car = Car()
print(f"10. {car.start()}")

print("\n✅ Solution completed!")
