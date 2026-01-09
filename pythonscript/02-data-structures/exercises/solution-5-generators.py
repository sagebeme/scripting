#!/usr/bin/env python3
"""
Solution: Exercise 5 - Iterators and Generators
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 5 - Iterators and Generators")
print("=" * 60)

# Task 1: Create a generator function
def squares(n):
    """Generator that yields squares of numbers 1 to n"""
    for i in range(1, n + 1):
        yield i ** 2

# Task 2: Use the generator
print("1-2. Generator squares (first 5):")
gen = squares(10)
for i, val in enumerate(gen):
    if i >= 5:
        break
    print(f"   {val}")

# Task 3: Generator expression
squares_gen = (x**2 for x in range(1, 6))
print("\n3. Generator expression (first 5):")
for val in squares_gen:
    print(f"   {val}")

# Task 4: Infinite generator
def fibonacci():
    """Generator that yields Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n4. Fibonacci generator (first 10):")
fib = fibonacci()
for i in range(10):
    print(f"   {next(fib)}")

# Task 5: Generator with condition
def even_numbers(n):
    """Generator that yields even numbers"""
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

print("\n5. Even numbers generator (first 5):")
evens = even_numbers(10)
for i, val in enumerate(evens):
    if i >= 5:
        break
    print(f"   {val}")

# Task 6: Use next() with generator
print("\n6. Using next() with generator:")
gen = squares(5)
print(f"   First: {next(gen)}")
print(f"   Second: {next(gen)}")
print(f"   Third: {next(gen)}")

# Task 7: Generator pipeline
print("\n7. Generator pipeline (squares -> filter evens -> take first 5):")
squares_gen = (x**2 for x in range(1, 11))
evens_gen = (x for x in squares_gen if x % 2 == 0)
for i, val in enumerate(evens_gen):
    if i >= 5:
        break
    print(f"   {val}")

# Task 8: Generator with send()
def receiver():
    """Generator that can receive values"""
    while True:
        value = yield
        print(f"   Received: {value}")

print("\n8. Generator with send():")
rec = receiver()
next(rec)  # Start generator
rec.send("Hello")
rec.send("World")

# Task 9: Iterator protocol
class CountDown:
    """Custom iterator class"""
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

print("\n9. Custom iterator (countdown from 5):")
for num in CountDown(5):
    print(f"   {num}")

# Task 10: Generator for file reading
def read_lines(text):
    """Generator that reads text line by line"""
    for line in text.split('\n'):
        yield line

print("\n10. Generator for reading lines:")
lines = "line1\nline2\nline3"
for line in read_lines(lines):
    print(f"   {line}")

print("\n✅ Solution completed!")
