#!/usr/bin/env python3
"""
Solution: Exercise 1 - Decorators
"""
print("=" * 60)
print("Solution: Exercise 1 - Decorators")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "Done"

slow_function()

print("\n✅ Solution completed!")
