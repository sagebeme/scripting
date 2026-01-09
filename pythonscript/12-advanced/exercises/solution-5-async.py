#!/usr/bin/env python3
"""
Solution: Exercise 5 - Async Programming
"""
import asyncio

print("=" * 60)
print("Solution: Exercise 5 - Async Programming")
print("=" * 60)

async def greet(name):
    await asyncio.sleep(0.1)
    return f"Hello, {name}!"

async def main():
    result = await greet("Python")
    print(f"1. {result}")
    
    tasks = [greet("Alice"), greet("Bob"), greet("Charlie")]
    results = await asyncio.gather(*tasks)
    print(f"2. Results: {results}")

asyncio.run(main())

print("\n✅ Solution completed!")
