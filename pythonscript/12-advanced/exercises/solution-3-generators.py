#!/usr/bin/env python3
"""
Solution: Exercise 3 - Advanced Generators
"""
print("=" * 60)
print("Solution: Exercise 3 - Advanced Generators")
print("=" * 60)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("1. Countdown:")
for num in countdown(5):
    print(f"   {num}")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n2. Fibonacci (first 10):")
fib = fibonacci()
for i in range(10):
    print(f"   {next(fib)}")

def generator_with_send():
    while True:
        value = yield
        print(f"   Received: {value}")

gen = generator_with_send()
next(gen)
gen.send("Hello")
gen.send("World")

print("\n✅ Solution completed!")
