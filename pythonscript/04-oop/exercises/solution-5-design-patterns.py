#!/usr/bin/env python3
"""
Solution: Exercise 5 - Design Patterns
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 5 - Design Patterns")
print("=" * 60)

# Task 1: Singleton pattern
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"1. Singleton: s1 is s2 = {s1 is s2}")

# Task 2: Factory pattern
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def create_animal(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal type")

dog = create_animal("dog")
cat = create_animal("cat")
print(f"2. Factory: {dog.speak()}, {cat.speak()}")

# Task 3: Observer pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, event):
        print(f"   {self.name} received: {event}")

subject = Subject()
observer1 = Observer("Observer1")
observer2 = Observer("Observer2")
subject.attach(observer1)
subject.attach(observer2)
print("3. Observer pattern:")
subject.notify("Event occurred")

# Task 4: Strategy pattern
class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def calculate(self, a, b):
        return self.strategy.execute(a, b)

calc = Calculator(AddStrategy())
print(f"4. Strategy (Add): {calc.calculate(5, 3)}")
calc.strategy = MultiplyStrategy()
print(f"   Strategy (Multiply): {calc.calculate(5, 3)}")

# Task 5: Decorator pattern
class Component:
    def operation(self):
        return "Component"

class Decorator(Component):
    def __init__(self, component):
        self._component = component
    
    def operation(self):
        return f"Decorator({self._component.operation()})"

component = Component()
decorated = Decorator(component)
print(f"5. Decorator: {decorated.operation()}")

# Task 6: Builder pattern
class Pizza:
    def __init__(self):
        self.toppings = []
        self.size = None
    
    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza

pizza = PizzaBuilder().set_size("Large").add_topping("Cheese").add_topping("Pepperoni").build()
print(f"6. Builder: {pizza}")

# Task 7: Adapter pattern
class OldSystem:
    def old_method(self):
        return "Old data"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def new_method(self):
        return f"Adapted: {self.old_system.old_method()}"

old = OldSystem()
adapter = Adapter(old)
print(f"7. Adapter: {adapter.new_method()}")

# Task 8: Facade pattern
class Subsystem1:
    def operation1(self):
        return "Subsystem1 operation"

class Subsystem2:
    def operation2(self):
        return "Subsystem2 operation"

class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()
    
    def simplified_operation(self):
        return f"{self.subsystem1.operation1()}, {self.subsystem2.operation2()}"

facade = Facade()
print(f"8. Facade: {facade.simplified_operation()}")

# Task 9: Command pattern
class Command:
    def execute(self):
        pass

class Light:
    def on(self):
        return "Light is ON"
    
    def off(self):
        return "Light is OFF"

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.on()

light = Light()
command = LightOnCommand(light)
print(f"9. Command: {command.execute()}")

# Task 10: Template method pattern
class AbstractClass:
    def template_method(self):
        return f"{self.operation1()}, {self.operation2()}"
    
    def operation1(self):
        return "Default operation1"
    
    def operation2(self):
        return "Default operation2"

class ConcreteClass(AbstractClass):
    def operation2(self):
        return "Custom operation2"

concrete = ConcreteClass()
print(f"10. Template method: {concrete.template_method()}")

print("\n✅ Solution completed!")
